from selenium.webdriver.common.keys import Keys


class Homepage():

    def __init__(self,driver):
        self.driver = driver

        self.search_link_id = "pv-search-nav"
        self.logout_out_id = "pv-nav-sign-out"
        self.dropdown_id = "nav-profiles-dropdown-label"

    def click_search(self,username):
        self.driver.find_element_by_id(self.search_link_id).clear()
        self.driver.find_element_by_id(self.search_link_id).send_keys(username)
        self.driver.find_element_by_id(self.search_link_id).send_keys(Keys.ENTER)

    def dropdown_click(self):
        self.driver.find_element_by_id(self.dropdown_id).click()

    def logout_click(self):
        self.driver.find_element_by_id("pv-nav-sign-out").click()