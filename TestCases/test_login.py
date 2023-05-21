

import time

from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.LoginPage import LoginPage
from Utilites.Logger import loggenreter
from Utilites.readproperties import ReadConfig


# from selenium.webdriver.support import expected_conditions as EC

class Test_Login:
    Url = ReadConfig.geturl()
    Email = ReadConfig.getemail()
    Password = ReadConfig.getpassword()
    log = loggenreter.loggen()


    def test_login(self, setup):
        self.log.info("test_login is started")
        self.driver = setup
        self.log.info("opening browser")
        self.lp = LoginPage(self.driver)
        self.driver.get(self.Url)
        self.log.info("go to url--->" + self.Url)
        self.lp.Enter_Email(self.Email)
        self.log.info("Entering Email" + self.Email)
        self.lp.Enter_Password(self.Password)
        self.log.info("Entering password" + self.Password)

        self.lp.Click_Login()
        self.log.info("Clicking Login")
        self.wait = WebDriverWait(self.driver, 10)

        if self.driver.title == "Dashboard / nopCommerce administration":
            self.log.info("Page_title--->" + self.driver.title)
            self.driver.save_screenshot("C:\\Users\\Jyoti\\PycharmProjects\\pytest_nopcommProject\\Screenshots\\nopcommpass_002.png")
            assert True
            self.log.info("test_login is Passed")
            self.lp.Click_Logout()
            self.log.info("click Logout button")
        else:
            self.driver.save_screenshot("C:\\Users\\Jyoti\\PycharmProjects\\pytest_nopcommProject\\Screenshots\\nopcommfail_002.png")
            assert False
            self.log.info("test_login is Failed")

            self.driver.close()
            self.log.info("test_login is Completed")
