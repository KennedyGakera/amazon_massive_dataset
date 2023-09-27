import json
import pandas as pd
import os
import argparse  # For command-line arguments

# Specify the directory containing the JSONL files
data_directory = r'C:\Users\joseph\Downloads\Compressed\1.1\data'

# Specify the output directory for Excel files
output_dir = r'C:\Users\joseph\PycharmProjects\pythonProject3\output_excel_files'
os.makedirs(output_dir, exist_ok=True)

def process_jsonl_file(file_path, keyword, filter_field):
    # Extract language code from the filename
    language_code = os.path.splitext(os.path.basename(file_path))[0]
    output_file = os.path.join(output_dir, f'{language_code}-{keyword}.xlsx')

    # Check if the file already exists
    if os.path.isfile(output_file):
        print(f"Warning: Excel file already exists, skipping: {output_file}")
        return

    # Read the JSONL file
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = [json.loads(line) for line in file]
    except FileNotFoundError as e:
        print(f"Error: JSONL file not found: {file_path}")
        return
    except Exception as e:
        print(f"Error: Failed to read JSONL file: {file_path}")
        print(f"Error Details: {str(e)}")
        return

    # Convert the data to a DataFrame
    df = pd.DataFrame(data)

    # Filter records where the specified keyword appears in the specified field
    filtered_df = df[df[filter_field].str.contains(keyword, case=False)]

    # Save the filtered DataFrame to an Excel file
    if len(filtered_df) > 0:
        try:
            filtered_df.to_excel(output_file, index=False)
            print(f"Excel file saved: {output_file}")
        except Exception as e:
            print(f"Error: Failed to save Excel file: {output_file}")
            print(f"Error Details: {str(e)}")
    else:
        print(f"No records found in JSONL file matching '{keyword}' in field '{filter_field}': {file_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process JSONL files and generate Excel files based on keyword and field.")
    parser.add_argument("--keyword", type=str, help="Specify the keyword to filter (e.g., 'english').")
    parser.add_argument("--field", type=str, help="Specify the field for filtering (e.g., 'utt').")

    args = parser.parse_args()

    if args.keyword and args.field:
        # Process all JSONL files in the data directory
        for filename in os.listdir(data_directory):
            if filename.endswith('.jsonl'):
                file_path = os.path.join(data_directory, filename)
                process_jsonl_file(file_path, args.keyword, args.field)
    else:
        print("Error: Both --keyword and --field arguments are required.")
