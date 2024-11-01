
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import constants  # Importer les constantes


def Scraping(lien):
    driver = webdriver.Chrome()
    annonce_data = []

    page = 1
    while page < constants.MAX_PAGES:
        driver.get(f'{lien}?o={page}')
        time.sleep(constants.WAIT_TIME)

        links = driver.find_elements(By.XPATH, constants.XPATH_LINKS)
        i = 0
        while i < len(links):
            links = driver.find_elements(By.XPATH, constants.XPATH_LINKS)
            link = links[i]
            url = link.get_attribute('href')
            driver.get(url)

            try:
                title = WebDriverWait(driver, constants.TIMEOUT).until(
                    EC.presence_of_element_located((By.XPATH, constants.XPATH_TITLE))
                )
                price = driver.find_element(By.XPATH, constants.XPATH_PRICE)
                localisation = driver.find_element(By.XPATH, constants.XPATH_LOCALISATION)
                info = driver.find_element(By.XPATH, constants.XPATH_INFO)

                try:
                    bedroom = driver.find_element(By.XPATH, constants.XPATH_BEDROOM).text or 'nan'
                    bathroom = driver.find_element(By.XPATH, constants.XPATH_BATHROOM).text or 'nan'
                    surface = driver.find_element(By.XPATH, constants.XPATH_SURFACE).text or 'nan'
                    equipement = driver.find_element(By.XPATH, constants.XPATH_EQUIPEMENT).text
                except:
                    equipement = 'nan'

                annonce_data.append({
                    'url': url,
                    'Title': title.text,
                    'info': info.text,
                    'Price': price.text,
                    'Localisation': localisation.text,
                    'Bedroom': bedroom,
                    'Bathroom': bathroom,
                    'surface': surface,
                    'Equipement': equipement
                })
            except Exception as e:
                print(f'Error in data {url}: {e}')
            driver.back()
            time.sleep(constants.WAIT_TIME)
            i += 1
        page += 1

    driver.quit()
    return annonce_data
