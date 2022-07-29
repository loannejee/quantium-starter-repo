import csv
import os

DATA_DIRECTORY = "./data"
OUTPUT_FILE_PATH = "./combined_and_cleaned_2.csv"

# open the OUTPUT file to write in it:
with open(OUTPUT_FILE_PATH, "w") as output_file:
    csv_writer = csv.writer(output_file)

    # add a csv header
    header = ["sales", "date", "region"]
    csv_writer.writerow(header)

    # iterate through all the csv files in the data directory
    for file_name in os.listdir(DATA_DIRECTORY):
        # open the csv file for reading
        with open(f"{DATA_DIRECTORY}/{file_name}", "r") as input_file:
            reader = csv.reader(input_file)
            
            # iterate through each row in the csv file
            # row_index initialized to 0
            row_index = 0 
            for input_row in reader:
                # if this row is not the csv header, process it
                if row_index > 0:
                    # collect data from row
                    product = input_row[0]
                    price = float(input_row[1][1:])
                    quantity = int(input_row[2])
                    transaction_date = input_row[3]
                    region = input_row[4]

                    # if this is a pink morsel transaction, process it
                    if product == "pink morsel":
                        # finish formatting data
                        sale = price * quantity

                        # write the row to output file
                        output_row = ["${:.2f}".format(sale), transaction_date, region]
                        csv_writer.writerow(output_row)
                row_index += 1