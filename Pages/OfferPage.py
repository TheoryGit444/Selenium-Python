from Utility.Locators import locators
from selenium.webdriver.support.ui import Select
from Pages.ProviderPage import providerpage

class offerpage():

    def __init__(self,driver,obj):
        self.driver=driver
        self.obj=obj

        self.price=locators.price_id
        self.select=locators.select_tag
        self.discount=locators.grouppriceenabled_id
        self.description=locators.descriptiom_id
        self.termsofuse=locators.checkbox_id
        self.createbutton=locators.submit_offer_css

        self.OK=locators.confirm_btn_css

        self.offertab=locators.offers_tab_xpath
        self.proname=locators.pro_tag


    def submitOffer(self):

        price=self.driver.find_element_by_id(self.price)
        self.obj.enterText(price,"45","Enter Price")

        select=Select(self.driver.find_element_by_tag_name(self.select))
        select.select_by_value("Group")

        enable=self.driver.find_element_by_id(self.discount)
        self.obj.clickOnButton(enable,"Group Discount Enabled")

        desc=self.driver.find_element_by_id(self.description)
        text="I am Service provider with larger business of connection 50 service businesses all over the North Carolina.My workers are very skilled and provide services on weekly and per hour basis,"

        self.obj.enterText(desc,text,"Description TextBox")

        createbutton=self.driver.find_element_by_css_selector(self.createbutton)
        self.obj.clickOnButton(createbutton,"Create button")

        OK=self.driver.find_element_by_css_selector(self.OK)
        self.obj.clickOnButton(OK,"Confirm pop up")

        self.obj.sleep(3)

        offertab=self.driver.find_element_by_xpath(self.offertab)

        self.obj.clickOnButton(offertab,"Offer")

        proname=self.driver.find_element_by_tag_name(self.proname)

        if(proname.is_displayed):
            return proname

    def getProviderPage(self,name):

        list=self.driver.find_elements_by_css_selector("app-campaign-offer-item")
        i=0
        for ele in list:
            i=i+1
            xpath_before="//app-campaign-offer-item["
            xpath_after=str(i)+"]//h4"
            xpath=xpath_before+xpath_after
            providerelement=self.driver.find_element_by_xpath(xpath)
            providername=providerelement.text
            if (providername==name):
                providerelement.click()
                self.obj.pageload(5)
                return providerpage(self.driver,self.obj)

            else:
                print("provider given by the test is not present,"+"provider name displayed after execution :"+providername)
                return offerpage(self.driver,self.obj)






