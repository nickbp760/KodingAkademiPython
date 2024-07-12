import csv

# Initialize an empty list to store rows
data = []
laki2 = []
perempuan = []
# Specify the file path
csv_file = 'Basic Python 2/Dataset-1.csv'

# Open the CSV file
with open(csv_file, mode='r') as file:
    # Create a CSV reader object with comma as delimiter
    csv_reader = csv.reader(file, delimiter=',')

    # Iterate over each row in the CSV file
    for index, row in enumerate(csv_reader):
        # Append the row to the data list
        data.append(row)

        # Check the gender column (assuming it's the 5th column, index 4)
        if row[4] == 'Laki-laki':
            laki2.append(row)
        elif row[4] == 'Perempuan':
            perempuan.append(row)

# Print the data list (optional)
# print(data)

# Path untuk file CSV laki-laki
laki_laki_file = 'Basic Python 2/laki-laki/laki2.csv'
# Path untuk file CSV perempuan
perempuan_file = 'Basic Python 2/perempuan/perempuan.csv'

# Tulis data laki-laki ke file CSV
with open(laki_laki_file, mode='w', newline='') as file:
    csv_writer = csv.writer(file, delimiter=',')
    csv_writer.writerow(['No', 'Nama', 'Course', 'Kota', 'Gender'])  # Tulis header
    csv_writer.writerows(laki2)  # Tulis data laki-laki ke file

# Tulis data perempuan ke file CSV
with open(perempuan_file, mode='w', newline='') as file:
    csv_writer = csv.writer(file, delimiter=',')
    csv_writer.writerow(['No', 'Nama', 'Course', 'Kota', 'Gender'])  # Tulis header
    csv_writer.writerows(perempuan)  # Tulis data perempuan ke file

print(f"Data laki-laki telah ditulis ke file: {laki_laki_file}")
print(f"Data perempuan telah ditulis ke file: {perempuan_file}")
