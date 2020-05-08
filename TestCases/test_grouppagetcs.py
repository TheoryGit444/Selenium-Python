import unittest
from selenium.webdriver import Chrome
import sys
sys.path.append("C://Users//ravin//PycharmProjects//End to End Automation")
from Pages.Loginpage import loginpage
import HtmlTestRunner
from Utility.readconfig import readconfig
from Pages.Profilepage import profilepage
from Pages.GroupPage import grouppage
from BaseFile.TestBase import testbase


class grouppagetest(unittest.TestCase):


    def setUp(self):

        base = testbase()
        self.driver = base.launchpage()

    @unittest.skip("skipping")
    def test_createnewgroup_UI005(self):

        self.owner='PRIYANKA'
        self.login = loginpage(self.driver)
        self.profile= self.login.enter_login("ravikumar", "ravikumar@123")
        self.driver.set_page_load_timeout(8)

        grouppage=self.login.startNewGroup()
        text="hi this priyanka ,I am doing cross browser testing"
        actual_status=grouppage.createNewGroup(text)

        if (actual_status=="FORMING"):
            self.driver.execute_script("sauce:job-result=passed")
        else:
            self.driver.execute_script("sauce:job-result=failed")

    @unittest.skip("skipping")
    def test_joinnewgroup_UI009(self):
        self.member="jacksonconsumer"
        self.login = loginpage(self.driver)
        self.profile= self.login.enter_login("jipriyaji@gmail.com", "priyanka@123")
        self.driver.set_page_load_timeout(8)

        self.profile.selectGrouptype("My Groups")
        self.profile.selectGroupStatus("Forming")

        grouppage= self.profile.launchGroupPage()
        grouppage.joinGroup()

        actual_status=self.profile.getgroupstatus()

        if (actual_status=="Joined"):
            self.driver.execute_script("sauce:job-result=passed")
            print("test is passed")
        else:
            self.driver.execute_script("sauce:job-result=failed")
            print("test is failed")

    def test_verifyownermemeberinfo_UI009(self):

        self.login = loginpage(self.driver)
        self.profile= self.login.enter_login("jipriyaji@gmail.com", "priyanka@123")
        self.driver.set_page_load_timeout(8)

        self.profile.selectGrouptype("My Groups")
        self.profile.selectGroupStatus("Forming")

        grouppage= self.profile.launchGroupPage()
        actual_owner=grouppage.getownerinfo()
        actual_memeber=grouppage.getmemberinfo()

        if(actual_owner==self.owner and actual_memeber==self.member):

            self.driver.execute_script("sauce:job-result=passed")
            print("test is passed: "+actual_owner+"  "+actual_memeber)
        else:
            self.driver.execute_script("sauce:job-result=failed")
            print("test is failed")
            print("test is passed: " + actual_owner + "  " + actual_memeber)

    def test_pro_making_offer(self):
        self.login = loginpage(self.driver)
        self.profile= self.login.enter_login("puday30", "priyanka@123")
        self.driver.set_page_load_timeout(8)

        self.profile.selectGrouptype("My Groups")
        self.profile.selectGroupStatus("Forming")

        grouppage=self.profile.launchGroupPage()

        offer=grouppage.makeAnOffer()
        proname=offer.submitOffer()
        actual_proname=proname.text

        if(actual_proname=="priyanka homer services"):

            self.driver.execute_script("sauce:job-result=passed")

        else:
            self.driver.execute_script("sauce:job-result=failed")
            print("test is pro making offer is failed")











    def test_xleavegroup(self):


        self.login = loginpage(self.driver)
        self.profile= self.login.enter_login("jipriyaji@gmail.com", "priyanka@123")
        self.driver.set_page_load_timeout(8)

        grouppage= self.profile.launchGroupPage()
        grouppage.leaveGroup()
        Actual_status=self.profile.getgroupstatus()

        if (Actual_status=="left group"):
            self.driver.execute_script("sauce:job-result=passed")
            print("test is passed")
        else:
            self.driver.execute_script("sauce:job-result=failed")
            print("test is failed")


    def test_verifyinviteemail(self):


     def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\ravin\\PycharmProjects\\End to End Automation\\TestOutput"))

