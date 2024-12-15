
from constant import registration
import random
import string
from selenium import webdriver

#driver = base_browser.chromeBrowser()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("prefs", {"profile.block_third_party_cookies": True})
driver = webdriver.Chrome(executable_path=r'C:\Users\Vinit\Desktop\New folder\Incubyte\WebDriver\chromedriver.exe',chrome_options=chrome_options)

def random_name_generator():
    res = ''.join(random.choices(string.ascii_letters,k=7))
    return res

class Registration:

    def open_url(self):
        driver.get(registration.url)

    def accept_cookies(self):
        try:
            driver.find_element_by_xpath(registration.appept_btn).click()
        except:
            print("Could not find the accept button")

    def first_name(self):
        f_name = random_name_generator()
        try:
            firstName = driver.find_element_by_xpath(registration.first_name)
            firstName.send_keys(f_name)
            print("First Name is"+" "+f_name)
        except:
            print("Error at First Name on Registration Page ")

    def last_name(self):
        try:
            l_name = random_name_generator()
            lastName = driver.find_element_by_xpath(registration.last_name)
            lastName.send_keys(l_name)
            print("Last Name is" + " " + l_name)
        except:
            print("Error at First Name on Registration Page ")

    def email(self):
        try:
            newemail = random_name_generator()+'@gmail.com'
            email = driver.find_element_by_xpath(registration.email)
            email.send_keys(newemail)
            print("Email is"+" "+newemail)
        except:
            print("Error at Email on Registration Page ")
    def password(self):
        try:
            newpassword="Demo@1234"
            password = driver.find_element_by_xpath(registration.password)
            password.send_keys(newpassword)
            confirnpassword = driver.find_element_by_xpath(registration.confirmpassword)
            confirnpassword.send_keys(newpassword)
            print("Password is "+newpassword)
        except:
            print("Error at Password on Registration Page ")

    def createaccount(self):
        try:
            driver.find_element_by_xpath(registration.createaccount).click()
            print("Entered")
        except:
            print("Error in account Creation")

    def check_account_page(self):
        try:
            my_title = driver.title
            if(my_title == 'My Account'):
                print("below are account details")
                details = driver.find_element_by_xpath('/html/body/div[3]/main/div[2]/div[1]/div[3]/div[2]/div').text
                print(details)
                driver.quit()
        except:
                print("Error at Account creation")