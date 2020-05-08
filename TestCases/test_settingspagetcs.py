import unittest
from selenium.webdriver import Chrome
import sys
sys.path.append("C://Users//ravin//PycharmProjects//End to End Automation")
from Pages.Loginpage import loginpage
import HtmlTestRunner
from Utility.readconfig import readconfig
from Pages.Profilepage import profilepage
from Pages.SettingsPage import settingspage
from BaseFile.TestBase import testbase

class settingpagetest(unittest.TestCase):

    def setUp(self):

        base=testbase()
        self.driver=base.launchpage()

        username=base.getuser()
        password=base.getuserpassword()

        #launching profilepage

        login=loginpage(self.driver)
        profile=login.enter_login(username,password)

        self.settingpage=profile.settingClick()


    def test_editsettingpage_UI007(self):

        self.settingpage.editSetting("priyanka","consumer","PRIYANKA")

        list=self.settingpage.getSettingInfo()

        self.buisnessname=list[0].text
        name=list[3].text


        if (self.buisnessname=="PRIYANKA") and (name, "priyanka consumer"):
            self.driver.execute_script("sauce:job-result=passed")
        else:
            self.driver.execute_script("sauce:job-result=failed")

    def tearDown(self):

        self.driver.quit()














if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\ravin\\PycharmProjects\\End to End Automation\\TestOutput"))