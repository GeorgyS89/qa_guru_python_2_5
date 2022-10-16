from model.pages.registration_form import *
from utils.app import given_opened_browser
from utils.app import remove_ads
from utils.assertions import check_submitted_form
from utils.path import upload
from model.pages.registration_form import RegistrationForm


def test_submit_user_details():
    # GIVEN
    given_opened_browser('/automation-practice-form')
    remove_ads()
    # WHEN

    RegistrationForm.set_first_name(gosha.name)
    set_last_name(gosha.last_name)
    set_email(gosha.email)
    select_gender(gosha.gender.value)

    set_mobile(gosha.mobile)

    select_date_of_birth()

    select_subjects(gosha.subjects)

    select_hobby()

    upload(gosha.picture_file)

    set_address(gosha.current_address)

    set_state(gosha.state)

    set_city(gosha.city)

    press_submit()

    # THEN

    check_submitted_form(
        [
            ('Student Name', 'Gosha Smirnov'),
            ('Student Email', 'gugugeguguge@gmail.com'),
            ('Gender', 'Male'),
            ('Mobile', '8889991011'),
            ('Date of Birth', '10 May,1989'),
            ('Subjects', 'History, Maths'),
            ('Hobbies', 'Sports'),
            ('Picture', '22460.jpg'),
            ('Address', 'Somewhere here'),
            ('State and City', 'NCR Gurgaon')
        ]
    )
