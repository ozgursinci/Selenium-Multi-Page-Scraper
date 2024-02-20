from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
import json
from concurrent.futures import ThreadPoolExecutor

# Configure WebDriver settings
CHROME_DRIVER_PATH = "C:/Users/Asus/Desktop/WebScrabing/ChromeDriver/chromedriver.exe"
LOAD_TIMEOUT = 20

def open_link(link):
    """Lists products on a specific link and opens the details of the first five products."""
    options = webdriver.ChromeOptions()
    chrome = uc.Chrome(options=options, driver_executable_path=CHROME_DRIVER_PATH)
    chrome.get(link)
    WebDriverWait(chrome, LOAD_TIMEOUT).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
    
    # Operations to be performed after ChromeDriver has launched
    try:
        listing_items = WebDriverWait(chrome, LOAD_TIMEOUT).until(
            EC.presence_of_all_elements_located((By.XPATH, '//li[contains(@class, "listing-item")]'))
        )
        print(f"{link} - Total Number of Products: {len(listing_items)}")

        for item in listing_items[:5]: 
            action = webdriver.ActionChains(chrome)
            action.move_to_element(item).perform() 
            item.click()
            
            WebDriverWait(chrome, LOAD_TIMEOUT).until(EC.presence_of_element_located((By.CLASS_NAME, 'some-class-name-on-new-page')))
            print(f"Product Detail Page: {chrome.current_url}")
            chrome.back()
            WebDriverWait(chrome, LOAD_TIMEOUT).until(EC.presence_of_all_elements_located((By.XPATH, '//li[contains(@class, "listing-item")]')))
    finally:
        chrome.quit()

def load_links_from_json(file_path):
    """Loads links from a JSON file."""
    with open(file_path, "r") as file:
        data = json.load(file)
    return data['links']

def main():
    links = load_links_from_json("C:/Users/Asus/anaconda3/envs/Selenium/Sahibinden/linkler.json")
    with ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(open_link, links)

if __name__ == "__main__":
    main()
