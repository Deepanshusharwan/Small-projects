# Image to ASCII Converter

This script converts an image file into ASCII art and saves it to a text file.

## Description

The script takes an image as input and converts each pixel into an ASCII character based on its brightness. The resulting ASCII art is then saved to a specified output file. The user can also choose to downscale the image for a more compact ASCII representation.

## Dependencies

The script requires the following Python library:

*   **Pillow**: A powerful image processing library.

You can install the dependencies using the following command:

```bash
pip install -r requirements.txt
```

## Usage

You can run the script in two ways:

### 1. Interactive Mode

Run the script without any arguments:

```bash
python main.py
```

The script will prompt you for the following information:

*   The path to the input image.
*   The name of the output file (defaults to `ascii_image.txt`).
*   The downscale factor (optional, defaults to 1).

### 2. Command-Line Arguments

You can also provide the necessary information as command-line arguments:

```bash
python main.py <image_path> [output_name] [downscale_factor]
```

*   `<image_path>`: The path to the input image (required).
*   `[output_name]`: The name of the output file (optional, defaults to `ascii_image.txt`).
*   `[downscale_factor]`: The downscale factor (optional, defaults to 1).

## Examples

### Interactive Mode

```bash
$ python main.py
The image you want to input (path): image.jpeg
Save output as? (for default) ascii_output.txt
if you want to downscale (leave blank otherwise) 2
```

### Command-Line Arguments

```bash
# Basic usage
python main.py image.jpeg

# With output name
python main.py image.jpeg ascii_art.txt

# With output name and downscale factor
python main.py image.jpeg ascii_art.txt 4
```
