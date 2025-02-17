import os
import pandas as pd
from thermal_outage_rates_functions import get_outage_curve
import argparse

# Define input and output directories
# Set up argument parser
parser = argparse.ArgumentParser(description="Process thermal outage data.")
parser.add_argument('--input_dir', type=str, required=True, help='Path to the input directory containing CSV files.')
parser.add_argument('--output_dir', type=str, required=True, help='Path to the output directory for saving processed files.')

args = parser.parse_args()

# Define input and output directories from arguments
input_dir = args.input_dir
output_dir = args.output_dir

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

plant_types = ["CC", "CT", "DS", "HD", "NU", "ST"]

# Process each CSV file in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith(".csv"):
        for plant_type in plant_types:
            # Define the input path
            input_path = os.path.join(input_dir, filename)
            
            # Read the CSV file into a DataFrame
            df = pd.read_csv(input_path)
            
            # Process the DataFrame using get_outage_curve
            result_df = get_outage_curve(df, plant_type)
            
            # Define the output path
            output_filename = f"{filename}_{plant_type}_outage.csv"
            output_path = os.path.join(output_dir, output_filename)
            
            # Save the processed DataFrame to CSV
            result_df.to_csv(output_path, index=False)
            
            print(f"Processed and saved: {output_path}")
        

print("All files processed successfully.")
