era = "AD"
tuple_month = 1998, "januray", "30", era
tuple_time = "day", "night", 24, 60, ("minute", "hour", "second")

tahun, bulan, tanggal, jaman = tuple_month
for i in tuple_month:
    print(i, end=' ')
print()
print(".........................................................................................")
tuple_all = tuple_month + tuple_time
print(tuple_all)
