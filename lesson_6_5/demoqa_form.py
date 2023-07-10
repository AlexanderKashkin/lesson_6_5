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

    def should_registered_user(self, user: UserStudent):
        full_name = f'{user.first_name} {user.last_name}'
        b.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
        b.all('.table-responsive>table>tbody>tr').should(have.size(10))
        b.element('.table').all('td').even.should(
            have.exact_texts(
                full_name,
                user.email,
                user.gender,
                user.phone,
                f'{user.day_birthday[1:]} {user.month_birthday},{user.year_birthday}',
                user.subject,
                f'{user.hobby}',
                user.name_image,
                user.address,
                f'{user.state} {user.city}'
            )
        )