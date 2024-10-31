import csv

# Define the path to the input and output files
input_file_path = 'data/daily_sales_data_0.csv'
output_file_path = 'data/formatted_sales_data.csv'

# Initialize the output data list
output_data = []

# Open and process the CSV file
with open(input_file_path, mode='r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Skip header row

    for input_row in reader:
        # Check if the row has the expected number of columns
        if len(input_row) < 4:
            print(f"Skipping row with missing values: {input_row}")
            continue  # Skip rows with missing columns

        try:
            product = input_row[0].strip().lower()
            quantity = int(input_row[1])
            price = float(input_row[2])
            transaction_date = input_row[3]
            region = input_row[4] if len(input_row) > 4 else "Unknown"  # Use "Unknown" if region is missing

            # Only process "pink morsel" product
            if product == "pink morsel":
                sales = quantity * price
                output_data.append([sales, transaction_date, region])
        except ValueError as e:
            print(f"Error processing row {input_row}: {e}")

# Write the formatted data to the output CSV file
with open(output_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["sales", "date", "region"])  # Write header
    writer.writerows(output_data)

print("Data processing complete. Output saved to:", output_file_path)
