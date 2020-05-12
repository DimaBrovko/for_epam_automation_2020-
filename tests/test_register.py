from selene.support.shared import browser, config
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

