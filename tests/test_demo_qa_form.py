from config import browser as b
from selene import have
from lesson_6_5 import StudentRegistrationForm, UserStudent


def test_form(set_window_size):
    user = UserStudent()
    reg_form = StudentRegistrationForm(user)
    reg_form.open()
    reg_form.register()
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
