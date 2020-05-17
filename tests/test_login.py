from selene.support.shared import browser, config
from selene import by, have, be
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('/bin/chromedriver', chrome_options=chrome_options)
browser.config.driver = driver

browser.config.window_height = 1080
browser.config.window_width = 1080

config.timeout = 8


def test_login():
    browser.open_url("https://www.training.epam.ua/")

    # Sign In
    browser.element('//div[@class="header-control header-auth"]').click()

    # Enter valid data
    browser.element('//input[@id="signInEmail"]').should(be.blank).type('test2020.epam@gmail.com')
    browser.element('//input[@id="signInPassword"]').should(be.blank).type('Qwe123ewQ')

    # Click 'Sign in' button in pop-up window
    browser.element('//input[contains(@class,"popup-reg-sign-in-form__sign-in")]').click()

    # Check login
    browser.all('//div[@class="user-info__name"]').should(have.text('test2020.epam'))

    # Sign out
    browser.element('//div[@class="dropdown user-info-desktop"]//div[@class="user-info__arrow"]').click()
    browser.element('//div[@class="user-navigation-container"]//div[5]//a[1]').click()


test_login()