import unittest
from selenium import webdriver
import time

from popdemo.pages.loginpage import Loginpage
from popdemo.pages.homepage import Homepage

from selenium.webdriver.common.keys import Keys



class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path="C://Users//dell//Downloads//chromedriver_win32//chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_LoginValid(self):
        driver = self.driver
        driver.get("https://www.primevideo.com/")
        login = Loginpage(driver)
        login.click_button()
        login.enter_username("7895483510")
        login.enter_password("shubhpooh1994")
        login.click_sigin()

        #self.driver.find_element_by_id("pv-nav-sign-in").click()
        #self.driver.find_element_by_id("ap_email").send_keys("7895483510")
        #self.driver.find_element_by_id("ap_password").send_keys("shubhpooh1994")
        #self.driver.find_element_by_id("signInSubmit").click()

    def test_searchbar(self):
        driver = self.driver
        homepage = Homepage(driver)
        homepage.click_search("movies")
        homepage.click_search("justice league")
        homepage.dropdown_click()
        homepage.logout_click()
        #self.driver.implicitly_wait(10)
        #self.driver.find_element_by_id("pv-search-nav").clear()
        #self.driver.find_element_by_id("pv-search-nav").send_keys("MOVIES")
        #self.driver.find_element_by_id("pv-search-nav").send_keys(Keys.ENTER)

        time.sleep(2)
        #self.driver.find_element_by_id("pv-search-nav").clear()
        #self.driver.find_element_by_id("pv-search-nav").send_keys("JUSTICE LEAGUE")
        #self.driver.find_element_by_id("pv-search-nav").send_keys(Keys.ENTER)
        #time.sleep(2)


        #self.driver.find_element_by_id("nav-profiles-dropdown-label").click()
        time.sleep(2)
        #self.driver.find_element_by_id("pv-nav-sign-out").click()
        #time.sleep(2)

    @classmethod
    def tearDownClass(self):
        time.sleep(5)
        self.driver.close()
        self.driver.quit()
        print("complete")


if __name__ == '__main__':
    unittest.main()