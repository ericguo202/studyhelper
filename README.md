# Study Helper (Similar to Quizlet)
This Python script reads a CSV file of terms and their definitions and converts it into an array of objects, where each object represents a row in the CSV file. The objects are represented as dictionaries, with keys corresponding to the column headers. The program randomly chooses one definition from the list of definitions and asks the user to respond with the term. The game continues until the user inputs "stop".

## Requirements
- Python 3.x (Python 3.6 or later recommended)

## Installation
No additional packages are required since this script uses Python's built-in `csv`, random, and sys modules.

## Usage
1. Prepare a CSV file: Ensure you have a CSV file ready to be converted. For example, `example.csv`.
2. Edit the script: Update the file_path variable in the script to point to your CSV file.
3. Run the script:
    ```bash
    python main.py
    ```
4. Output: The script will print the array of dictionaries to the console.

## License
This project is licensed under the MIT License