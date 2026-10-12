#!/usr/bin/env python3
"""Watcher don gian: poll intake folder, tu go intake.py khi co file moi.

Chay thu cong:
  python3 scripts/watch_intake.py

Hoac cai launchd (macOS) de chay nen:
  python3 scripts/watch_intake.py --install
  python3 scripts/watch_intake.py --uninstall
"""

import argparse
import os
import subprocess
import sys
import time

INTAKE_DIR = os.path.expanduser("~/Downloads/intake")
POLL_SECONDS = 5
INTEGRITY_DEBOUNCE = 2  # cho file stable truoc khi xu ly (tranh doc dang copy)

INTAKE_PY = os.path.join(os.path.dirname(os.path.abspath(__file__)), "intake.py")
PLIST_LABEL = "com.hienho.intake-agent"
PLIST_PATH = os.path.expanduser(f"~/Library/LaunchAgents/{PLIST_LABEL}.plist")


def snapshot():
    out = {}
    if not os.path.isdir(INTAKE_DIR):
        return out
    for f in os.listdir(INTAKE_DIR):
        p = os.path.join(INTAKE_DIR, f)
        if os.path.isfile(p) and not f.startswith("."):
            try:
                st = os.stat(p)
                out[p] = (st.st_mtime, st.st_size)
            except OSError:
                pass
    return out


def process_new(prev, curr):
    new_or_changed = []
    for path, sig in curr.items():
        if path not in prev or prev[path] != sig:
            new_or_changed.append(path)
    for path in new_or_changed:
        time.sleep(INTEGRITY_DEBOUNCE)
        sig_now = snapshot().get(path)
        if sig_now != curr[path]:
            print(f"[WATCH] {os.path.basename(path)} dang copy, bo qua lan nay.")
            continue
        print(f"[WATCH] Phat hien file moi: {os.path.basename(path)} - chay intake...")
        res = subprocess.run(
            [sys.executable, INTAKE_PY, "--file", path, "--push"],
            capture_output=False,
        )
        if res.returncode != 0:
            print(f"[WATCH] Intake loi voi {path} (exit {res.returncode})")


def run_forever():
    os.makedirs(INTAKE_DIR, exist_ok=True)
    print(f"[WATCH] Dang giam sat {INTAKE_DIR} (poll {POLL_SECONDS}s). Ctrl+C de dung.")
    prev = snapshot()
    try:
        while True:
            time.sleep(POLL_SECONDS)
            curr = snapshot()
            process_new(prev, curr)
            prev = curr
    except KeyboardInterrupt:
        print("\n[WATCH] Da dung.")


def install_launchd():
    script_path = os.path.abspath(__file__)
    python_bin = sys.executable
    plist = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>{PLIST_LABEL}</string>
    <key>ProgramArguments</key>
    <array>
        <string>{python_bin}</string>
        <string>{script_path}</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <true/>
    <key>StandardOutPath</key>
    <string>/tmp/intake-agent.log</string>
    <key>StandardErrorPath</key>
    <string>/tmp/intake-agent.err.log</string>
</dict>
</plist>
"""
    os.makedirs(os.path.dirname(PLIST_PATH), exist_ok=True)
    with open(PLIST_PATH, "w", encoding="utf-8") as f:
        f.write(plist)
    subprocess.run(["launchctl", "unload", PLIST_PATH], capture_output=True)
    subprocess.run(["launchctl", "load", PLIST_PATH], check=False)
    print(f"Da cai launchd agent: {PLIST_PATH}")


def uninstall_launchd():
    if os.path.exists(PLIST_PATH):
        subprocess.run(["launchctl", "unload", PLIST_PATH], capture_output=True)
        os.remove(PLIST_PATH)
        print("Da go launchd agent.")
    else:
        print("Chua cai launchd agent.")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--install", action="store_true", help="Cai lam launchd agent (chay nen)")
    ap.add_argument("--uninstall", action="store_true", help="Go launchd agent")
    args = ap.parse_args()
    if args.install:
        install_launchd()
        return
    if args.uninstall:
        uninstall_launchd()
        return
    run_forever()


if __name__ == "__main__":
    main()
