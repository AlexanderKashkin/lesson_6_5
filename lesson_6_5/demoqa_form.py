import os

from config import browser as b
from selene import be, have
from tests.path import path_for_picture as path


class StudentRegistrationForm:
    def __init__(self,
                 first_name: str = 'Alexey',
                 last_name: str = 'Ivanov',
                 gender: str = 'Male',
                 year_birthday: str = '1990',
                 month_birthday: str = 'February',
                 day_birthday: str = '006',
                 subject: str = 'Maths',
                 hobby: str = 'Sports',
                 path_for_picture: str = path,
                 phone: str = '1234567890',
                 address: str = 'my_address',
                 state: str = 'NCR',
                 city: str = 'Noida',
                 ):
        self.first_name = first_name
        self.last_name = last_name
        self.email = f'{self.first_name.lower()}_{self.last_name.lower()}@email.com'
        self.gender = gender
        self.year_birthday = year_birthday
        self.month_birthday = month_birthday
        self.day_birthday = day_birthday
        self.subject = subject
        self.hobby = hobby
        self.path_for_picture = path_for_picture
        self.phone = phone
        self.address = address
        self.state = state
        self.city = city
        self.table_responsive = b.all('.table-responsive tr')

    def open(self):
        b.open('automation-practice-form')
        b.should(have.title('DEMOQA'))
        b.element('[class="main-header"]').should(have.text('Practice Form'))

    def fill_first_name(self):
        b.element('#firstName').should(be.blank).click().type(self.first_name)

    def fill_last_name(self):
        b.element('#lastName').should(be.blank).click().type(self.last_name)

    def fill_email(self):
        b.element('#userEmail').should(be.blank).click().type(self.email)

    def choose_gender(self):
        b.element('[for="gender-radio-1"]').click()

    def fill_mobile(self):
        b.element('#userNumber').should(be.blank).click().type(self.phone)

    def fill_data_of_birth(self):
        b.element('#dateOfBirthInput').click()
        b.element('[class="react-datepicker__year-select"]').click().type(self.year_birthday).click()
        b.element('[class="react-datepicker__month-select"]').click().type(self.month_birthday).click()
        b.element(f'[class="react-datepicker__day react-datepicker__day--{self.day_birthday}"]').click()

    def fill_subj(self):
        b.element('#subjectsInput').type(self.subject).press_enter()

    def choose_hobbies(self):
        b.element(f'//label[contains(text(), "Sports")]').click()

    def select_picture(self):
        b.element('#uploadPicture').send_keys(os.path.abspath(self.path_for_picture))

    def fill_current_address(self):
        b.element('#currentAddress').should(be.blank).click().type(self.address)

    def fill_state(self):
        b.element('#state').click()
        b.element('#react-select-3-input').type(self.state).press_enter()

    def fill_city(self):
        b.element('#react-select-4-input').type(self.city).press_enter()
        b.element('#submit').click()

    def close(self):
        b.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))

    def close_modal_window(self):
        b.element('[id="closeLargeModal"]').click()

    def should_registered_user(self):
        b.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
        b.all('.table-responsive>table>tbody>tr').should(have.size(10))
        b.element('.table').all('td').even.should(
            have.exact_texts(
                f'{self.first_name} {self.last_name}',
                f'{self.email}',
                f'{self.gender}',
                f'{self.phone}',
                f'{self.day_birthday[1:]} {self.month_birthday},{self.year_birthday}',
                f'{self.subject}',
                f'{self.hobby}',
                'meme.jpg',
                f'{self.address}',
                f'{self.state} {self.city}'
            )
        )
