from selene import have
from selene.support.shared import browser


def check_submitted_form(data):
    dialog = browser.element('.modal-content')
    rows = dialog.all('tbody tr')
    for row, value in data:
        rows.element_by(have.text(row)).all('td')[1].should(have.exact_text(value))
