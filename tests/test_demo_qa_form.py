import os

from config import browser as b
from selene import be, have
from lesson_6_5.demoqa_form import StudentRegistrationForm


def test_form(set_window_size):
    reg_form = StudentRegistrationForm()
    reg_form.open()
    reg_form.fill_first_name()
    reg_form.fill_last_name()
    reg_form.fill_email()
    reg_form.choose_gender()
    reg_form.fill_mobile()
    reg_form.fill_data_of_birth()
    reg_form.fill_subj()
    reg_form.choose_hobbies()
    reg_form.select_picture()
    reg_form.fill_current_address()
    reg_form.fill_state()
    reg_form.fill_city()
    reg_form.close()

    b.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    b.all('.table-responsive>table>tbody>tr').should(have.size(10))
    reg_form.table_responsive.element_by(have.text('Student Name')).should(
        have.text(f'{reg_form.first_name} {reg_form.last_name}'))
    reg_form.table_responsive.element_by(have.text('Student Email')).should(have.text(f'{reg_form.email}'))
    reg_form.table_responsive.element_by(have.text('Gender')).should(have.text(f'{reg_form.gender}'))
    reg_form.table_responsive.element_by(have.text('Mobile')).should(have.text(f'{reg_form.phone}'))
    reg_form.table_responsive.element_by(have.text('Date of Birth')).should(
        have.text(f'{reg_form.day_birthday[1:]} {reg_form.month_birthday},{reg_form.year_birthday}'))
    reg_form.table_responsive.element_by(have.text('Subjects')).should(have.text(f'{reg_form.subject}'))
    reg_form.table_responsive.element_by(have.text('Hobbies')).should(have.text(f'{reg_form.hobby}'))
    reg_form.table_responsive.element_by(have.text('Picture')).should(have.text('meme.jpg'))
    reg_form.table_responsive.element_by(have.text('Address')).should(have.text(f'{reg_form.address}'))
    reg_form.table_responsive.element_by(have.text('State and City')).should(
        have.text(f'{reg_form.state} {reg_form.city}'))
    reg_form.close_modal_window()
