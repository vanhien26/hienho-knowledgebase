"""Parse Web Performance Tracking xlsx -> SSOT + snapshots.

Gọi lại sync_tracking_report.py với --no-push để tái sử dụng logic parse
(code Single Source of Truth, không duplicate). Push do intake.py điều phối.
"""

import os
import subprocess
import sys

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
SYNC_SCRIPT = os.path.join(BASE_DIR, "scripts", "sync_tracking_report.py")


def parse(file_path, dry_run=True):
    """Chạy sync_tracking_report.py --file <file> --no-push.

    Trả về dict summary hoặc raise RuntimeError.
    """
    cmd = [sys.executable, SYNC_SCRIPT, "--file", file_path, "--no-push"]
    res = subprocess.run(cmd, capture_output=True, text=True, cwd=BASE_DIR)
    if res.returncode != 0:
        raise RuntimeError(f"sync_tracking_report failed: {res.stderr.strip() or res.stdout.strip()}")
    print(res.stdout.strip())
    return {"parser": "tracking", "source": file_path, "log": res.stdout.strip()}
