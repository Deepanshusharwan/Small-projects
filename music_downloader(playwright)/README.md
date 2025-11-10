# Song Downloader Script

This Python script allows you to download songs from a specified website (Tidal) using Playwright and Google Chrome. You can either provide the song name directly or use a text file containing song names to download multiple tracks.

## Requirements

Before running the script, you must have the following installed:

- **Python 3.x** (Preferably Python 3.7 or above)
- **Google Chrome**: The script uses Chromium (Google Chrome) via Playwright. Make sure you have Google Chrome installed on your system. If not, download it from [Google Chrome's official site](https://www.google.com/chrome/).
- **Playwright**: The script utilizes Playwright, a Node.js-based browser automation library, to interact with the website and download the songs.

### Installation Steps

1. **Install Python Dependencies**:
   - First, ensure you have Python installed. You can check by running `python --version` in the terminal.
   - Install Playwright and its dependencies by running the following command:

     ```bash
     pip install playwright
     python -m playwright install
     ```

2. **Download Google Chrome**:
   - If you do not have Google Chrome installed, download and install it from [here](https://www.google.com/chrome/).
   - The script requires Google Chrome to work properly, as it launches the Chromium browser during execution.

3. **Clone the Repository** (or place the script in a folder of your choice).

---

## Usage

### Command Line

You can run the script from the command line by specifying the song name or a file containing a list of songs:

#### Option 1: Download a Single Song

You can run the script and provide a song name interactively (the script will prompt you for it):

```bash
python download_song.py
```

#### Option 2: Download Songs from a File

You can create a text file (e.g., songs.txt) with a list of song names (one per line). Then, you can provide the path to this file:

```bash
python download_song.py path/to/songs.txt
```

Note: Each song name in the text file should be on a separate line. The script will read through the file, download each song, and save it to your default downloads folder.

Script Behavior

- The script will open a Chromium browser window (not headless) and navigate to the website to search and download the song.

* The song will be saved in your default Downloads folder.

* If a song name or file is invalid, the script will notify you with an error message.

## Troubleshooting

- "File Not Found" Error: Make sure the file path to the text file is correct if you're using a text file.

* Missing Google Chrome: If you get errors related to Chrome not being found, ensure Google Chrome is installed on your system.

## License

This script is released under the MIT License.

## Contributing

Feel free to fork the repository, submit issues, and send pull requests. Contributions are welcome!


### Explanation:

- **Requirements**: Added the note about needing Google Chrome.
- **Installation**: Instructions for installing Playwright and Google Chrome.
- **Usage**: Clear instructions on how to run the script either interactively or with a file containing multiple song names.
- **Troubleshooting**: Common issues like file not found or missing Google Chrome are addressed.
- **License and Contributing**: Basic sections if you want to open-source the project. You can modify or add your preferred license.

Let me know if you need anything else!
