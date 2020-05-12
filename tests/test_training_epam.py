from selene.support.shared import browser, config
from selene import by, have

def test_login():
    browser.open_url("https://www.training.epam.ua/")

    browser.element('//div[@class="header-control header-auth"]').click()

    browser.element('//input[@id="signInEmail"]').type('test2020.epam@gmail.com')
    browser.element('//input[@id="signInPassword"]').type('Qwe123ewQ')


    browser.element('//input[contains(@class,"popup-reg-sign-in-form__sign-in")]').click()


test_login()