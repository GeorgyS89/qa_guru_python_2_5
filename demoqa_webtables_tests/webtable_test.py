
from selene.support.shared import browser

def test_webtables():

    browser.open('https://demoqa.com/webtables')

    browser.element('#addNewRecordButton').click()
    browser.element('#firstName').type('Gosha')
    browser.element('#lastName').type('Smirnov')
    browser.element('#userEmail').type('gugugeguguge@gmail.com')
    browser.element('#age').type('33')
    browser.element('#salary').type('0')
    browser.element('#department').type('THE Department')
    browser.element('#submit').click()

    browser.element('#edit-record-2').click()
    browser.element('#firstName').clear().type('Chel')
    browser.element('#lastName').clear().type('Chelibosov')
    browser.element('#userEmail').clear().type('chel@chelibos.com')
    browser.element('#age').clear().type('30')
    browser.element('#salary').clear().type('300000')
    browser.element('#department').clear().type('Department chelikov')
    browser.element('#submit').click()
    browser.element('#delete-record-3').click()
