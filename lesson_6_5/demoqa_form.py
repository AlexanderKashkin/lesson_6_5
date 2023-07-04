import os

from config import browser as b
from selene import be, have

from lesson_6_5 import UserStudent


class StudentRegistrationForm:
    def __init__(self, user: UserStudent):
        self.first_name = user.first_name
        self.last_name = user.last_name
        self.email = user.email
        self.gender = user.gender
        self.year_birthday = user.year_birthday
        self.month_birthday = user.month_birthday
        self.day_birthday = user.day_birthday
        self.subject = user.subject
        self.hobby = user.hobby
        self.path_for_picture = user.path_for_picture
        self.phone = user.phone
        self.address = user.address
        self.state = user.state
        self.city = user.city
        self.table_responsive = b.all('.table-responsive tr')

    def open(self):
        b.open('automation-practice-form')
        b.should(have.title('DEMOQA'))
        b.element('[class="main-header"]').should(have.text('Practice Form'))

    def register(self):
        b.element('#firstName').should(be.blank).click().type(self.first_name)
        b.element('#lastName').should(be.blank).click().type(self.last_name)
        b.element('#userEmail').should(be.blank).click().type(self.email)
        b.element('[for="gender-radio-1"]').click()
        b.element('#userNumber').should(be.blank).click().type(self.phone)
        b.element('#dateOfBirthInput').click()
        b.element('[class="react-datepicker__year-select"]').click().type(self.year_birthday).click()
        b.element('[class="react-datepicker__month-select"]').click().type(self.month_birthday).click()
        b.element(f'[class="react-datepicker__day react-datepicker__day--{self.day_birthday}"]').click()
        b.element('#subjectsInput').type(self.subject).press_enter()
        b.element(f'//label[contains(text(), "Sports")]').click()
        b.element('#uploadPicture').send_keys(os.path.abspath(self.path_for_picture))
        b.element('#currentAddress').should(be.blank).click().type(self.address)
        b.element('#state').click()
        b.element('#react-select-3-input').type(self.state).press_enter()
        b.element('#react-select-4-input').type(self.city).press_enter()
        b.element('#submit').click()

    def close(self):
        b.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))

    def close_modal_window(self):
        b.element('[id="closeLargeModal"]').click()
