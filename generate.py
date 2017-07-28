from csv import DictWriter
from collections import defaultdict
from datetime import date, timedelta


def get_scriptures_per_day():
    r = []
    with open('passages.txt') as f:
        for days_of_month in [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]:
            scriptures_of_month = defaultdict(list)
            for passage_id in range(4):
                for day in range(days_of_month):
                    scriptures_of_month[day].append(f.readline().strip())
            passages_list = [v for k, v in sorted(scriptures_of_month.items())]
            r.extend(passages_list)
    return r


def get_column_widths(scr):
    col_widths = []
    for col in zip(*scr):
        sorted_by_str_len = sorted(col, key=lambda v: len(v))
        col_widths.append(len(sorted_by_str_len[-1]))
    return col_widths


def write_rst(scr, col_widths, start_date):
    with open('output.rst', 'w') as f:
        def make_line(fields):
            line = '|'
            for field, width in zip(fields, [10] + col_widths):
                line += ' {} |'.format(field.ljust(width))
            return line + '\n'

        def make_sep(fill='-'):
            line = '+{}+'.format(fill * 12)
            for width in col_widths:
                line += '{}+'.format(fill * (width + 2))
            return line + '\n'

        # Write header
        f.write(make_sep())
        f.write(make_line(['Date'] + ['Family'] * 2 + ['Private'] * 2))
        f.write(make_sep('='))

        for day_offset, scriptures_of_day in enumerate(scr):
            day = start_date + timedelta(days=day_offset)
            f.write(make_line([day.isoformat()] + scriptures_of_day))
            f.write(make_sep())


def write_csv(scr, start_date):
    with open('output.csv', 'w', newline='') as f:
        field_names = ['Family 1', 'Family 2', 'Private 1', 'Private 2']
        writer = DictWriter(f, ['Date'] + field_names)
        writer.writeheader()
        for day_offset, scriptures_of_day in enumerate(scr):
            day = start_date + timedelta(days=day_offset)
            line = {'Date': day.isoformat()}
            line.update(dict(zip(field_names, scriptures_of_day)))
            writer.writerow(line)


scr = get_scriptures_per_day()
col_widths = get_column_widths(scr)
write_rst(scr, col_widths, date(2017, 7, 9))
write_csv(scr, date(2017, 7, 9))
