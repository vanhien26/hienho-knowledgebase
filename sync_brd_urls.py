

from scripts._lib import load_workbook_safe, save_with_backup, standard_argparser


def main(args=None):
    with open('05_HUBS/financial-hub-brd.md', 'r', encoding='utf-8') as f:
        text = f.read()

    # Update URL references in BRD
    text_new = text.replace('`/gia-vang`', '`/tai-chinh/gia-vang`')
    text_new = text_new.replace('`/tinh-luong`', '`/tai-chinh/tinh-luong`')
    text_new = text_new.replace('`/lai-suat`', '`/tai-chinh/gui-tiet-kiem`')

    if text_new != text:
        if args is not None and args.dry_run:
            print('[dry-run] skip write: 05_HUBS/financial-hub-brd.md')
            return
        with open('05_HUBS/financial-hub-brd.md', 'w', encoding='utf-8') as f:
            f.write(text_new)
        print('Successfully synced BRD URLs to /tai-chinh/*')
    else:
        print('BRD already clean.')

if __name__ == "__main__":
    _ap = standard_argparser("Fix runner - safe with --dry-run")
    main(_ap.parse_args())

