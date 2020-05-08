from Utility.Locators import locators
from Utility.Commonfunction import commonfunction
import time
from Pages.SettingsPage import settingspage
from Pages.GroupPage import grouppage

class profilepage():

    def __init__(self,driver,obj):

        self.driver=driver
        self.obj=obj

        #locators
        self.profileimage=locators.profileimage_xpath
        self.profile=locators.profile_xpath
        self.setting=locators.settings_xpath
        self.edit=locators.editprofile_xpath

        #editprofileframe

        self.profiledescription=locators.descriptionprofile_id
        self.savebutton=locators.savebutton_css
        self.about=locators.about_tagname

        #Home page

        self.statuslink=locators.statuslink_xpath

        self.groupitem1=locators.groupitme1_xpath
        self.Groupheaderlink=locators.Groupheaderlink

        self.item1=locators.itemafterjoining_xpath

        self.joinstatus=locators.joinedstatus_xpath

        self.grouptype1 = locators.grouptlink1_xpath
        self.grouptype2 = locators.grouptlink2_xpath
        self.grouptype3 = locators.grouptlink3_xpath

        self.status1 = locators.status1_xpath
        self.status2 = locators.status2_xpath
        self.status3 = locators.status3_xpath


        self.envelope=locators.messageicon_css
        self.messagereceived=locators.messagetext_xpath


    def getRecentMessageReceived(self):

        messageenvelope=self.driver.find_element_by_css_selector(self.envelope)
        self.obj.clickOnButton(messageenvelope,"Message envelope")

        self.pageload(5)

        messagereceived=self.driver.find_element_by_xpath(self.messagereceived)
        return  messagereceived.text

    def selectGrouptype(self, grouptype):

        if (grouptype == "My Groups"):
            mygroup = self.driver.find_element_by_xpath(self.grouptype1)
            self.obj.clickOnButton(mygroup, "My Group")

        elif grouptype == "Saved":
            saved = self.driver.find_element_by_xpath(self.grouptype2)
            self.obj.clickOnButton(saved, "Saved")
        else:
            nofilter = self.driver.find_element_by_xpath(self.grouptype1)
            self.obj.clickOnButton(nofilter, "No Filter")

    def selectGroupStatus(self, grpstatus):

        if (grpstatus == "Forming"):
            forming = self.driver.find_element_by_xpath(self.status2)
            self.obj.clickOnButton(forming, "Forming")

        elif (grpstatus == "Assigned"):
            assigned = self.driver.find_element_by_xpath(self.status3)
            self.obj.clickOnButton(assigned, "Assigned")

        else:
            nofilter = self.driver.find_element_by_xpath(self.status1)
            self.obj.clickOnButton(nofilter, "No Filter")


    def getgroupstatus(self):


        GroupsLink=self.driver.find_element_by_xpath(self.Groupheaderlink)

        self.obj.clickOnButton(GroupsLink,"GroupsLink")

        Item2=self.driver.find_element_by_xpath(self.item1)
        self.obj.explicitwait(5,Item2,"House Cleaning Object")


        Joinstatus= self.driver.find_element_by_xpath(self.joinstatus)
        if(Joinstatus.is_displayed()):
            return Joinstatus.text
        else:
            return "left group"

    def readGroupObjectWithOffer(self):

        list=self.driver.find_elements_by_css_selector("app-campaign-item")
        i=0
        for ele in list:
            i=i+1
            xpath_before="//app-campaign-item["
            xpath_after=str(i)+"]//a[contains(text(),'Offers')]"
            xpath=xpath_before+xpath_after
            offercountelement=self.driver.find_element_by_xpath(xpath)
            offercount=offercountelement.text

            if (offercount!="0 Offers"):
                break

            else:
                continue

        return i

    def launchGroupWithObjectnumber(self,objectnumber):

        xpath_before="//app-campaign-list//app-campaign-item["
        xpath_after=str(objectnumber)+"]/div"
        xpath=xpath_before+xpath_after
        groupitem=self.driver.find_element_by_xpath(xpath)

        self.obj.clickOnButton(groupitem, "Group Item1")

        self.obj.pageload(10)

        return grouppage(self.driver,self.obj)

        # groupitme1_xpath="//app-campaign-list//app-campaign-item[1]/div"

    def launchGroupPage(self):

        # Group=self.driver.find_element_by_xpath(self.grouplink)

       # Status = self.driver.find_element_by_xpath(self.statuslink)
        # self.obj.clickOnButton(Group,"NO Filter")
        #self.obj.clickOnButton(Status, "Status link")

        groupitem1 = self.driver.find_element_by_xpath(self.groupitem1)

        self.obj.clickOnButton(groupitem1, "Group Item1")

        self.obj.pageload(10)

        return grouppage(self.driver,self.obj)


        #self.obj = commonfunction(self.driver)
    def settingClick(self):
        time.sleep(10)

        profileimage = self.driver.find_element_by_xpath(self.profileimage)

        # self.obj.clickToelement(profileimage)
        self.obj.clickOnButton(profileimage, "Profile Icon")
        settings=self.driver.find_element_by_xpath(self.setting)

        self.obj.clickOnButton(settings,"Setting Link")

        self.obj.implicitwait(6)

        return settingspage(self.driver,self.obj)


    def profileclick(self):

        time.sleep(3)

        profileimage=self.driver.find_element_by_xpath(self.profileimage)

        #self.obj.clickToelement(profileimage)
        self.obj.clickOnButton(profileimage,"Profile Icon")



        profile=self.driver.find_element_by_xpath(self.profile)
        self.obj.clickOnButton(profile,"Profile Link")

        self.obj.implicitwait(6)

    def editButtonClick(self):

        #self.driver.implicitly_wait(20)
        #self.obj.explicitwait(20,locators.editprofile_xpath,"EditProfile Button")
        editprofile=self.driver.find_element_by_xpath(self.edit)
        self.obj.clickOnButton(editprofile,"EditProfile Button")

    def editProfileDetails(self,textentered):

        # switch to edit profile page

        self.obj.switchToFrame()

        #edit descriptiom of the user

        element=self.driver.find_element_by_id(self.profiledescription)

        self.obj.enterText(element,textentered,"Description TextBox")

        element=self.driver.find_element_by_css_selector(self.savebutton)
        self.obj.clickOnButton(element,"Save Button")

        self.obj.switchToparent()

        self.obj.implicitwait(5)

        about=self.driver.find_element_by_tag_name(self.about)
        abouttext=about.text


        return abouttext


    def getprofileimage(self):

        imageloaded=self.driver.find_element_by_xpath('//img[@*="Your profile image."]').is_displayed()
        return imageloaded


    def uploadProfilePhoto(self):
         # saving current window handler

         parent = self.driver.current_window_handle

         #click on change picture

         changepitcure=self.driver.find_element_by_xpath("//*[text()=' Change Picture ']")

         self.obj.clickOnButton(changepitcure,"Change Pitcure Button")


         #uploading picture...
         self.obj.loadfile("C:\\Users\\sauce\\Downloads\\mike-castro-demaria-94BUerwdFP8-unsplash.jpg")

         #click on crop button
         currentwin=self.driver.current_window_handle
        #print("current window after uploading image is :"+currentwin)
         self.driver.switch_to_window(currentwin)



         cropbtn=self.driver.find_element_by_xpath("//button/span[text()=' Crop Image ']")
         self.obj.clickOnButton(cropbtn,"Crop Button")

         #Clicking on save button

         save=self.driver.find_element_by_css_selector("button[type='submit']")
         self.obj.clickOnButton(save,"Save Button")

    def opennewtab(self):

        mainwindow=self.obj.getcurrentwindow()
        time.sleep(3)

        self.driver.execute_script('window.open("https://unsplash.com/photos/94BUerwdFP8","_blank")')
        allwindow = self.driver.window_handles
        print(allwindow)
        for win in allwindow:
            if (win != mainwindow):
                print(win)
                self.driver.switch_to.window(win)

                element = self.driver.find_element_by_xpath("//span[text()='Download free']")
                element.click()
                print("download button is clicked")
                time.sleep(3)
                allwindow1=self.driver.window_handles
                print(allwindow1)

        self.driver.switch_to.window(mainwindow)
        print("switched to main window: " + mainwindow)
        #self.driver.find_element_by_id("username").send_keys("ravi")




















