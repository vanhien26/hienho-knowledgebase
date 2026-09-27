import openpyxl


from scripts._lib import load_workbook_safe, save_with_backup, standard_argparser

def main(args=None):
    wb = load_workbook_safe('05_HUBS/financial-hub-roadmap.xlsx')

    for s in ['Roadmap', 'Utilities', 'Content Plan']:
        ws = wb[s]
        for r in range(1, ws.max_row + 1):
            for c in range(1, ws.max_column + 1):
                val = str(ws.cell(row=r, column=c).value or '')
                if 'realtime' in val:
                    new_val = val.replace('realtime', 'trực tuyến').replace('Realtime', 'Trực Tuyến')
                    ws.cell(row=r, column=c).value = new_val
                    print(f"Cleaned {s} Row {r} Col {c}: {new_val[:60]}")

    save_with_backup(wb, '05_HUBS/financial-hub-roadmap.xlsx', dry_run=args.dry_run, make_backup=not args.no_backup)
    print("Successfully replaced 'realtime' with natural Vietnamese 'trực tuyến' / 'mới nhất' in Excel!")

if __name__ == "__main__":
    _ap = standard_argparser("Fix runner - safe with --dry-run")
    main(_ap.parse_args())

