# URL de base pour la pagination
BASE_URL = "https://www.avito.ma/fr/maroc/appartements/appartement_a_vendre"

# XPaths des éléments à scraper
XPATH_LINKS = "//a[@class ='sc-1jge648-0 eTbzNs']"
XPATH_TITLE = "//h1[@class='sc-1g3sn3w-12 jUtCZM']"
XPATH_PRICE = "//div[@class='sc-1g3sn3w-10 leGvyq']"
XPATH_LOCALISATION = "//span[@class='sc-1x0vz2r-0 iotEHk']"
XPATH_INFO = "//div[@class='sc-qmn92k-0 cjptpz']"
XPATH_BEDROOM = '//*[@id="__next"]/div/main/div/div[3]/div[1]/div[2]/div[1]/div[1]/div[2]/div[4]/div[1]/div[1]/div'
XPATH_BATHROOM = '//*[@id="__next"]/div/main/div/div[3]/div[1]/div[2]/div[1]/div[1]/div[2]/div[4]/div[1]/div[2]/div'
XPATH_SURFACE = '//*[@id="__next"]/div/main/div/div[3]/div[1]/div[2]/div[1]/div[1]/div[2]/div[4]/div[1]/div[3]/div'
XPATH_EQUIPEMENT = "//div[@class='sc-1g3sn3w-15 evEiLa']"

# Autres constantes
MAX_PAGES = 2  # Par exemple, pour limiter le nombre de pages
WAIT_TIME = 2  # Temps d'attente pour le chargement des pages
TIMEOUT = 10   # Délai d'attente pour les éléments