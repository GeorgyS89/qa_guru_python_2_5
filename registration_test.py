import os
from selene.core import command
from selene.support.shared import browser
from selene import be, have, command


def test_submit_user_details():
    browser.open('/automation-practice-form')
    browser.should(have.title('ToolsQA'))


    browser.element('#firstName').type('Gosha')
    browser.element('#lastName').type('Smirnov')
    browser.element('#userEmail').type('gugugeguguge@gmail.com')

    browser.execute_script('document.getElementById("gender-radio-1").click()')

    browser.element('#userNumber').type('8889991011')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').type('May')
    browser.element('.react-datepicker__year-select').type('1989')
    browser.element('[aria-label="Choose Wednesday, May 10th, 1989"]').click()

    browser.element('#subjectsInput').type('Computer Science').press_enter().type('English').press_enter()

    browser.execute_script('document.getElementById("hobbies-checkbox-1").click()')

    browser.element('#uploadPicture').send_keys(os.path.abspath('images/22460.jpg'))

    browser.element('#currentAddress').click().type('Somewhere here')

    browser.element('#state').perform(command.js.scroll_into_view).click()

    browser.element('#state').click()
    browser.element('#state input').type('NCR').press_enter()
    browser.element('#city').click()
    browser.element('#city input').type('Noida').press_enter()

    ads = browser.all('[id^=google_ads_][id$=container__')
    if ads.wait.until(have.size_greater_than_or_equal(3)):
        ads.perform(command.js.remove)

    browser.element('#submit').perform(command.js.scroll_into_view)
    browser.element('#submit').press_enter()

    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))

    browser.all('.modal-body td+td').should(have.texts(
        'Gosha Smirnov',
        'gugugeguguge@gmail.com',
        'Male',
        '8889991011',
        '10 May,1989',
        'Computer Science, English',
        'Sports',
        '22460.jpg',
        'Somewhere here',
        'NCR Noida'))