from Utility.Locators import locators
from Utility.Commonfunction import commonfunction
import time

class settingspage:

    def __init__(self,driver,obj):

        self.driver=driver
        self.obj=obj

        #locators for setting page
        self.edit=locators.edit_class
        self.firstname=locators.firstname_id
        self.lastname=locators.lastname_id
        self.displayname=locators.displayname_id
        self.savebtn=locators.savebutton_css
        self.classname=locators.classname



    def editSetting(self,fname,lname,disname):
        editbutton=self.driver.find_element_by_xpath(self.edit)
        self.obj.moveToelement(editbutton)
        self.obj.clickOnButton(editbutton, "Edit Button")
        self.obj.switchToFrame()
        firstname=self.driver.find_element_by_id(self.firstname)
        lastname=self.driver.find_element_by_id(self.lastname)
        displayname=self.driver.find_element_by_id(self.displayname)
        savebutton=self.driver.find_element_by_css_selector(self.savebtn)

        self.obj.enterText(firstname, fname, "FirstName TextBox")
        self.obj.enterText(lastname, lname, "LastName TextBox")
        self.obj.enterText(displayname, disname, "DisplayName TextBox")

        self.obj.clickOnButton(savebutton,"Save Button")

        self.obj.switchToparent()

    def getSettingInfo(self):

        time.sleep(5)
        list=self.driver.find_elements_by_tag_name("dd")

        return list









