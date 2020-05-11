
class locators():

    #loginpage locators

        loginbutton='//a/span[text()="Log In"]'
        username_id = "username"
        password_id = "current-password"
        submit_css = "button[type='submit']"


        #startnewgroup_xpath = "//a[@class='header__create-group-btn--desktop ng-star-inserted']/span[text()='Finish your group']"
        startnewgroup_xpath = "//a/*[text()='Start a new group']"
    #profilepage locators
        profileimage_xpath="//button[@id='dropDown']"
        profile_xpath="//button[@class='dropdown-item'][1]"
        settings_xpath="//button[@class='dropdown-item'][2]"
        editprofile_xpath="//*[@class='app-container__sidebar-wrapper']//button[1]"

        descriptionprofile_id="aboutTextArea"
        savebutton_css= "[type='submit']"
        about_tagname="app-description"

        grouplink="//ul[@role='navigation']/li[1]/a"
        dropdown_delivary="//button[text()=' Delivery Groups ']"
        startnewgroup="//a/span[contains(text(),'Start a delivery group')]"

        #startnewgroup_class="header__create-group-btn--desktop ng-star-inserted"

    #DelivaryPage locators



        delivary_group="//h3[text()='Delivery Group']"
        reuseradiobutton_id="reuseGroup"
        grocerydelivarybutton="//h3[text()='Grocery Delivery']"
        memeberlimit_name="members-limit"
        finishbutton="//button[text()=' Finish ']"

        placeanorderbutton="//app-delivery-details-sidebar-actions/button[contains(text(),'Place')]"
        textarea_id="description"

        editorder_xpath="//app-delivery-details-sidebar-actions/button[1]"
        leavegroup_xpath="//app-delivery-details-sidebar-actions/button[2]"

        finalizeorders="//app-delivery-details-sidebar-actions/button[2]"
        closegroup="//app-delivery-details-sidebar-actions/button[1]"

        orderstab="//*[@class='group-details-header__nav']//ul[@role='navigation']/li[2]"






    #Settings page Locators

        edit_class="//button[@*='app-btn--primary app-btn--outline']"
        firstname_id="given-name"
        lastname_id="family-name"
        displayname_id="display_name"
        save_css="[type='submit']"

        classname="col-md-9 col-sm-12"

    ##Group Page Locators

        #viewallcategories="//button[text()='View all available categories']"
        searchbox_xpath="//input[@*='Search for categories']"
        #groupname="//label[text()='Pest Control']"

        #confirm_css="button[type='submit']"
        nextbtn_xpath="//button[text()=' Next ']"
        groupname_xpath="//*[@role='listbox']"

        textarea_tagname="textarea"
        status_xpath="//div[text()='FORMING' and @class='campaign-status--forming app-text--bold app-margin__sm--b']"


        grouptlink1_xpath = "//*[@maintitle='Groups']//*[@role='tablist']/a[1]"


        grouptlink2_xpath = "//*[@maintitle='Groups']//*[@role='tablist']/a[2]"
        grouptlink3_xpath = "//*[@maintitle='Groups']//*[@role='tablist']/a[3]"


        status1_xpath="//*[@maintitle='Status']//*[@role='tablist']/a[1]"

        status2_xpath = "//*[@maintitle='Status']//*[@role='tablist']/a[2]"
        status3_xpath="//*[@maintitle='Status']//*[@role='tablist']/a[3]"


#Ok button locator on confirm popup
        confirm_btn_css="button[type='submit']"
        #joined group locators
        grouptlink_xpath="//*[@maintitle='Groups']//*[@role='tablist']/a[1]"
        statuslink_xpath="//*[@maintitle='Status']//*[@role='tablist']/a[2]"
        groupitme1_xpath="//app-campaign-list//app-campaign-item[1]/div"
        JoinGroupbutton_xpath="//app-campaign-details-sidebar-action//button[contains(text(),'Join this')]"
        descriptiom_id="description"
        submit_joingroup_xpath="//button[text()=' Submit ']"
        Groupheaderlink="//a/span[text()='Groups']"
        itemafterjoining_xpath="//app-campaign-list//app-campaign-item[1]/div"
        joinedstatus_xpath="//app-campaign-item[1]//app-campaign-item-status/app-campaign-user-status[1]//*[contains(text(),'Joined')]"

        leavegroupbutton_xpath="//app-campaign-details-sidebar-action/*[contains(text(),' Leave this group')]"

        overviewtab_xpath="//span[text()='Overview']"
        memberstab_xpath="//span[contains(text(),'Members')]"
        owner_tagname="h4"
        memberinfo_xpath="//*[@maintitle='My Request']//app-campaign-user-card//h4"

        makeofferbutton_xpath="//app-campaign-details-sidebar-action/button[1]"
        price_id="price"
        select_tag="select"
        grouppriceenabled_id="group-price-enabled"
        textarea_id='description'
        checkbox_id="termsofuse"
        submit_offer_css="button[type='submit']"
        offers_tab_xpath="//a/span[contains(text(),'Offers')]"
        pro_tag="h4"

    #Locators Provider Page

        messagebutton="//*[@class='app-container__sidebar d-none d-md-block']//app-send-message-button"
        messagetextarea_tagname="textarea"

        messageicon_css="app-notifications-btn"
        messagetext_xpath="//app-conversation-item[1]//div[@*='conversation-item__text']"
    #reviewbutton
        Reviewbutton_xpath="//*[@class='app-container__sidebar d-none d-md-block']//app-profile-actions-sidebar/button"
        title_css="input[aria-label='Title:']"
        yourreview_css="#reviewText"
        reviewcheckbox_css="#certify-check[type=checkbox]"
        submit_css="button[type='submit']"
        stars_xpath="//app-profile-reviews-form//div[@class='simple-rating-stars__stars-bottom']/span[2]"

        reviewtab_xpath="//*[@class='profile-header__nav']//*[@role='navigation']/li[3]"

    #DeliveryPage




























