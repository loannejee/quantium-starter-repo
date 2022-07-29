import csv

data_0 = open('data/daily_sales_data_0.csv', encoding="utf-8")
csv_data_0 = csv.reader(data_0)
data_0_lines = list(csv_data_0)
data_0_lines_pink = []

for line in data_0_lines:
    if "pink" in line[0]:
        data_0_lines_pink.append(line)

# ==============================================================

data_1 = open('data/daily_sales_data_1.csv', encoding="utf-8")
csv_data_1 = csv.reader(data_1)
data_1_lines = list(csv_data_1)
data_1_lines_pink = []

for line in data_1_lines:
    if "pink" in line[0]:
        data_1_lines_pink.append(line)

# ==============================================================

data_2 = open('data/daily_sales_data_2.csv', encoding="utf-8")
csv_data_2 = csv.reader(data_2)
data_2_lines = list(csv_data_2)
data_2_lines_pink = []

for line in data_2_lines:
    if "pink" in line[0]:
        data_2_lines_pink.append(line)

# ==============================================================

f = open('data/combined_and_cleaned.csv','a',newline='')

csv_writer = csv.writer(f)

# Add title row:
# csv_writer.writerow(['Sales','Date','Region'])

# for line in data_0_lines_pink:
#     price = float(line[1][1:])
#     quantity = int(line[2])
#     sales = price * quantity
#     date = line[3]
#     region = line[4]
#     clean_line = ["${:.2f}".format(sales), date, region]
#     csv_writer.writerow(clean_line)

# for line in data_1_lines_pink:
#     price = float(line[1][1:])
#     quantity = int(line[2])
#     sales = price * quantity
#     date = line[3]
#     region = line[4]
#     clean_line = ["${:.2f}".format(sales), date, region]
#     csv_writer.writerow(clean_line)

# for line in data_2_lines_pink:
#     price = float(line[1][1:])
#     quantity = int(line[2])
#     sales = price * quantity
#     date = line[3]
#     region = line[4]
#     clean_line = ["${:.2f}".format(sales), date, region]
#     csv_writer.writerow(clean_line)