from typing import Tuple

from selene import have, command
from selene.support import by
from selene.support.shared import browser

from demoqa_registration_tests.user_data import Subject, Hobby, gosha
from model.controls.datepicker import DatePicker
from model.controls.dropdown import DropDown
from model.controls.modal import dialog
from utils.convert import convert
from utils.path import upload


class RegistrationForm:
    def __init__(self):
        self.birthday = DatePicker(browser.element('#dateOfBirthInput'))

    def open_browser_and_remove_ads(self):
        browser.open('/automation-practice-form')
        ads = browser.all('[id^=google_ads][id*=container]')
        if ads.with_(timeout=5).wait.until(have.size_greater_than_or_equal(3)):
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
        browser.all('[for^=gender-radio]').by(have.exact_text(gender)
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

    def select_hobbies(self, values: Tuple[Hobby]):
        for hobby in values:
            path = "//label[contains(.,'" + str(hobby.value) + "')]"
            browser.element(by.xpath(path)).click()
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

    def submit_form(self):
        browser.element('#submit').perform(command.js.scroll_into_view)
        browser.element('#submit').press_enter()
        return self

    def check_submitted_form(self, data):
        rows = dialog.all('tbody tr')
        for row, value in data:
            rows.element_by(have.text(row)).all('td')[1].should(have.exact_text(value))
        return self


class RegisterNewUser:
    def __init__(self):
        self.registration_form = RegistrationForm()

    def fill_and_submit(self):
        (
            self.registration_form.open_browser_and_remove_ads()

            .set_first_name(gosha.name)
            .set_last_name(gosha.last_name)
            .set_email(gosha.email)
            .select_gender(gosha.gender.value)
            .set_mobile(gosha.mobile)
            .select_date_of_birth(gosha.birth_year,gosha.birth_month,gosha.birth_day)
            .type_subjects(gosha.subjects)
            .select_hobbies(gosha.hobbies)
            .upload_picture(gosha.picture_file)
            .set_address(gosha.current_address)
            .set_state(gosha.state)
            .set_city(gosha.city)
            .submit_form()

            .check_submitted_form(
                [
                    ('Student Name', f'{gosha.name} {gosha.last_name}'),
                    ('Student Email', gosha.email),
                    ('Gender', gosha.gender.value),
                    ('Mobile', gosha.mobile),
                    ('Date of Birth', f'{gosha.birth_day} {gosha.birth_month},{gosha.birth_year}'),
                    ('Subjects', convert(gosha.subjects)),
                    ('Hobbies', convert(gosha.hobbies)),
                    ('Picture', gosha.picture_file),
                    ('Address', gosha.current_address),
                    ('State and City', f'{gosha.state} {gosha.city}')
                ],
            )
        )