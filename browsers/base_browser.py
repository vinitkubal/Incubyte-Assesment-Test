
from selenium import webdriver

class chromeBrowser:
    def chrome_browser(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("prefs", {"profile.block_third_party_cookies": False})
        driver = webdriver.Chrome(executable_path=r'C:\Users\Vinit\Desktop\New folder\Incubyte\WebDriver\chromedriver.exe',chrome_options=chrome_options)
        return driver
