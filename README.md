# Small Projects Repository

This repository is a collection of various small projects, ranging from simple scripts to more complex applications. Each project is contained in its own directory with its own `README.md` file for detailed information.

---

### 🧴 `bottler_telegram_bot`
- **Purpose**: A Telegram bot that responds to user commands.
- **Functionality**: Appears to use the `telebot` (PyTelegramBotAPI) library.
- **Main Features**:
  - Responds to `/start` and `/help`.
  - Likely echoes or processes messages.
- **Note**: Useful for creating basic bot interactions.

---

### 🔠 `figlet`

- **Purpose**: A simple script to generate ASCII art using the `pyfiglet` library.
- **Functionality**: Takes user input and prints it as stylized ASCII text.
- **Use Case**: Fun command-line tool for decorative outputs.

---

### 💥 Fork Bomb (Dangerous)

⚠️ **WARNING**: Do not run this script on a live system.

**Function**: Repeatedly forks processes until the system crashes due to resource exhaustion.

**Code**: Implements an infinite loop with `os.fork()`.

**Use Case**: Educational purposes only, preferably in a virtual machine or sandbox.

---

### 🎞️ `gifmaker`

- **Purpose**: Converts image files into an animated GIF.
- **Functionality**:
  - Uses `Pillow` to read image files.
  - Compiles them into a looping GIF.
- **Main Options**:
  - Set duration, output name, etc.
- **Good For**: Quick automation of GIF creation from static images.

---

### 🎵 `music_downloader(playwright)`

- **Purpose**: A script to download music from websites using Playwright.
- **Functionality**: Automates browser interactions to search for and download music.
- **Note**: Requires Playwright and its browser dependencies.

---

### 🎤 `singer_music_lister`

- **Purpose**: Lists songs by a singer using web scraping.
- **Functionality**:
  - Takes a singer's name.
  - Scrapes song list from the web.
- **Use Case**: Music lovers or karaoke prep!

---

### 📈 `stock-portfolio-valuation-scraper`

- **Purpose**: A script to scrape stock prices and calculate portfolio valuation.
- **Functionality**:
  - Connects to financial websites to fetch real-time stock data.
  - Computes the current value of a user's stock portfolio.
- **Note**: Requires specific web scraping libraries and might need updates if website structures change.

---

### 🌳 `tree`

- **Purpose**: Replicates the UNIX `tree` command.
- **Functionality**:
  - Displays directory structure in a tree format.
  - Customizable depth and folder options.
- **Useful For**: File structure overviews, especially for large projects.

---

### 🔗 `url_shortner`

- **Purpose**: A URL shortener created using FastAPI.
- **Functionality**:
  - Provides an API to shorten long URLs.
  - Stores original and shortened URLs in a database.
- **Note**: Requires FastAPI and a database (e.g., SQLite).

---

### 🌐 `web_browser_simple`

- **Purpose**: A very simple web browser using Python.
- **Functionality**:
  - Takes the URL and HTTP request and outputs the response from the browser.
- **Educational Value**: Shows how browsers work under the hood.

---

### 🌍 `web_server_simple`

- **Purpose**: Basic HTTP web server.
- **Functionality**:
  - Uses `http.server` or similar to serve files.
  - Could be extended to serve dynamic content.
- **Use Case**: Local development, static site hosting.

---

### 🎬 `youtube-vid-downloader`

**Purpose**: A script to download YouTube videos.

- **Functionality**:
  - Downloads videos in MP4 format using `pytubefix`.
  - Provides a GUI for selecting the download location.
  - Displays a progress bar with `tqdm` for the download process.

- **Main Features**:
  - Prompts for a YouTube URL.
  - Allows the user to choose a download location via a file dialog.
  - Uses `on_progress_callback` and `on_complete_callback` to handle progress updates and completion.

**Note**: Requires `pytubefix`, `tkinter`, and `tqdm` libraries.

---

### 🎨 `image-to-ascii`

- **Purpose**: Converts an image file into ASCII art.
- **Functionality**: Takes an image, converts pixels to ASCII characters based on brightness, and saves the result to a text file. Supports optional image downscaling.
- **Dependencies**: `Pillow`.
- **Main Features**:
  - Interactive mode for guided input.
  - Command-line arguments for quick execution.
- **Use Case**: Generating creative text-based representations of images.
