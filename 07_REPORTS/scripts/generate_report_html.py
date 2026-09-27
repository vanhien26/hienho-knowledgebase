#!/usr/bin/env python3
"""Shim - canonical source: scripts/generate_report_html.py (single source, do not duplicate)."""
import runpy
from pathlib import Path
runpy.run_path(str(Path(__file__).resolve().parents[2] / "scripts" / "generate_report_html.py"), run_name="__main__")
