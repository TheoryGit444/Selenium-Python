from Utility.Locators import locators

from Pages.OfferPage import offerpage
from Pages.ProviderPage import providerpage
from Pages.OfferPage import offerpage

class grouppage():

    def __init__(self,driver,obj):

        self.driver=driver
        self.obj=obj



        #self.viewcategorylink=locators.viewallcategories
        #self.groupname=locators.groupname
        #self.confirmbtn=locators.confirm_css
        self.searchbox=locators.searchbox_xpath
        self.nextbtn=locators.nextbtn_xpath
        self.description=locators.textarea_tagname
        self.status=locators.status_xpath
        self.groupname=locators.groupname_xpath

        self.confirm_ok=locators.confirm_btn_css

        self.grouplink=locators.groupitme1_xpath



        self.JoinButton=locators.JoinGroupbutton_xpath

        self.DescriptionTextBox=locators.descriptiom_id

        self.SubmitJoingroup=locators.submit_joingroup_xpath

        self.Groupheaderlink=locators.Groupheaderlink

        self.item1=locators.itemafterjoining_xpath

        self.joinstatus=locators.joinedstatus_xpath

        self.leavegroup=locators.leavegroupbutton_xpath

        self.overview=locators.overviewtab_xpath
        self.ownername=locators.owner_tagname
        self.member=locators.memberstab_xpath
        self.member_info=locators.memberinfo_xpath
        self.makofferbtn=locators.makeofferbutton_xpath
        #offertab section
        self.offertab=locators.offers_tab_xpath
        self.proname = locators.pro_tag




    def getownerinfo(self):

        overview_tab=self.driver.find_element_by_xpath(self.overview)
        self.obj.clickOnButton(overview_tab,"Overview Tab")

        ownername=self.driver.find_element_by_tag_name(self.ownername).text

        return ownername

    def getmemberinfo(self):

        member_tab=self.driver.find_element_by_xpath(self.member)
        self.obj.clickOnButton(member_tab,"Member Tab")

        memberinfo=self.driver.find_element_by_xpath(self.member_info).text

        return memberinfo

    def launchOfferSection(self):

        offertab=self.driver.find_element_by_xpath(self.offertab)

        self.obj.clickOnButton(offertab,"Offer")
        return offerpage(self.driver,self.obj)

    def launchProviderPage(self):
        proname = self.driver.find_element_by_tag_name(self.proname)
        self.obj.clickOnButton(proname,"Pro Name")

        return providerpage(self.driver,self.obj)

    def leaveGroup(self):
        leavegrpbutton=self.driver.find_element_by_xpath(self.leavegroup)
        self.obj.clickOnButton(leavegrpbutton,"Leave This Group Button")

        OK=self.driver.find_element_by_css_selector(self.confirm_ok)
        self.obj.clickOnButton(OK,"Confirm Button on PopUP")

    def makeAnOffer(self):

        MakeOfferButton=self.driver.find_element_by_xpath(self.makofferbtn)
        self.obj.clickOnButton(MakeOfferButton,"Make Offer Button")

        return offerpage(self.driver,self.obj)







    def joinGroup(self):



        JoinButton=self.driver.find_element_by_xpath(self.JoinButton)
        self.obj.clickOnButton(JoinButton,"Join the Group")

 #   time.sleep(10)
        NextButton=self.driver.find_element_by_xpath(self.nextbtn)
        self.obj.clickOnButton(NextButton, "Next button")
        self.obj.clickOnButton(NextButton, "Next button")
        DescriptionBox= self.driver.find_element_by_id(self.DescriptionTextBox)
        self.obj.enterText(DescriptionBox,"hello this is Priyanka doing Sauce lab test on selenium with python","Description Box")

        self.obj.clickOnButton(NextButton, "Next button")
        self.obj.clickOnButton(NextButton, "Next button")

        Submitbtn=self.driver.find_element_by_xpath(self.SubmitJoingroup)
        self.obj.clickOnButton(Submitbtn,"Submit Button")

        self.obj.sleep(3)
        confirmpopup=self.driver.find_element_by_css_selector(self.confirm_ok)
        self.obj.clickOnButton(confirmpopup,"Confirm OK")




    def createNewGroup(self,text):

        self.obj.sleep(5)

        searchbx=self.driver.find_element_by_xpath(self.searchbox)

        self.obj.enterText(searchbx,"House Cleaning","Group Name")
        self.obj.sleep(5)

        grouplistbtn=self.driver.find_element_by_xpath(self.groupname)

        self.obj.clickOnButton(grouplistbtn,"Group Name")


        #groupname=self.driver.find_element_by_xpath(self.groupname)

        #self.obj.clickOnButton(groupname,"Group Name Link")
        #confirmbutton=self.driver.find_element_by_css_selector(self.confirmbtn)
        #self.obj.clickOnButton(confirmbutton,"Confirm Button")

        nextbutton=self.driver.find_element_by_xpath(self.nextbtn)
        self.obj.clickOnButton(nextbutton,"Next Button")

        self.obj.clickOnButton(nextbutton,"Next Button")

        self.obj.clickOnButton(nextbutton, "Next Button")
        self.obj.clickOnButton(nextbutton, "Next Button")
        description=self.driver.find_element_by_tag_name(self.description)
        self.obj.enterText(description,text,"DescriptionBox")
        self.obj.clickOnButton(nextbutton, "Next Button")
        self.obj.clickOnButton(nextbutton, "Next Button")
        self.obj.clickOnButton(nextbutton, "Next Button")

        self.obj.sleep(5)

        #click ok on confirmation popup

        OK=self.driver.find_element_by_css_selector(self.confirm_ok)

        self.obj.clickOnButton(OK, "OK Button(confirm popup)")

        groupstatus=self.driver.find_element_by_xpath(self.status)
        return groupstatus.text







