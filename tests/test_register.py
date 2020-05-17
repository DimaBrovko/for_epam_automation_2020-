from selene.support.shared import browser, config
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

def test_sign_up():
    browser.open_url("https://www.training.epam.ua/")

    # Sign In
    browser.element('//p[@class="header-auth__signin"]').click()
    # Register
    browser.element('//p[contains(@class,"popup-reg-footer-actions__register ng-binding")]').click()

    # Enter data function
    def sign_up_input():
        browser.element('//input[@id="registrationEmail"]').type('test2021.epam@gmail.com')
        browser.element('//input[@id="registrationPassword"]').type('Qwe123ewQ')
        browser.element('//label[contains(@class,"section-accept-data-processing__description ng-binding")]').click()
        browser.element('//input[contains(@name,"register")]').click()

    try:
        sign_up_input()
    except:
        browser.element('//p[contains(@class,"popup-reg-footer-actions__register ng-binding")]').click()
        sign_up_input()


test_sign_up()

