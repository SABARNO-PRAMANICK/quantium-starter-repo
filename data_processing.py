import pandas as pd
import glob

# Path to the data folder containing the CSV files
data_files = glob.glob('data/daily_sales_data_*.csv')

# Initialize an empty DataFrame to hold the formatted data
formatted_data = pd.DataFrame(columns=['sales', 'date', 'region'])

# Process each CSV file
for file in data_files:
    # Load the data
    data = pd.read_csv(file)

    # Filter for "Pink Morsels" only
    pink_morsels_data = data[data['product'] == 'pink morsel']

    # Calculate the "sales" field by multiplying "quantity" by "price"
    pink_morsels_data['sales'] = pink_morsels_data['quantity'] * pink_morsels_data['price']

    # Select the relevant columns
    formatted_data = pd.concat([formatted_data, pink_morsels_data[['sales', 'date', 'region']]])

# Save the formatted data to a new CSV file
formatted_data.to_csv('data/formatted_sales_data.csv', index=False)
