
from Utility.Locators import locators
from Utility.Commonfunction import commonfunction
from Pages.Profilepage import profilepage
from Pages.GroupPage import grouppage


class loginpage():

    def __init__(self, driver):
        self.driver = driver

        # locators

        self.loginbutton=locators.loginbutton
        self.username = locators.username_id
        self.password = locators.password_id
        self.submit = locators.submit_css
        #self.startnewgrorupbtn=locators.startnewgroup_class
        self.startnewgroupbtn=locators.startnewgroup_xpath

        self.obj = commonfunction(self.driver)

    def enter_login(self, username, password):

        loginbutton=self.driver.find_element_by_xpath(self.loginbutton)

        self.obj.clickOnLink(loginbutton,"Login Link")

        user=self.driver.find_element_by_id(self.username)
        self.obj.enterText(user,username,"Username TextBox")

        pwd=self.driver.find_element_by_id(self.password)
        self.obj.enterText(pwd,password,"Password Text Box")

        submit=self.driver.find_element_by_css_selector(self.submit)
        self.obj.clickOnButton(submit,"Login Button")

        return profilepage(self.driver,self.obj)

    def get_title(self):

        title=self.driver.title
        return title

    def startNewGroup(self):

        newgroup=self.driver.find_element_by_xpath(self.startnewgroupbtn)
        self.obj.clickOnButton(newgroup,"Start New Group ")
        grouppg=grouppage(self.driver,self.obj)
        return grouppg


