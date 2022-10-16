from selene import have

from model.controls.modal import dialog


def check_submitted_form(data):
    rows = dialog.all('tbody tr')
    for row, value in data:
        rows.element_by(have.text(row)).all('td')[1].should(have.exact_text(value))
