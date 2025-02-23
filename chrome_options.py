import undetected_chromedriver as uc
from webdriver_manager.chrome import ChromeDriverManager

def chrome_options(profile_dir=None, headless=None):
    options = uc.ChromeOptions()
    if headless != 'y':
        options.add_argument("--headless=new")
        options.add_argument("--disable-gpu")
        options.add_argument("--remote-allow-origins=*")
    options.add_argument(f"--user-data-dir={profile_dir}")
    options.add_argument("--allow-pre-commit-input")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-background-networking")
    options.add_argument("--disable-client-side-phishing-detection")
    options.add_argument("--disable-default-apps")
    options.add_argument("--disable-hang-monitor")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-sync")
    options.add_argument('--disable-extensions')
    options.add_argument("--no-first-run")
    options.add_argument("--disable-web-security")
    options.add_argument("--no-service-autorun")
    options.add_argument("--password-store=basic")
    options.add_argument("--test-type=webdriver")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-gaia-services")
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--disable-plugins")
    options.add_argument('--disable-logging')
    options.add_argument("--disable-application-cache")
    options.add_argument("--disk-cache-size=0")
    driver = uc.Chrome(options=options, driver_executable_path=ChromeDriverManager().install())
    return driver