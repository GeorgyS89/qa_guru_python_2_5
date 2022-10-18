from model.pages.registration_form import *
from utils.app import registration_form
from utils.convert import convert


def test_submit_user_details():
    # GIVEN
    registration_form.open_browser_and_remove_ads()
    # WHEN

    registration_form.set_first_name(gosha.name)
    registration_form.set_last_name(gosha.last_name)
    registration_form.set_email(gosha.email)
    registration_form.select_gender(gosha.gender.value)

    registration_form.set_mobile(gosha.mobile)

    registration_form.select_date_of_birth(gosha.birth_year,gosha.birth_month,gosha.birth_day)

    registration_form.click_subjects(gosha.subjects)

    registration_form.select_hobbies(gosha.hobbies)

    registration_form.upload_picture(gosha.picture_file)

    registration_form.set_address(gosha.current_address)

    registration_form.set_state(gosha.state)

    registration_form.set_city(gosha.city)

    registration_form.press_submit()

    # THEN

    registration_form.check_submitted_form(
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
        ]
    )
