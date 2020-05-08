from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as expected
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common import exceptions
import logging
#import pyperclip
#from pynput.keyboard import Controller,Key
import time


class commonfunction():

    def __init__(self, driver):
        self.driver = driver

        # setting logs for actions perform on page

        self.logger = logging.getLogger(__name__)
         #print("%s",%__name__)
        self.logger.setLevel(logging.INFO)
        logging.basicConfig(filename="info_log.txt",filemode='w',format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
      # create file handler
        self.handler_info = logging.FileHandler("info_log.txt")
        self.handler_info.setLevel(logging.INFO)

        # create a logging format


        #self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # self.handler_warn.setFormatter(self.formatter)
        #self.handler_info.setFormatter(self.formatter)


        # add the handler to the logger

        # self.logger.addHandler(handler_warn)
        self.logger.addHandler(self.handler_info)

        self.logger.info("Logs generated for the test")
    def loadfile(self,path):
        # this is the funcrion to copy paste the url and upload the image
        ##copy data to clipboard
        self.logger.info("Loading Image...")
        time.sleep(8)
        pyperclip.copy(path)
        pyperclip.paste

        print("cpoy path"+path

              )

        time.sleep(4)


        #paste data to the window opened for file upload

        keyboard=Controller()
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        print("pressed enter key")



        # press control v

        keyboard.press(Key.ctrl)
        keyboard.press("v")

        print("pressed control v")

        time.sleep(3)

        # release control v

        keyboard.release(Key.ctrl)
        keyboard.release("v")

        print("release control v")

        time.sleep(3)


        # press and release enter

        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

        print("image loaded")

        self.logger.info("Image Loaded")

    def getcurrentwindow(self):

        mainwindow = self.driver.current_window_handle
        return mainwindow


    def sleep(self,second):
        time.sleep(second)

    def pageload(self,second):
        self.driver.set_page_load_timeout(8)

    def explicitwait(self, time, elementlocator, elementname):

        self.logger.info("waiting for the " + elementname + " to be clickable")

        wait = WebDriverWait(self.driver, time)
        element = wait.until(expected.element_to_be_clickable, elementlocator)
        return element

    def implicitwait(self, time):
        self.logger.info("page is loading...")
        self.driver.implicitly_wait(time)



    def clickOnLink(self,element,elementname):




        #self.explicitwait(20, element, elementname)

        #if (element.is_displayed()):

        for i in range(0, 2):
            try:
                element.click()
                self.logger.info(elementname + " is clicked")
                break
            except exceptions.StaleElementReferenceException as e:
                self.logger.info(e)
                element.click()
                self.logger.info("element is clicked again after the StaleElementException")
                    # print(" \n element cannot be located")

        #else:
         #   self.logger.info(elementname + " is not visible")




    def clickOnButton(self, element, elementname):

        self.explicitwait(20, element, elementname)

        if (element.is_enabled()):

            for i in range(0, 2):
                try:
                    element.click()
                    self.logger.info(elementname + " is clicked")
                    break
                except exceptions.StaleElementReferenceException as e:
                    self.logger.info(e)
                    element.click()
                    self.logger.info("element is clicked again after the StaleElementException")
                    # print(" \n element cannot be located")

        else:
            self.logger.info(elementname + " is not enabled")

    def moveToelement(self, element):

        self.logger.info("move to the element")
        act = ActionChains(self.driver)
        # act.click(element).perform()
        act.move_to_element(element).perform()

    def enterText(self, element, text, elementname):

        if (element.is_enabled()):

            element.clear()
            element.send_keys(text)
            self.logger.info(text + " is entered on " + elementname)
        else:
            self.logger.info(elementname + " is disabled")

    def switchToFrame(self):

        # get window handles
        allwindow = self.driver.window_handles

        for win in allwindow:
            self.driver.switch_to_window(win)
            self.logger.info("switched to frame " + win)

    def switchToparent(self):

        self.driver.switch_to_default_content()
        self.logger.info("switched to parent frame")


    def gettext(self,element):

        textvalue=element.text

        self.logger.info(textvalue)

