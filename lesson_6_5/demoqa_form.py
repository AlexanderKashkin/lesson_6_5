import os

from config import browser as b
from selene import be, have

from lesson_6_5 import UserStudent


class StudentRegistrationForm:
    def __init__(self):
        self.table_responsive = b.all('.table-responsive tr')

    def open(self):
        b.open('automation-practice-form')
        b.should(have.title('DEMOQA'))
        b.element('[class="main-header"]').should(have.text('Practice Form'))

    def register(self, user: UserStudent):
        b.element('#firstName').should(be.blank).click().type(user.first_name)
        b.element('#lastName').should(be.blank).click().type(user.last_name)
        b.element('#userEmail').should(be.blank).click().type(user.email)
        b.element('[for="gender-radio-1"]').click()
        b.element('#userNumber').should(be.blank).click().type(user.phone)
        b.element('#dateOfBirthInput').click()
        b.element('[class="react-datepicker__year-select"]').click().type(user.year_birthday).click()
        b.element('[class="react-datepicker__month-select"]').click().type(user.month_birthday).click()
        b.element(f'[class="react-datepicker__day react-datepicker__day--{user.day_birthday}"]').click()
        b.element('#subjectsInput').type(user.subject).press_enter()
        b.element(f'//label[contains(text(), "Sports")]').click()
        b.element('#uploadPicture').send_keys(os.path.abspath(user.path_for_picture))
        b.element('#currentAddress').should(be.blank).click().type(user.address)
        b.element('#state').click()
        b.element('#react-select-3-input').type(user.state).press_enter()
        b.element('#react-select-4-input').type(user.city).press_enter()
        b.element('#submit').click()

    def close(self):
        b.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))

    def close_modal_window(self):
        b.element('[id="closeLargeModal"]').click()

    def assert_reg(self, user: UserStudent):
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