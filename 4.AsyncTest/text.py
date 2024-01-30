import requests
import logging
import time

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

TOTAL_NUMBER = 100
BASE_URL = 'https://static4.scrape.cuiqingcai.com/detail/5'

start_time = time.time()
for _ in range(1, TOTAL_NUMBER + 1):
    logging.info('Scraping %s', BASE_URL)
    response = requests.get(BASE_URL, timeout=10, verify=True)

end_time = time.time()
logging.info('Total time: %s seconds', end_time - start_time)


