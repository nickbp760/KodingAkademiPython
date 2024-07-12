from datetime import datetime

# Mendapatkan datetime sekarang
now = datetime.now()
print(now)

# Format pertama: Sun, 18-07-2022 06:29:40
formatted_1 = now.strftime('%a, %d-%m-%Y %H:%M:%S')
print(formatted_1)

# Format kedua: Tue Aug 16 21:30:00 1988
# Misalnya kita menggunakan datetime yang diberikan
specific_datetime = datetime(1988, 8, 16, 21, 30, 0)
formatted_2 = specific_datetime.strftime('%a %b %d %H:%M:%S %Y')
print(formatted_2)

# Format ketiga: Monday, 07 March 2022
formatted_3 = now.strftime('%A, %d %B %Y')
print(formatted_3)

# Format datetime yang ada
datetime_str = "Tue Aug 16 21:30:00 1988"
datetime_obj = datetime.strptime(datetime_str, '%a %b %d %H:%M:%S %Y')
print(datetime_obj)
