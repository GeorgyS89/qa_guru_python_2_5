import allure
from allure_commons.types import AttachmentType

from model.pages.registration_form import *
from utils.app import given_opened_browser
from utils.app import remove_ads
from utils.assertions import check_submitted_form
from utils.path import upload_picture


@allure.title("Registration form test")
def test_submit_user_details():
    # GIVEN
    with allure.step("Open registration form"):
        given_opened_browser('https://demoqa.com/automation-practice-form')
        remove_ads()
    # WHEN
    with allure.step("Fill and submit form"):
        set_first_name(gosha.name)
        set_last_name(gosha.last_name)
        set_email(gosha.email)

        select_gender(gosha.gender.value)

        set_mobile(gosha.mobile)

        select_date_of_birth()

        select_subjects(gosha.subjects)

        select_hobby()

        upload_picture(gosha.picture_file)

        set_address(gosha.current_address)

        set_state(gosha.state)

        set_city(gosha.city)

        press_submit()

    # THEN
    with allure.step("Check form results"):
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

    def add_screenshot(browser):
        png = browser.driver.get_screenshot_as_png()
        allure.attach(body=png, name='screenshot', attachment_type=AttachmentType.PNG, extension='.png')

    def add_logs(browser):
        log = "".join(f'{text}\n' for text in browser.driver.get_log(log_type='browser'))
        allure.attach(log, 'browser_logs', AttachmentType.TEXT, '.log')

    def add_html(browser):
        html = browser.driver.page_source
        allure.attach(html, 'page_source', AttachmentType.HTML, '.html')

    def add_video(browser):
        video_url = "https://selenoid.autotests.cloud/video/" + browser.driver.session_id + ".mp4"
        html = "<html><body><video width='100%' height='100%' controls autoplay><source src=' " \
               + video_url \
               + "' type='video/mp4'></video></body></html>"
        allure.attach(html, 'video' + browser.driver.session_id, AttachmentType.HTML, '.html')

    add_html(browser)
    add_screenshot(browser)
    add_logs(browser)
    add_video(browser)