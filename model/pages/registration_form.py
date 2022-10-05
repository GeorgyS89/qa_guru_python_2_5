from typing import Tuple

from selene import have, command
from selene.support.shared import browser

from demoqa_registration_tests.user_data import gosha, Subject
from model.controls import dropdown


def set_first_name(first_name):
    browser.element('#firstName').type(first_name)


def set_last_name(last_name):
    browser.element('#lastName').type(last_name)


def set_email(email):
    browser.element('#userEmail').type(email)


def select_gender(gender):
    browser.all('[for^=gender-radio]').by(
        have.exact_text(gender)
    ).first.click()


def set_mobile(mobile):
    browser.element('#userNumber').type(mobile)


def select_date_of_birth():
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').type(gosha.birth_month)
    browser.element('.react-datepicker__year-select').type(gosha.birth_year)
    browser.element(
        f'.react-datepicker__day--0{gosha.birth_day}'
        f':not(.react-datepicker__day--outside-month)'
    ).click()


def select_subjects(values: Tuple[Subject]):
    for subject in values:
        browser.element('#subjectsInput').type(subject.value).press_enter()


def select_hobby():
    for hobby in gosha.hobbies:
        browser.all('[id^=hobbies]').by(have.value(hobby.value)).first.element(
            '..'
        ).click()


def set_address(address):
    browser.element('#currentAddress').type(address)


def set_state(value):
    browser.element('#state').perform(command.js.scroll_into_view)
    dropdown.select(browser.element('#state'), value)



def set_city(value):
    dropdown.select(browser.element('#city'), value)



def press_submit():
    browser.element('#submit').perform(command.js.scroll_into_view)
    browser.element('#submit').press_enter()


