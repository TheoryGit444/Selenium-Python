
from Utility.Locators import locators

class providerpage():

    def __init__(self,driver,obj):

        self.driver=driver
        self.obj=obj

        self.messagebtn=locators.messagebutton
        self.messagetext=locators.messagetextarea_tagname
        self.sendbutton=locators.submit_offer_css

        self.envelope=locators.messageicon_css
        self.messagesent=locators.messagetext_xpath

        self.reviewbutton=locators.Reviewbutton_xpath
        self.stars=locators.stars_xpath
        self.title=locators.title_css
        self.reviewtext=locators.yourreview_css
        self.iconfirm=locators.reviewcheckbox_css
        self.submitreview=locators.submit_css

        self.reviewtab=locators.reviewtab_xpath



    def clickMessageButton(self):

        messagebutton=self.driver.find_element_by_xpath(self.messagebtn)
        self.obj.clickOnButton(messagebutton,"Message Button")

    def WriteMessage(self,text):

        message=self.driver.find_element_by_tag_name(self.messagetext)
        self.obj.enterText(message,text,"Message Textbox")

    def sendMessage(self):
        sendbutton=self.driver.find_element_by_css_selector(self.sendbutton)
        self.obj.clickOnButton(sendbutton,"Send ")

    def getRecentMessageSent(self):

        messageenvelope=self.driver.find_element_by_css_selector(self.envelope)
        self.obj.clickOnButton(messageenvelope,"Message envelope")

        self.pageload(5)

        messagesent=self.driver.find_element_by_xpath(self.messagesent)
        return  messagesent.text

    def clickOnReviewButton(self):

        reviewbutton=self.driver.find_element_by_xpath(self.reviewbutton)
        self.obj.clickOnButton(reviewbutton,"Write Review")


    def WriteReviewToPro(self,text):

        rating=self.driver.find_element_by_xpath(self.stars)
        self.obj.clickOnButton(rating,"Rating")

        title=self.driver.find_element_by_css_selector(self.title)
        self.obj.clickOnButton(title,"Title")

        yourreview=self.driver.find_element_by_css_selector(self.reviewtext)
        self.obj.enterText(yourreview,text,"Your Review")

        checkbox=self.driver.find_element_by_xpath(self.iconfirm)
        self.driver.execute_script("arguments[0].click();", checkbox)

        submitreview= self.driver.find_element_by_css_selector(self.submitreview)
        self.obj.clickOnButton(submitreview,"Submit Review")



    def clickOnReviewTab(self):
        self.obj.sleep(2)
        reviewtab=self.driver.find_element_by_xpath(self.reviewtab)
        self.obj.clickOnLink(reviewtab,"Review Tab")


    def verifyRecentReview(self):
        reviewobject=self.driver.find_element_by_xpath("//*[@class='profile-review-item__container']")
        return reviewobject















