from typing import Tuple

from selene import have, command
from selene.support.shared import browser

from demoqa_registration_tests.user_data import gosha, Subject, Hobby
from model.controls.dropdown import DropDown
from model.controls.datepicker import DatePicker
from utils.path import upload


class RegistrationForm:
    def __init__(self):
        self.birthday = DatePicker(browser.element('#dateOfBirthInput'))

    def open_browser_and_remove_ads(self):
        browser.open('/automation-practice-form')
        ads = browser.all('[id^=google_ads][id*=container]')
        if ads.with_(timeout=6).wait.until(have.size_greater_than_or_equal(3)):
            ads.perform(command.js.remove)
        return self

    def set_first_name(self, first_name: str):
        browser.element('#firstName').type(first_name)
        return self

    def set_last_name(self, last_name: str):
        browser.element('#lastName').type(last_name)
        return self

    def set_email(self, email: str):
        browser.element('#userEmail').type(email)
        return self

    def select_gender(self, gender):
        browser.all('[for^=gender-radio]').by(
            have.exact_text(gender.value)
        ).first.click()
        return self

    def set_mobile(self, mobile: str):
        browser.element('#userNumber').type(mobile)
        return self

    def select_date_of_birth(self, birth_year, birth_month, birth_day):
        self.birthday.select_date(birth_year, birth_month, birth_day)
        return self

    def type_subjects(self, values: Tuple[Subject]):
        for subject in values:
            browser.element('#subjectsInput').type(subject.value).press_enter()
        return self

    def click_subjects(self, values: Tuple[Subject]):
        for subject in values:
            browser.element('#subjectsInput').click().type(subject.value)
            browser.element('[id^="react-select-2"]').click()
        return self

    def select_hobby(self, values: Tuple[Hobby]):
        for hobby in values:
            browser.all('[id^=hobbies]').by(have.value(hobby.value)).first.element(
                '..'
            ).click()
        return self

    def upload_picture(self, picture):
        upload(picture)
        return self

    def set_address(self, address: str):
        browser.element('#currentAddress').type(address)
        return self

    def set_state(self, value):
        browser.element('#state').perform(command.js.scroll_into_view)
        DropDown.select(self, browser.element('#state'), value)
        return self

    def set_city(self, value):
        DropDown.select(self, browser.element('#city'), value)
        return self

    def press_submit(self):
        browser.element('#submit').perform(command.js.scroll_into_view)
        browser.element('#submit').press_enter()
        return self
