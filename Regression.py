from tests import registration
import time

#--------------------------------------Registration Process Starts Here--------------------------------------------

reg = registration.Registration()


#open the registration page
reg.open_url()
time.sleep(5)

#accept cookies
reg.accept_cookies()

#fill the Personal Information
reg.first_name()
reg.last_name()
time.sleep(2)

#fill the Sign-in Information
reg.email()
reg.password()
time.sleep(2)

reg.createaccount()

time.sleep(5)

reg.check_account_page()

#--------------------------------------Registration Process Stops Here--------------------------------------------

#--------------------------------------Login Process Starts Here---------------------------------------------------
from tests import login

log = login.Login()

#open login page
log.open_url()
time.sleep(5)

#accept cookies
log.accept_cookies()

#fills email and password
log.email()
log.password()

log.submit()

#--------------------------------------Login Process Stops Here---------------------------------------------------