import unittest
from selenium.webdriver import Chrome
import sys
sys.path.append("C://Users//ravin//PycharmProjects//End to End Automation")
from Pages.Loginpage import loginpage
import HtmlTestRunner
from Utility.readconfig import readconfig
from Pages.Profilepage import profilepage
from BaseFile.TestBase import testbase
from Utility import readconfig

import time
from pynput.keyboard import Controller,Key
import logging

class profiletest(unittest.TestCase):

    def setUp(self):

        base = testbase()
        self.driver = base.launchpage()

        #username = base.getuser()
        #password = base.getuserpassword()

        #login = loginpage(self.driver)
        #self.profile = login.enter_login(username, password)
    def test_uploadprofilephoto_UI004(self):

        login = loginpage(self.driver)
        self.profile = login.enter_login("ravikumar", "ravikumar@123")
        #click on profile image and edit button
        self.profile.profileclick()

        #download image on new tab
        self.profile.opennewtab()
        self.profile.uploadProfilePhoto()# currently this is incomplete as phtot is not loaded beacuse cannot opy past from the keyboard to remote browser

    @unittest.skip("skipping")
    def test_createprofile_consumer_UI003(self):

        login = loginpage(self.driver)
        self.profile = login.enter_login("ravikumar","ravikumar@123")
       #profile = profilepage(driver)
        self.profile.profileclick()
        self.profile.editButtonClick()

        #editing the description of the user profile
        testdatatext="hello this is priyanka doinf regression testing"

        actual_text=self.profile.editProfileDetails(testdatatext)

        #self.assertEqual(actual_text,testdatatext,"details edited are not matching")
        if(actual_text==testdatatext):
            self.assertEqual(actual_text, testdatatext)
            self.driver.execute_script("sauce:job-result=passed")
        else:
            self.driver.execute_script("sauce:job-result=failed")

    @unittest.skip("skipping")
    def test_createprofile_contractor_UI003(self):
       # driver = self.driver
        login = loginpage(self.driver)
        profile =login.enter_login("priyankacontractor","priyanka@123")
        # profile = profilepage(driver)
        profile.profileclick()
        profile.editButtonClick()

        # editing the description of the user profile
        testdatatext = "hello,I am service provider for Home Serivces from past 10 Years.I have good Man power to provide services even during crisis time"

        actual_text = profile.editProfileDetails(testdatatext)


        if (actual_text==testdatatext):
            self.assertEqual(actual_text,testdatatext)
            self.driver.execute_script("sauce:job-result=passed")
        else:
            self.driver.execute_script("sauce:job-result=failed")

        #self.assertEqual(actual_text, testdatatext, "details edited are not matching")

    @unittest.skip("skipping")
    def test_verifyUploadphoto_consumer(self):

        # driver = self.driver
        login = loginpage(self.driver)
        profile = login.enter_login("ravikumar", "ravikumar@123")
        # profile = profilepage(driver)
        profile.profileclick()
        profile.uploadProfilePhoto()
        isimageloaded= profile.getprofileimage()

        if (isimageloaded):
            assert isimageloaded
            self.driver.execute_script("sauce:job-result=passed")
        else:
            self.driver.execute_script("sauce:job-result=failed")


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\ravin\\PycharmProjects\\End to End Automation\\TestOutput"))