# Open Web Scraper Python

A Python program designed to execute web scraping tasks using configurations exported from the [Open Web Scraper](https://openwebscraper.com) Chrome plugin.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Introduction

**Open Web Scraper Python** is a lightweight Python tool for running web scraping tasks using the settings from the Open Web Scraper Chrome plugin. This program reads a JSON settings file exported from the plugin and performs the scraping based on the specified configurations.

## Features

- **JSON-based Configuration:** Load and execute scraping tasks from JSON files.
- **Automated Scraping:** Automate data extraction tasks with minimal setup.
- **Customizable:** Easily modify scraping configurations without altering the code.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/open-web-scraper-python.git
   cd open-web-scraper-python
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Export your scraping settings from the Open Web Scraper Chrome plugin as a JSON file.

2. Run the Python script with the path to your JSON configuration file:
   ```bash
   python scraper.py path/to/your-settings.json
   ```

3. The scraped data will be saved in the format specified in your settings file (e.g., CSV, JSON).

## Configuration

The JSON settings file should follow the format exported from the Open Web Scraper Chrome plugin. Below is an example structure:

```json
{
  "startUrl": "https://example.com",
  "selectors": [
    {
      "id": "title",
      "type": "Text",
      "selector": "h1.title",
      "multiple": false
    },
    {
      "id": "links",
      "type": "Link",
      "selector": "a.link",
      "multiple": true
    }
  ],
  "pagination": {
    "type": "Click",
    "selector": "a.next"
  }
}
```

## Examples

Here are some example commands to get you started:

- Scraping a single page:
  ```bash
  python scraper.py settings/single_page.json
  ```

- Scraping with pagination:
  ```bash
  python scraper.py settings/paginated.json
  ```

## Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new feature branch (`git checkout -b feature/new-feature`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature/new-feature`).
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
