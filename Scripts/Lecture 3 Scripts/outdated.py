"""
GOALS:
- implement a program that prompts the user fpr a date in month-day-year order
- formatted like 9/8/1636 or September 8,1636
- wherein the month of the latter might by any of the values in the list below
- then outputs the same date in yyyy-mm-dd format
- if users input not valid date in either format, then prompt again
"""

month_list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

month_num = {
    "January": "01", "February": "02", "March": "03",
    "April": "04", "May": "05", "June": "06",
    "July": "07", "August": "08", "September": "09",
    "October": "10", "November": "11", "December": "12"
}


def main():
    month, day, year = get_date()
    print(f"{year}-{month}-{day}")

def get_date():
    while True:
        try:
            m, d, y = break_date()
            d = d.zfill(2)
            y = y.strip()

            if m in month_list:
                month = month_num[m]
            elif m.isdigit() and 1 <= int(m) <= 12:
                month = str(m).zfill(2)
            else:
                continue

            if 1 <= int(d) <= 31:
                return month, d, y
        except:
            continue

def break_date():
    date_entry = input("Date: ").strip()

    if '/' in date_entry:
        parts = date_entry.split('/')
        if len(parts) != 3:
            raise ValueError("Invalid slash format")
        m, d, y = parts
    elif ',' in date_entry:
        try:
            m_d, y = date_entry.split(',')
            m, d = m_d.strip().split()
        except ValueError:
            raise ValueError("Invalid comma format")
    else:
        raise ValueError("Invalid format")

    return m.strip(), d.strip(), y.strip()

main()
