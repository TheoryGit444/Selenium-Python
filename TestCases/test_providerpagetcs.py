import unittest
from selenium.webdriver import Chrome
import sys
sys.path.append("C://Users//ravin//PycharmProjects//End to End Automation")
from Pages.Loginpage import loginpage
import HtmlTestRunner
from Utility.readconfig import readconfig
from Pages.Profilepage import profilepage
from Pages.GroupPage import grouppage
from Pages.ProviderPage import providerpage
from Pages.OfferPage import offerpage
from BaseFile.TestBase import testbase


class grouppagetest(unittest.TestCase):


    def setUp(self):

        base = testbase()
        self.driver = base.launchpage()

    def test_verifymessagesentbyconsumer_UI007(self):
        # login as group owner

        self.login = loginpage(self.driver)
        self.profile= self.login.enter_login("ravikumar", "ravikumar@123")
        self.driver.set_page_load_timeout(8)

        self.profile.selectGrouptype("My Groups")
        self.profile.selectGroupStatus("Forming")
        groupObjectnumber=self.profile.readGroupObjectWithOffer()

        # click on my groups---launch grouppage
        grouppage=self.profile.launchGroupWithObjectnumber(groupObjectnumber)
        # click on offer tab----launch offer tab section

        offer=grouppage.launchOfferSection()

        #launch providerpage
        propage=offer.getProviderPage("priyanka homer services")
        # click on message buttom-----launch message page
        propage.clickMessageButton()
        message_to_pro="hello this is Selenium python automation testing"
        propage.WriteMessage(message_to_pro)
        propage.sendMessage()
        actual_text=propage.getRecentMessageSent()

        if(actual_text==message_to_pro):
            self.messagesenttopro=actual_text
            self.driver.execute_script("sauce:job-result=passed")
            print(actual_text+ " Was sent")
        else:
            self.driver.execute_script("sauce:job-result=failed")
            print((message_to_pro+ "was sent but receivedthe message "+ actual_text))

    def test_verrifymessagereceivedbypro_UI015(self):

        messagereceived=self.messagesenttopro

        #login as pro

        self.login = loginpage(self.driver)
        self.profile= self.login.enter_login("priyankacontractor", "priyanka@123")
        self.driver.set_page_load_timeout(8)
    #click on message envelope
        self.profile.profileclick()
        actual_message= self.profile.getRecentMessageReceived()

        if(actual_message==messagereceived):

            self.driver.execute_script("sauce:job-result=passed")
            print(actual_message+" is received")

        else:
            self.driver.execute_script("sauce:job-result=failed")
            print(messagereceived+" is sent by the user and message received by the pro is "+actual_message)

    def test_verifyreviewsubmittedbyconsumer_UI007(self):

        self.login = loginpage(self.driver)
        self.profile= self.login.enter_login("ravikumar", "ravikumar@123")
        self.driver.set_page_load_timeout(8)

        self.profile.selectGrouptype("My Groups")
        self.profile.selectGroupStatus("Forming")
        groupObjectnumber=self.profile.readGroupObjectWithOffer()

        # click on my groups---launch grouppage
        grouppage=self.profile.launchGroupWithObjectnumber(groupObjectnumber)

        offer=grouppage.launchOfferSection()
        propage=offer.getProviderPage("priyanka homer services")

        propage.clickOnReviewButton()
        propage.WriteMessage("This is my review--Priyanka")
        propage.clickOnReviewTab()
        reviewelement=propage.verifyRecentReview()

        if(reviewelement.is_displayed()):

            self.driver.execute_script("sauce:job-result=passed")
        else:
            self.driver.execute_script("sauce:job-result=failed")





















