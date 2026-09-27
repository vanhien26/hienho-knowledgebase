"""Core utility library for Web Platform automation scripts."""
from scripts.lib.excel_utils import EXCEL_STYLES, load_workbook_safe, repo_root, save_with_backup

__all__ = ["repo_root", "load_workbook_safe", "save_with_backup", "EXCEL_STYLES"]
