
# Payment Receipt Maker and Data Miner

This repository contains two Python scripts designed for specific purposes:

1. **Payment Receipt Maker**: Generates a PDF receipt for payment transactions.
2. **Data Miner**: Scrapes data from websites and saves it in an Excel file.

---

## Payment Receipt Maker

### Description
This script creates a detailed payment receipt in PDF format using the `reportlab` library. The receipt includes details such as the transaction ID, date, name, payment mode, and taxes.

### Features
- Generates a unique transaction ID.
- Computes and displays tax (18% GST).
- Saves the receipt as a PDF.
- Customizes user inputs like name and amount.

### How to Use
1. Run the script.
2. Enter the user’s name and payment amount when prompted.
3. The receipt will be saved as `Receipt.pdf` in the `CBT-CIP/` directory.

---

## Data Miner

### Description
This script extracts specific information from websites using the `Playwright` library and saves it into an Excel file. It's ideal for scraping data such as product names and prices from e-commerce platforms.

### Features
- Scrapes data based on provided CSS class names.
- Automatically waits for elements to load.
- Saves the extracted data in an Excel file.
- Includes the domain name in the saved file for better organization.

### How to Use
1. Define the URL and the CSS class names of elements you want to scrape in the `urls` dictionary.
2. Run the script.
3. The scraped data will be saved in the `CBT-CIP/` directory as an Excel file named after the website domain.

### Example
For the URL `https://www.amazon.in`, the script extracts product titles and prices using the CSS class names `s-title-instructions-style` and `a-price-whole`.

---

## Prerequisites

### Libraries Required
- `reportlab` for PDF generation.
- `playwright` for web scraping.
- `pandas` for data manipulation.
- `urllib.parse` for URL parsing.

### Installation
1. Install Python 3.x.
2. Install the required libraries:
   ```bash
   pip install reportlab playwright pandas
   ```
3. Install Playwright browsers:
   ```bash
   playwright install
   ```

---

## Directory Structure
```
CBT-CIP/
  |-- Receipt.pdf            # Output receipt file
  |-- <domain>.xlsx          # Output Excel file with scraped data

scripts/
  |-- receipt_maker.py       # Script for generating receipts
  |-- data_miner.py          # Script for data mining
```

---

## Usage
- Place the scripts in the `scripts/` directory.
- Ensure the `CBT-CIP/` directory exists or create it.
- Run the desired script and follow the prompts or configurations.

---

## Notes
- Modify the `urls` dictionary in `data_miner.py` to scrape data from different websites.
- Ensure that the specified CSS class names match the elements on the target webpage.

---

## License
This repository is available under the MIT License. Feel free to modify and distribute.

---

## Contributions
Contributions are welcome! Feel free to submit a pull request or raise an issue for enhancements or bug fixes.

---

## Author
Abhas Ganguli  
- Email: abhasganguli2003@gmail.com  
- LinkedIn: [linkedin.com/in/abhasganguli](https://linkedin.com/in/abhasganguli)  

A passionate developer with interests in Python and Software Development. Currently exploring AI, machine learning, and ethical hacking.
