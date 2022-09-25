from selene import have, command
from selene.support.shared import browser


def given_opened_browser(url):
    browser.open(url)


def remove_ads():
    ads = browser.all('[id^=google_ads_][id$=container__')
    if ads.wait.until(have.size_greater_than_or_equal(3)):
        ads.perform(command.js.remove)
