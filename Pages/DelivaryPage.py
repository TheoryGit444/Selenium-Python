from Utility.Locators import locators
from selenium.common.exceptions import NoSuchElementException



class delivarypage():

    def __init__(self,driver,obj):

        self.driver=driver
        self.obj=obj

        self.delivarygroup=locators.delivary_group
        self.reuseradio=locators.reuseradiobutton_id
        self.nextbutton=locators.nextbtn_xpath
        self.grocery=locators.grocerydelivarybutton
        self.memberlimit=locators.memeberlimit_name
        self.finishbutton=locators.finishbutton
        self.placeanorder=locators.placeanorderbutton
        self.description=locators.textarea_id
        self.save=locators.submit_css
        self.editorder=locators.editorder_xpath
        self.leavegroup=locators.leavegroup_xpath
        self.leave=locators.submit_css
        self.finalizeorders=locators.finalizeorders
        self.closegroup=locators.closegroup
        self.finalizeconfirm=locators.submit_css
        self.ordertab=locators.orderstab
        self.startnewgroup=locators.startnewgroup

    def clickonstartdelivarygroup(self):
         self.obj.sleep(3)
         startnewgroup=self.driver.find_element_by_xpath(self.startnewgroup)
         self.obj.clickOnButton(startnewgroup,"Start New Group")
         self.obj.pageload(5)

    def clickonordertab(self):

        orders=self.driver.find_element_by_xpath(self.ordertab)
        self.obj.clickOnButton(orders,"Order Tab")

    def selectstatus(self,type):

        if (type=="Forming"):
            status=self.driver.find_element_by_xpath("//app-group-status-filters/div/a[2]")
            self.obj.clickOnButton(status,"Status")
         #click on finalized
        else:
            status=self.driver.find_element_by_xpath("//app-group-status-filters/div/a[3]")
            self.obj.clickOnButton(status,"Staus")

    def selectgrouptype(self,grouptype):

        if(grouptype=="My Groups"):
            group=self.driver.find_element_by_xpath("//app-group-mygroups-filters/div/a[2]")
            self.obj.clickOnButton(group,"MyGroups")

        else:
            group=self.driver.find_element_by_xpath("//app-group-mygroups-filters/div/a[3]")
            self.obj.clickOnButton(group,"Saved")

    def selectdelivaryitem(self,itemname):

        #xpath=//app-deliveries-list//app-deliveries-item[1]//h1
        xpathbefore = "//app-deliveries-item["
        xpathafter = "]//app-group-item-container//h1"
        list=self.driver.find_elements_by_xpath("//app-deliveries-list//app-deliveries-item")
       # totalitem=len(list)

        i = 1
        for ele in list:
            xpath = xpathbefore + str(i) + xpathafter
            print(xpath)
            item = self.driver.find_element_by_xpath(xpath)
            groupname = self.driver.find_element_by_xpath(xpath).text
            print(groupname)

            if (groupname == itemname):
                item.click()
                break
            i = i + 1

    def launchgroupitempage(self):

        self.obj.sleep(3)

        item=self.driver.find_element_by_xpath("//app-deliveries-list//app-deliveries-item[1]//h1")
        self.obj.clickOnButton(item,"GroupItem")

    def getordertext(self):

        ordertext=self.driver.find_element_by_xpath("//app-delivery-member-item-body//app-description/span").text
        return ordertext


    def gettotalorder(self):

        ordertext=self.driver.find_element_by_xpath("//*[@class='group-details-header__nav']//ul[@role='navigation']/li[2]//span").text
        orderarr=ordertext.split(" ")
        ordernumber=max(orderarr[1])
        return ordernumber


    def createnewdelivary(self,maxorder):

        grocerygroup=self.driver.find_element_by_xpath(self.grocery)
        self.obj.clickOnButton(grocerygroup,"Grocery Group")
        nextbutton=self.driver.find_element_by_xpath(self.nextbutton)
        self.obj.clickOnButton(nextbutton,"Next Button")
        self.obj.clickOnButton(nextbutton, "Next Button")
        self.obj.clickOnButton(nextbutton, "Next Button")

        groupname=self.driver.find_element_by_id("buisness-name")
        self.obj.enterText(groupname,"Taj Hotel Delivery near Morrisville","Group name")
        self.obj.clickOnButton(nextbutton, "Next Button")
        memeberlimit=self.driver.find_element_by_name(self.memberlimit)
        self.obj.enterText(memeberlimit, str(maxorder), "Member Limit Text Box")
        self.obj.clickOnButton(nextbutton, "Next Button")
        self.obj.clickOnButton(nextbutton, "Next Button")
        self.obj.clickOnButton(nextbutton, "Next Button")

        orderdes=self.driver.find_element_by_id("member-description")
        self.obj.enterText(orderdes,'''milk
        bread
        potatao''',"Order Decription")

        finish=self.driver.find_element_by_xpath(self.finishbutton)
        self.obj.clickOnButton(finish,"finish button")






    def reuseExistedGroup(self,ordercount):

        #click on delivary group
        grocerygroup=self.driver.find_element_by_xpath(self.grocery)
        self.obj.clickOnButton(grocerygroup,"Grocery Group")
        nextbutton=self.driver.find_element_by_xpath(self.nextbutton)
        self.obj.clickOnButton(nextbutton,"Next Button")
        self.obj.clickOnButton(nextbutton, "Next Button")
        self.obj.clickOnButton(nextbutton, "Next Button")
        #click on reuse button
        reusebutton=self.driver.find_element_by_id(self.reuseradio)
        self.obj.clickOnButton(reusebutton,"Reuse RadioButton")
        #click on next button
        nextbutton=self.driver.find_element_by_xpath(self.nextbutton)
        self.obj.clickOnButton(nextbutton,"Next Button")
        # ,click on grocery delivary
        delivarybutton=self.driver.find_element_by_xpath(self.delivarygroup)
        self.obj.clickOnButton(delivarybutton,"Delivary")
        # ,click on next,click on next,click on next,click on next,click on next
        self.obj.clickOnButton(nextbutton,"Next Button")
        self.obj.clickOnButton(nextbutton,"Next Button")
        self.obj.clickOnButton(nextbutton,"Next Button")
        self.obj.clickOnButton(nextbutton,"Next Button")
        self.obj.clickOnButton(nextbutton,"Next Button")
        # ,enter memeber limit
        memeberlimit=self.driver.find_element_by_name(self.memberlimit)
        self.obj.enterText(memeberlimit, str(ordercount), "Member Limit Text Box")

        # ,click on next,click on next,click on next,
        self.obj.clickOnButton(nextbutton, "Next Button")
        self.obj.clickOnButton(nextbutton, "Next Button")
        self.obj.clickOnButton(nextbutton, "Next Button")

        finish=self.driver.find_element_by_xpath(self.finishbutton)
        self.obj.clickOnButton(finish,"finish button")
