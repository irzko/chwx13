import time
from selenium.webdriver import EdgeOptions, Edge
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

url_runner = [
    'https://replit.com/@tmkha/JollyUnrulyWebpages',
    'https://replit.com/@tmkha/RotatingSardonicWearables',
    'https://replit.com/@tmkha/SlategrayAmbitiousDaemon',
    'https://replit.com/@tmkha/AbleThinGeeklog',
    'https://replit.com/@tmkha/FaroffDelayedDevices',
]


def init_webdriver(profile='runner'):
    profile_path = os.path.expanduser(r"~/AppData/Local/Microsoft/Edge/User Data/{0}".format(profile))
    options = EdgeOptions()
    prefs = {"profile.managed_default_content_settings.images": 2}
    options.add_experimental_option("prefs", prefs)
    options.use_chromium = True
    options.add_argument(
            "user-data-dir=" + profile_path
        )
    return Edge(options=options)

driver = init_webdriver()

i = 0
while True:
    print("Starting runner {0}".format(url_runner[i]))
    driver.get(url_runner[i])
    WebDriverWait(driver, 5*60).until(EC.visibility_of_element_located((By.CLASS_NAME, 'css-1kvwu98')))
    driver.find_elements(By.CLASS_NAME, "css-1kvwu98")[0].click()
    print('Running...')
    WebDriverWait(driver, 5*60).until(EC.visibility_of_element_located((By.CLASS_NAME, 'css-1kvwu98')))
    print('Done!')
    if i == len(url_runner) - 1:
        i = 0
    else: 
        i += 1