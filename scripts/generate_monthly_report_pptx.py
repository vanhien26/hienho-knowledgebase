#!/usr/bin/env python3
"""
Generate Web Platform Monthly Business Review PPTX (7 Slides)
Standardized 100% against MoMo Reporting Guidelines & Templates.
This script delegates directly to scripts/build_templated_pptx.py (SSOT).
"""
import sys
from pathlib import Path

# Add script directory to sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_templated_pptx import main

if __name__ == "__main__":
    main()
