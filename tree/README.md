# Directory Tree Generator

## Description
This Python script generates a visual representation of a directory structure, similar to the `tree` command in Linux. It recursively traverses the directory and prints a tree-like structure, including a count of total directories and files.

## Features
- Recursively lists directories and files in a tree format.
- Uses ASCII characters to create a visually structured output.
- Counts the total number of directories and files.
- Supports command-line arguments to specify a target directory.

## Installation
Ensure you have Python installed on your system.

```sh
# Clone the repository (if applicable)
git clone <repository-url>
cd <repository-folder>
```

## Usage
Run the script without arguments to display the current directory structure:

```sh
python tree.py
```

Run the script with a specific directory as an argument:

```sh
python tree.py path/to/directory
```

## Example Output
```
.
├─ folder1
│   ├─ file1.txt
│   ├─ file2.txt
│   └─ subfolder1
│       ├─ file3.txt
│       └─ file4.txt
└─ folder2
    ├─ file5.txt
    └─ file6.txt
Total directories: 3
Total files: 6
```

## Code Structure
- `print_dir(directory, prefix='')`: Recursively prints the directory structure.
- Counts the number of directories and files.
- Uses ASCII symbols for tree formatting (`├─`, `└─`, `│   `, `    `).

## License
This project is licensed under the MIT License.

## Author
Deepanshu Sharwan

