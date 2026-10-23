import sys
import json
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from scripts.build_full_funnel_matrix import build_theme_matcher, normalize_path

matcher = build_theme_matcher()

with open("07_REPORTS/data/ga4/landing-pages.json") as f:
    ga4_data = json.load(f)

rows = ga4_data["rows"]
project_stats = {}
total_sessions = 0
total_w2a = 0

# Track channels
channel_stats = {}

for r in rows:
    p = normalize_path(r["landing_page"])
    s = r.get("sessions", 0)
    w = r.get("onelink_clicks_track1", 0) + r.get("onelink_clicks_track2", 0)
    cg = r.get("channel_group", "Other")
    total_sessions += s
    total_w2a += w
    
    # Global channels
    if cg not in channel_stats:
        channel_stats[cg] = {"sessions": 0, "w2a": 0, "pages": set()}
    channel_stats[cg]["sessions"] += s
    channel_stats[cg]["w2a"] += w
    channel_stats[cg]["pages"].add(p)
    
    tid, tname, sec, mvol, proj, ptype = matcher(p)
    if proj not in project_stats:
        project_stats[proj] = {
            "sessions": 0, "w2a": 0, "pages": set(),
            "channels": {}
        }
    project_stats[proj]["sessions"] += s
    project_stats[proj]["w2a"] += w
    project_stats[proj]["pages"].add(p)
    if cg not in project_stats[proj]["channels"]:
        project_stats[proj]["channels"][cg] = {"sessions": 0, "w2a": 0}
    project_stats[proj]["channels"][cg]["sessions"] += s
    project_stats[proj]["channels"][cg]["w2a"] += w

print(f"Total rows: {len(rows):,}")
print(f"Total sessions: {total_sessions:,}")
print(f"Total W2A Clicks: {total_w2a:,} (Overall CR: {total_w2a/total_sessions*100:.2f}%)")
print(f"Total mapped projects: {len(project_stats):,}")

print("\n--- GLOBAL CHANNELS BREAKDOWN ---")
for c, st in sorted(channel_stats.items(), key=lambda x: -x[1]["sessions"]):
    s = st["sessions"]
    w = st["w2a"]
    pct = (s / total_sessions) * 100
    cr = (w / s * 100) if s > 0 else 0
    print(f"{c:20}: {s:>10,} sess ({pct:>5.1f}%) | {w:>7,} W2A (CR: {cr:>4.2f}%) | {len(st['pages']):>4} pages")

print("\n--- TOP 25 PROJECTS ---")
for p, st in sorted(project_stats.items(), key=lambda x: -x[1]["sessions"])[:25]:
    s = st["sessions"]
    w = st["w2a"]
    pages_cnt = len(st["pages"])
    cr = (w / s * 100) if s > 0 else 0
    pct = (s / total_sessions) * 100
    
    # Calculate non-paid vs paid for this project
    paid_s = sum(cv["sessions"] for ck, cv in st["channels"].items() if "paid" in ck.lower())
    non_paid_s = s - paid_s
    non_paid_pct = (non_paid_s / s * 100) if s > 0 else 0
    paid_pct = (paid_s / s * 100) if s > 0 else 0
    
    print(f"- {p:22}: {s:>9,} sess ({pct:>4.1f}%) | {w:>6,} W2A (CR: {cr:>4.2f}%) | Non-Paid: {non_paid_pct:>5.1f}% | Paid: {paid_pct:>4.1f}% | {pages_cnt:>4} pgs")
