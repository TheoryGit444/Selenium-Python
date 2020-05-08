import unittest
from selenium.webdriver import Chrome
import sys

sys.path.append("C://Users//ravin//PycharmProjects//End to End Automation")
from Pages.Loginpage import loginpage
import HtmlTestRunner
from Utility import readconfig


class logintest(unittest.TestCase):

    def setUp(self):
        self.path = readconfig.readconfig("Section1", "Path")
        self.url = readconfig.readconfig("Section1", "URL")
        self.driver = Chrome(executable_path=self.path)
        self.driver.maximize_window()
        self.driver.get(self.url)
        self.driver.set_page_load_timeout(20)
        self.driver.implicitly_wait(10)

    def test_loginconsumer_UI002(self):
        driver = self.driver
        login = loginpage(driver)
        profile = login.enter_login("ravikumar", "ravikumar@123")

        #login.enter_login("ravikumar","ravikumar@123")
        title = login.get_title()
        self.assertEqual(title, "Welcome to Zuudoo' - Welcome back to Zuudoo! ", "title verification failed")

    def test_loginpro_UI002(self):
        driver = self.driver
        login = loginpage(driver)
        login.enter_login(readconfig.readconfig("Userdata", "pro"), readconfig.readconfig("Userdata", "pro_password"))
        title = login.get_title()
        self.assertEqual(title, "Welcome to Zuudoo' - Welcome back to Zuudoo! ", "title verification failed")

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\ravin\\PycharmProjects\\End to End Automation\\TestOutput"))
