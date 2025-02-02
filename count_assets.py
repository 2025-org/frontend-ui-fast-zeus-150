import pandas as pd

# Define input and output file paths
input_file = '/Users/idolourie/IDO/scripts/Connectors/weaknesses.csv'  # Replace with your input CSV file path
output_file = 'output_weaknesses.csv'  # Replace with your desired output CSV file path
column_name = 'IP'  # Replace with the column name you want to count

# Read the CSV file into a DataFrame
df = pd.read_csv(input_file)

# Count occurrences of each unique value in the specified column
counts = df[column_name].value_counts().reset_index()

# Rename columns for clarity
counts.columns = [column_name, 'Count']

# Convert the 'IP' column to a list, ignoring NaN values
ip_list = df[column_name].dropna().tolist()

# Print the list of IPs
print(ip_list)