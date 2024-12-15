from constant import login
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("prefs", {"profile.block_third_party_cookies": True})
driver = webdriver.Chrome(executable_path=r'C:\Users\Vinit\Desktop\New folder\Incubyte\WebDriver\chromedriver.exe',chrome_options=chrome_options)



class Login:

    def open_url(self):
        driver.get(login.url)

    def accept_cookies(self):
        driver.find_element_by_xpath(login.accept_btn).click()

    def email(self):
        try:
            driver.find_element_by_xpath(login.email).send_keys(login.email_id)
            print("Email Entered : "+login.email_id)
        except:
            print("Error finding Email Textbox on Login Page")

    def password(self):
        try:
            driver.find_element_by_xpath(login.password).send_keys(login.pwd)
            print("Password Entered : "+login.pwd)
        except:
            print("Error finiding Password Textbox on Login Page")

    def submit(self):
        try:
            driver.find_element_by_xpath(login.sign_in).click()

            driver.quit()
        except:
            print("Cannot find Sign-in button")

