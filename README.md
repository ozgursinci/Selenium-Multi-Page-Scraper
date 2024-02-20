
# Project Name: Threading with selenium

This project uses Selenium and undetected_chromedriver to scrape product details listed on a specific website. It leverages Python's `ThreadPoolExecutor` class to process multiple links concurrently.

## Features

- **Dynamic Content Management:** Manage dynamically loaded content with Selenium and undetected_chromedriver.
- **Multi-Page Support:** Ability to work on multiple links loaded from a JSON file simultaneously.
- **Product Detail Extraction:** Access and extract the URL information of the first five listed products' detail pages.

## Installation

1. **Python Installation:** Python is required to run this project. Download and install the latest version from [Python's official website](https://www.python.org/downloads/).
2. **Dependencies Installation:**
   ```bash
   pip install selenium undetected-chromedriver
   ```
3. **WebDriver Configuration:** The project uses ChromeDriver. Download the appropriate version for your OS from [ChromeDriver's official website](https://sites.google.com/a/chromium.org/chromedriver/) and place it in the specified path in the project.

## Usage

1. **Adding Links to the JSON File:** Add the URLs of the pages you want to scrape to the `links.json` file.
   ```json
   {
     "links": [
       "http://example.com/page1",
       "http://example.com/page2"
     ]
   }
   ```
2. **Running the Project File:** Open a terminal or command prompt in the project folder and run the following command:
   ```bash
   python <file_name>.py
   ```
   Note: Replace `<file_name>` with the name of your Python file.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
