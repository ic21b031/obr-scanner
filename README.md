# OBR Scanner Tool

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

## Description

A Python script that monitors a specified directory for file creation or modification events using the `watchdog` library.\
When events occur, it runs a script `run_local.py` and starts a scanner software specified by the `scanner_exe` environment variable.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Installation
- Python 3.x
- `watchdog` library: Install it using `pip install watchdog`

## Usage

1. Set up the environment:
   - Ensure you have Python installed.
   - Install the required Python packages by running:
     ```bash
     pip install watchdog
     ```

2. Set the `scanner_exe` environment variable:
   - Specify the path to the scanner software executable in the environment variable. For example:
     ```bash
     export scanner_exe=/path/to/scanner/executable
     ```

3. Run the script:
   ```bash
   python app.py
    ```

## Configuration
Modify the `watch_directory` variable in the script to specify the directory to monitor.
Adjust the language variable and the script command in the Handler class to fit your requirements.

## Notes
This script assumes a Unix-like environment.\
If your operating system is windows set up the environment variable accordingly.

## Contributing

If you would like to contribute to the project, provide guidelines for how others can do so. This may include information about submitting bug reports, feature requests, or code contributions.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- [AngelinaReader](https://github.com/IlyaOvodov/AngelinaReader)
