#!/usr/bin/env python3
"""Shim - canonical source: scripts/generate_pptx.py (single source, do not duplicate)."""
import runpy
from pathlib import Path
runpy.run_path(str(Path(__file__).resolve().parents[2] / "scripts" / "generate_pptx.py"), run_name="__main__")
