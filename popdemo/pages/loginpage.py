class Loginpage():

    def __init__(self, driver):
        self.driver = driver

        self.button_id = "pv-nav-sign-in"
        self.username_textbox_id = "ap_email"
        self.password_textbox_id = "ap_password"
        self.sighin_button_id= "signInSubmit"

    def click_button(self):
        self.driver.find_element_by_id(self.button_id).click()

    def enter_username(self, username):
        self.driver.find_element_by_id(self.username_textbox_id).clear()
        self.driver.find_element_by_id(self.username_textbox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

    def click_sigin(self):
        self.driver.find_element_by_id(self.sighin_button_id).click()
