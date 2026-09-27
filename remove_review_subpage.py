import openpyxl


from scripts._lib import load_workbook_safe, save_with_backup, standard_argparser

def main(args=None):
    wb = load_workbook_safe('05_HUBS/student-hub-roadmap.xlsx')

    # 1. Update Roadmap Sheet
    if 'Roadmap' in wb.sheetnames:
        ws = wb['Roadmap']
        rows_to_delete = []
        for r in range(4, ws.max_row+1):
            item_val = ws.cell(row=r, column=4).value or ''
            if '/review' in str(item_val):
                rows_to_delete.append(r)
    
        for r in reversed(rows_to_delete):
            ws.delete_rows(r)
        print(f'Deleted {len(rows_to_delete)} row(s) containing /review from Roadmap sheet.')

    # 2. Update Sitemap Sheet
    if 'Sitemap' in wb.sheetnames:
        ws_sm = wb['Sitemap']
        rows_to_delete_sm = []
        for r in range(4, ws_sm.max_row+1):
            url_val = ws_sm.cell(row=r, column=4).value or ''
            name_val = ws_sm.cell(row=r, column=3).value or ''
            if '/review' in str(url_val) or 'Review' in str(name_val):
                rows_to_delete_sm.append(r)
            
        for r in reversed(rows_to_delete_sm):
            ws_sm.delete_rows(r)
        print(f'Deleted {len(rows_to_delete_sm)} row(s) containing /review from Sitemap sheet.')

    # 3. Update Readme Sheet text if present
    if 'Readme' in wb.sheetnames:
        ws_rd = wb['Readme']
        for r in range(1, ws_rd.max_row+1):
            for c in range(1, ws_rd.max_column+1):
                val = ws_rd.cell(row=r, column=c).value
                if val and '/review' in str(val):
                    new_val = str(val).replace(', /review', '').replace('/review, ', '').replace('/review', '')
                    ws_rd.cell(row=r, column=c, value=new_val)

    save_with_backup(wb, '05_HUBS/student-hub-roadmap.xlsx', dry_run=args.dry_run, make_backup=not args.no_backup)
    print('Successfully removed standalone /review subpage from student-hub-roadmap.xlsx!')

if __name__ == "__main__":
    _ap = standard_argparser("Fix runner - safe with --dry-run")
    main(_ap.parse_args())

