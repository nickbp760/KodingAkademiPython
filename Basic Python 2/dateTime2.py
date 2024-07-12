from datetime import datetime, timezone
import pytz
import time

# Mendapatkan waktu sekarang
waktu_komputer_now = datetime.now()
print(waktu_komputer_now)
waktu_komputer = datetime.now(timezone.utc)
print(waktu_komputer)

# Daftar zona waktu yang ingin ditampilkan
timezones = ['America/Los_Angeles', 'Europe/London', 'Asia/Jakarta', 'Australia/Sydney']

# Menampilkan waktu dalam empat zona waktu berbeda
for tz in timezones:
    timezone = pytz.timezone(tz)
    local_time = waktu_komputer.astimezone(timezone)
    formatted_time = local_time.strftime('%H:%M:%S')
    print(f'Time in {tz}: {formatted_time}')


datetime_america = datetime(2024, 7, 7, 12, 43, 00, tzinfo=pytz.timezone('America/Los_Angeles'))
print(datetime_america)
datetime_indonesia = datetime_america.astimezone(pytz.timezone('Asia/Jakarta'))
print(datetime_indonesia)


minutes = int(input("Masukkan menit: "))
seconds = int(input("Masukkan detik: "))
total_seconds = minutes * 60 + seconds
time.sleep(total_seconds)
print(f"Waktu selesai setelah {minutes} menit dan {seconds} detik.")
