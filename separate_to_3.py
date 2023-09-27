import json
import os
import pandas as pd

# Specify the source directory for the JSONL data
source_directory = r'C:\Users\joseph\Downloads\Compressed\1.1\data'

# Step 1: Load and Prepare the Dataset using pandas
source_files = [os.path.join(source_directory, filename) for filename in os.listdir(source_directory) if filename.endswith('.jsonl')]

for source_file in source_files:
    try:
        df = pd.read_json(source_file, lines=True, encoding='utf-8')
    except FileNotFoundError as e:
        print(f"Error: JSONL file not found: {source_file}")
        continue
    except Exception as e:
        print(f"Error: Failed to read JSONL file: {source_file}")
        print(f"Error Details: {str(e)}")
        continue

    # Step 2: Partition Data by Language and Split into Test, Train, and Dev Sets
    languages = {'en': df[df['locale'].str.startswith('en')],
                 'sw': df[df['locale'].str.startswith('sw')],
                 'de': df[df['locale'].str.startswith('de')]}

    # Define the partition ratios (you can adjust these ratios as needed)
    partition_ratios = {'test': 0.1, 'train': 0.7, 'dev': 0.2}

    # Step 3: Write Data to JSONL Files using pandas
    output_directory = r'C:\Users\joseph\PycharmProjects\pythonProject3\partitions_ttd'
    os.makedirs(output_directory, exist_ok=True)

    for lang, lang_df in languages.items():
        partitioned_data = {}
        total_entries = len(lang_df)
        for partition, ratio in partition_ratios.items():
            ratio_values = list(partition_ratios.values())  # Convert to a list
            start_idx = int(total_entries * sum(ratio_values[:list(partition_ratios.keys()).index(partition)]))
            end_idx = int(total_entries * (sum(ratio_values[:list(partition_ratios.keys()).index(partition)]) + ratio))
            partitioned_data[partition] = lang_df.iloc[start_idx:end_idx]

        for partition, data_df in partitioned_data.items():
            output_file = os.path.join(output_directory, f'{os.path.splitext(os.path.basename(source_file))[0]}_{lang}_{partition}.jsonl')
            data_df.to_json(output_file, orient='records', lines=True, force_ascii=False)

print('JSONL files generated successfully.')
