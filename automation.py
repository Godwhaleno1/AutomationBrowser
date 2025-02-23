from pathlib import Path
import time
import uuid
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from chrome_options import chrome_options

def random_profile():
    home = Path(__file__).parent
    profile_dir = home / 'profile' / f"profile_{str(uuid.uuid4())}"
    profile_dir.mkdir(parents=True, exist_ok=True)
    return profile_dir

def wait_for_element(driver, locator_type, locator_value, action=None, input_value=None, typing_delay=0.1, timeout=60):
        element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((locator_type, locator_value))
        )
        if action == "click":
            element.click()
        elif action == "send_keys" and input_value is not None:
            for char in input_value:
                element.send_keys(char)
                time.sleep(typing_delay)
        elif action == "get_data":
            return element.text
        elif action == "chose_list":
            input_value = str(input_value).lstrip('0')
            select = Select(element)
            select.select_by_value(input_value)
            return element
        return element
                        
def automate_browser(headless = None):
    try:
        profile_dir = random_profile()
        driver = chrome_options(profile_dir, headless)
        if headless == 'y':
            driver.set_window_size(1000, 1000)     
        #===========================================================================edit here===========================================================================
        driver.get('https://bot.sannysoft.com/')
        time.sleep(60)
        #======================================================================================================================================================        
        driver.quit()
        return
    except Exception as e:
        driver.quit()
        return