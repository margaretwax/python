import os
import time

XPATH_LOGIN_INPUT = '//UIAApplication[1]/UIAWindow[1]/UIATextField[1]'
XPATH_PASSWORD_INPUT = '//UIAApplication[1]/UIAWindow[1]/UIASecureTextField[1]'
XPATH_MENU_MESSAGES = '//UIAApplication[1]/UIAWindow[1]/UIATabBar[1]/UIAButton[4]'

PHONE_NUMBER_SELLER = '0000009192'
PHONE_NUMBER_BUYER = '0000009191'
PASSWORD_SELLER = '123'
PASSWORD_BUYER = '123'

random_email = lambda: 'oorraatest_mobile_' + os.urandom(8).encode('hex') + '@oorraa.com'
random_name = lambda: 'oorraatest_mobile_' + os.urandom(5).encode('hex')


def click_and_send_keys(driver, xpath, value):
    el = driver.find_element_by_xpath(xpath)
    el.click()
    el.send_keys(value)


def nextscreen(driver):
    for index in ['OK', 'Next', 'Next', 'Next', 'Next', 'Start']:
        driver.find_element_by_name(index).click()


def do_login(driver, role='seller'):
    if role == 'buyer':
        phone = PHONE_NUMBER_BUYER
        password = PASSWORD_BUYER
    else:
        phone = PHONE_NUMBER_SELLER
        password = PASSWORD_SELLER

    # allow notifications
    driver.find_element_by_name('OK').click()

    # skip promo screens
    driver.find_element_by_name('Skip').click()

    # go to menu messages page
    driver.find_element_by_xpath(XPATH_MENU_MESSAGES).click()

    # switch to login by phone
    driver.find_element_by_name('Phone').click()

    # enter phone number as login
    click_and_send_keys(driver, XPATH_LOGIN_INPUT, phone)

    # enter password
    click_and_send_keys(driver, XPATH_PASSWORD_INPUT, password)

    # login
    driver.find_element_by_name('Login').click()


def do_reg(driver):
    find_name = driver.find_element_by_name
    find_xpath = driver.find_element_by_xpath

    nextscreen(driver) #skip promo screen

    find_xpath("//UIAApplication[1]/UIAWindow[1]/UIATabBar[1]/UIAButton[3]").click()  # login button (messages)
    find_name("Registration").click()  # change to registration

    click_and_send_keys(driver, '//UIAApplication[1]/UIAWindow[1]/UIATextField[2]', random_email()) # tap on email and send keys 'email random'
    click_and_send_keys(driver, "//UIAApplication[1]/UIAWindow[1]/UIASecureTextField[1]", "123456") #tap on password and send keys 123456 as password
    find_xpath("//UIAApplication[1]/UIAWindow[1]/UIAButton[3]").click()  # tap 'registration''s button

    find_xpath( "//UIAApplication[1]/UIAWindow[1]/UIAAlert[1]/UIACollectionView[1]/UIACollectionCell[3]/UIAButton[1]").click()  # accept rules

    find_name("Upload a photo").click()  # tap upload a photo
    find_name("OK").click()  # tap on springboard access to user's photos
    find_xpath("//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/UIAStaticText[1]").click()  # select moments folder
    find_xpath("//UIAApplication[1]/UIAWindow[1]/UIACollectionView[1]/UIACollectionCell[9]").click()  # choose a photo

    click_and_send_keys(driver, "//UIAApplication[1]/UIAWindow[1]/UIATextField[1]", random_name()) # tap on first name and input user's first name 'random'

    find_name("Begin").click()  # tap to Begin button
    find_name("OK").click()  # tap OK button on springboard
    time.sleep(3)
