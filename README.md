
# amazon_massive_dataset

Brief project description.

## Table of Contents
- [Dependencies](#dependencies)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Dependencies

Ensure you have the following dependencies installed:
- Python 3.x
- Pandas: You can install it using pip with `pip install pandas`

## Getting Started

Clone the repository to get started:

```bash
git clone https://github.com/your-username/your-project.git
cd your-project
```

## Usage

Describe how to use your project here. Provide examples and usage instructions.

## Configuration

To configure the project for your specific environment, you may need to make the following changes:

1. **Data Directory**: Update the `data_directory` variable in the code to point to the directory containing your JSONL files.
   
   ```python
   data_directory = r'path/to/your/data_directory'
   ```

2. **Output Directory**: Update the `output_dir` variable to specify where you want to save the generated Excel files.
   
   ```python
   output_dir = r'path/to/your/output_directory'
   ```

3. **Keyword and Field**: When running the script, you can specify the keyword and field for filtering using the `--keyword` and `--field` arguments.
   
   ```shell
   python script_name.py --keyword your_keyword --field your_field
   ```