#click on finish

    def consumer_placeorder(self):

        placeanorderbutton=self.driver.find_element_by_xpath(self.placeanorder)
        self.obj.clickOnButton(placeanorderbutton,"Place an order")

    def consumer_enterorder(self):

        text="bread=1,milk=2,rice=1 packet"
        description=self.driver.find_element_by_id(self.description)
        self.obj.enterText(description,text,"Description")

        save=self.driver.find_element_by_css_selector(self.save)
        self.obj.clickOnButton(save,"Save Button")

    def consumer_editorder(self,text):

        editorder=self.driver.find_element_by_xpath(self.editorder)
        self.obj.clickOnButton(editorder,"EditOrder Button")


        #text="bread=1,milk=5,rice=1 packet,potato=3"
        description=self.driver.find_element_by_id(self.description)
        self.obj.enterText(description,text,"Description")

        save=self.driver.find_element_by_css_selector(self.save)
        self.obj.clickOnButton(save,"Save Button")




    def consumer_leaveGroup(self):

        leavegroup=self.driver.find_element_by_xpath(self.leavegroup)
        self.obj.clickOnButton(leavegroup,"Leave Group")

        leavebutton=self.driver.find_element_by_css_selector(self.leave)
        self.obj.clickOnButton(leavebutton,"Leave confirm")

    def getgroupstatus(self):

            groupstatus=self.driver.find_element_by_xpath("//app-group-status/div/div[1]").text
            return groupstatus

    def getorderstatus(self):

        orderstatus=self.driver.find_element_by_xpath("//app-group-status/div/div[2]").text
        return orderstatus

    def finalizeorder(self):

        finalizebutton=self.driver.find_element_by_xpath(self.finalizeorders)
        self.obj.clickOnButton(finalizebutton,"Finalize orders")

        submit=self.driver.find_element_by_css_selector(self.finalizeconfirm)
        self.obj.clickOnButton(submit,"Confirm finalize")

        #then get order status

    def closedgroup(self):

        closegroupbutton=self.driver.find_element_by_xpath(self.closegroup)
        self.obj.clickOnButton(closegroupbutton,"Closed group")

        submit=self.driver.find_element_by_css_selector(self.finalizeconfirm)
        self.obj.clickOnButton(submit,"Close confirm")

    def getMyOrderitemtext(self):
        try:

            if(self.driver.find_element_by_xpath("//*[@maintitle='My Order']").is_displayed()):
                myorder=self.driver.find_element_by_xpath("//*[@maintitle='My Order']//h2").text
                myorder=myorder.strip()
                return myorder

        except NoSuchElementException:

            myorder="order deleted"
            return myorder






























