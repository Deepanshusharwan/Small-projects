# YouTube-Vid-Downloader

This project is a Python application that requires setting up a virtual environment and installing dependencies before running the main application.

## Prerequisites

Make sure you have the following installed on your system:

- Python 3.x
- `pip` (Python's package installer)
- `uv` (Python dependency manager)

You can install `uv` using the following command:

```bash
pip install uv
```

## Setting Up the Project

To set up the project environment and install dependencies, follow these steps:

### 1. Initial Setup (`firstrun.sh`)

Run the `firstrun.sh` script to initialize the virtual environment and install dependencies. This is typically done only once when you first clone the repository or if the environment needs to be set up again.

```bash
./firstrun.sh
```

**`firstrun.sh` script breakdown:**

- Installs `uv` if it's not installed.
- Creates a virtual environment using `uv`.
- Installs project dependencies as listed in the `pyproject.toml`.
- Runs the Python application (`app/main.py`).

This script will set up everything you need and prepare the environment.

### 2. Running the Application (`run.sh`)

Once the environment is set up, you can run the application using the `run.sh` script:

```bash
./run.sh
```

**NOTE:** when running the script in a new terminal you may need to run the 'run.sh' script twice to run the program the first time in any new terminal

**`run.sh` script breakdown:**

- Activates the virtual environment using `pipenv shell`.
- Installs any missing dependencies using `pipenv install`.
- Runs the main Python application (`app/main.py`).

### 3. Additional Notes

- **If you are using linux then make sure that you have downloaded the tk module **

```sudo pacman -S tk #use this to download the tk module in arch linux

```

- Ensure that the `Pipfile` and `app/main.py` are in place and contain the correct dependencies and code for the project to work as expected.
- If you encounter any issues with dependencies, try running `pipenv install` manually to update them.

## Project Structure

```

your-project/
├── app/
│ └── main.py # Main Python script
├── Pipfile # pipenv dependencies file
├── Pipfile.lock # pipenv lock file (auto-generated)
├── firstrun.sh # Script to set up environment
└── run.sh # Script to run the application

```

## Troubleshooting

- **Issue: `pipenv shell` not activating correctly**

  - Ensure `pipenv` is installed correctly: `pip install pipenv`.
  - Try re-running `firstrun.sh` to ensure the environment is created correctly.

- **Issue: Missing dependencies**

  - If dependencies are missing, run `pipenv install` manually to ensure everything is installed.

```

### Key Points:

1. **`firstrun.sh`**: Used for initial setup and environment creation.
2. **`run.sh`**: Used to run the application once the environment is set up.
3. **Dependencies**: Managed using `pipenv`.

```

```

```
