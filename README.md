# AutomationBrowser
Selenium Chrome Automation Tool

## Overview
This tool automates web interactions using Selenium with the Chrome browser. It leverages `undetected-chromedriver` to bypass bot detection mechanisms and ensures compatibility with the latest Chrome versions.

## Features
- Automates web interactions using Chrome.
- Bypasses bot detection with `undetected-chromedriver`.
- Uses `webdriver-manager` for automatic ChromeDriver management.
- Simple setup and easy-to-use interface cmd with run program from file run.bat.

## Installation
To use this tool, ensure you have Python installed (recommended version: 3.8+). Then, install the required dependencies:
```bash
pip install setuptools
pip install selenium
pip install webdriver-manager
pip install undetected-chromedriver

## Notes
- `undetected-chromedriver` helps in avoiding bot detection on sites.
- `webdriver-manager` automatically manages the correct ChromeDriver version.
- Use `--headless` mode if running on a server without a GUI.

## License
This project is licensed under the MIT License. Feel free to contribute and improve the tool!
