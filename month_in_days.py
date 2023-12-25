md = {
    'January': 31,
    'February': '28/29',
    'March': 31,
    'April': 30,
    'May': 31,
    'June': 30,
    'July': 31,
    'August': 31,
    'September': 30,
    'October': 31,
    'November': 30,
    'December': 31
}
month_name = input("Input the name of the Month: ")
if month_name in md:
    days = md[month_name]
    print(f"No. of days: {days} days")
else:
    print("Invalid month name")
