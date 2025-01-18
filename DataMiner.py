from playwright.sync_api import sync_playwright
import pandas as pd
from urllib.parse import urlparse

def scrape_website(url, classNames):
    extractedData = {}
    with sync_playwright() as p:
        browser = p.chromium.launch(headless = True)
        page = browser.new_page()
        page.goto(url)

        for className in classNames:
            page.wait_for_selector(f".{className}")
            element = page.locator(f".{className}").all_text_contents()
            extractedData[className] = element
        
        df = pd.DataFrame(extractedData)
        domain = urlparse(url).netloc.replace('www.', '').split('.')[0]
        df.to_excel(f"CBT-CIP/{domain}.xlsx", index=False)
        print(f"Extracted data saved to {domain}.xlsx")
        
#urls={"url" : [className1, className2, ....] }
urls = {
    "https://www.amazon.in/s?k=monitors&crid=1J8T4LARJ6NOE&sprefix=monitors%2Caps%2C285&ref=nb_sb_noss_1" : ["s-title-instructions-style", "a-price-whole"]


}

for url, classlist in urls.items():
    scrape_website(url,classlist)
