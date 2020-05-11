import unittest
from selenium.webdriver import Chrome
import sys
sys.path.append("C://Users//ravin//PycharmProjects//End to End Automation")
from Pages.Loginpage import loginpage
import HtmlTestRunner
from Pages.Profilepage import profilepage
from Pages.DelivaryPage import delivarypage
from BaseFile.TestBase import testbase

class delivarypagetcs(unittest.TestCase):

    def setUp(self):

        base = testbase()
        self.driver = base.launchpage()


    def test_TC_001(self):

        #tescase:user (pro) creat the delivary group of grocerytype
        login = loginpage(self.driver)
        self.profile = login.enter_login("priyankacontractor", "priyanka@123")
        #click on delivary group to launch the delivary group
        delivarypage=self.profile.clickonDelivaryGroup()
        delivarypage.clickonstartdelivarygroup()
        #create the grocery Delivary group
        delivarypage.createnewdelivary(2)

        #get group status

        status=delivarypage.getgroupstatus()
        if(status=="FORMING"):
            self.driver.execute_script("lambda-status=passed")
        else:
            self.driver.execute_script("lambda-status=failed")


    def test_TC_002(self):
       #login as the consumer and place the order

        login = loginpage(self.driver)
        self.profile = login.enter_login("ravikumar", "ravikumar@123")
        delivarypage=self.profile.clickonDelivaryGroup()
        delivarypage.selectstatus("Forming")
        #select the group name
        delivarypage.selectdelivaryitem("Asia Market Delivery on January 14th near Raleigh")
       #get total order

        orderbefore=delivarypage.gettotalorder()

        delivarypage.consumer_placeorder()
        delivarypage.consumer_enterorder()

        orderafter=int(delivarypage.gettotalorder())
        orderexpected=int(orderbefore)+1

        if(orderafter==orderexpected):
            self.driver.execute_script("lambda-status=passed")
        else:
            self.driver.execute_script("lambda-status=failed")


    def test_TC_003(self):
        #consumer edit the order
        login = loginpage(self.driver)
        self.profile = login.enter_login("ravikumar", "ravikumar@123")
        delivarypage=self.profile.clickonDelivaryGroup()
        #select group type
        delivarypage.selectgrouptype("My Groups")
        #select status
        delivarypage.selectstatus("Forming")
        #launch group page
        delivarypage.launchgroupitempage()

        #Edit order
        text=''' milk-1
bread-1
potato'''
        delivarypage.consumer_editorder(text)
        delivarypage.clickonordertab()
        ordertext=delivarypage.getordertext()

        if(ordertext==text):
            self.driver.execute_script("lambda-status=passed")
        else:
            self.driver.execute_script("lambda-status=failed")

    def test_TC004(self):

        #order status updated to "max orders reached" when maximum orders are placed

        #Taj Hotel Delivery near Morrisville
        login = loginpage(self.driver)
        self.profile = login.enter_login("jipriyaji@gmail.com", "priyanka@123")
        #prerequisite,group with name Taj Hotel Delivery near Morrisville created in TC001 already present with order limit=2

        delivarypage=self.profile.clickonDelivaryGroup()
        delivarypage.selectstatus("Forming")

        #select the group name
        delivarypage.selectdelivaryitem("Taj Hotel Delivery near Morrisville Delivery near Raleigh")
        delivarypage.consumer_placeorder()
        delivarypage.consumer_enterorder()
        #get the order status
        orderstatus=delivarypage.getorderstatus()

        if(orderstatus=="Max Orders Reached"):

            self.driver.execute_script("lambda-status=passed")
        else:
            self.driver.execute_script("lambda-status=failed")


    def test_TC005(self):

        #group owner should ne able to finalize the order
    #login as the group owner "Taj Hotel Delivery near Morrisville"

        login = loginpage(self.driver)
        self.profile = login.enter_login("priyankacontractor", "priyanka@123")

        #click on delivary group to launch the delivary group
        delivarypage=self.profile.clickonDelivaryGroup()

        delivarypage.selectgrouptype("My Groups")
        delivarypage.selectstatus("Forming")
        delivarypage.selectdelivaryitem("Taj Hotel Delivery near Morrisville Delivery near Raleigh")

        #click on finalize group button
        delivarypage.finalizeorder()
        groupstatus=delivarypage.getgroupstatus()

        if(groupstatus=="FINALIZED"):
            self.driver.execute_script("lambda-status=passed")
        else:
            self.driver.execute_script("lambda-status=failed")


    def test_TC006(self):

        #consumer should be able to leave the group
        #login as the consumer
        login = loginpage(self.driver)
        self.profile = login.enter_login("jipriyaji@gmail.com", "priyanka@123")

        delivarygroup=self.profile.clickonDelivaryGroup()
        delivarygroup.selectgrouptype("My Groups")
        delivarygroup.selectstatus("Forming")

        delivarygroup.launchgroupitempage()
        delivarygroup.clickonordertab()

        delivarygroup.consumer_leaveGroup()
        actual_text=delivarygroup.getMyOrderitemtext()

        if(actual_text=="order deleted"):
            self.driver.execute_script("lambda-status=passed")
        else:
            self.driver.execute_script("lambda-status=failed")


    def test_TC007(self):

        #groupowner close the group,crreated in TC001
        login = loginpage(self.driver)
        self.profile = login.enter_login("priyankacontractor", "priyanka@123")
        #click on delivary group to launch the delivary group
        delivarygroup=self.profile.clickonDelivaryGroup()
        delivarygroup.selectgrouptype("My Groups")
        delivarygroup.selectstatus("Finalized")
        delivarygroup.selectdelivaryitem("Taj Hotel Delivery near Morrisville Delivery near Raleigh")
        delivarygroup.closedgroup()
        actual_status=delivarygroup.getgroupstatus()

        if(actual_status=="Closed"):
            self.driver.execute_script("lambda-status=passed")
        else:
            self.driver.execute_script("lambda-status=failed")




        #if  My Order




























    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\ravin\\PycharmProjects\\End to End Automation\\TestOutput"))










