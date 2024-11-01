# main.py

from scraper import Scraping
from processor import stock_data
import constants

def main():
    lien = constants.BASE_URL # Exemple de lien
    data = Scraping(lien)  # Appelle la fonction de scraping
    df = stock_data(data)   # Traite et enregistre les données
    print("Scraping et enregistrement dans le fichier CSV terminés.")

if __name__ == "__main__":
    main()
