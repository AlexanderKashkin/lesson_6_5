import os

from config import browser as b
from selene import be, have


class StudentRegistrationForm:
    def __init__(self):
        self.table_responsive = b.all('.table-responsive tr')

    def open(self):
        b.open('automation-practice-form')
        b.should(have.title('DEMOQA'))
        b.element('[class="main-header"]').should(have.text('Practice Form'))

    def fill_first_name(self, first_name: str):
        b.element('#firstName').should(be.blank).click().type(first_name)

    def fill_last_name(self, last_name: str):
        b.element('#lastName').should(be.blank).click().type(last_name)

    def fill_email(self, email: str):
        b.element('#userEmail').should(be.blank).click().type(email)

    def choose_gender(self):
        b.element('[for="gender-radio-1"]').click()

    def fill_mobile(self, phone: str):
        b.element('#userNumber').should(be.blank).click().type(phone)

    def fill_data_of_birth(self, year: str, month: str, day: str):
        b.element('#dateOfBirthInput').click()
        b.element('[class="react-datepicker__year-select"]').click().type(year).click()
        b.element('[class="react-datepicker__month-select"]').click().type(month).click()
        b.element(f'[class="react-datepicker__day react-datepicker__day--{day}"]').click()

    def fill_subj(self, subject: str):
        b.element('#subjectsInput').type(subject).press_enter()

    def choose_hobbies(self):
        b.element(f'//label[contains(text(), "Sports")]').click()

    def select_picture(self, path: str):
        b.element('#uploadPicture').send_keys(os.path.abspath(path))

    def fill_current_address(self, address: str):
        b.element('#currentAddress').should(be.blank).click().type(address)

    def fill_state(self, state: str):
        b.element('#state').click()
        b.element('#react-select-3-input').type(state).press_enter()

    def fill_city(self, city: str):
        b.element('#react-select-4-input').type(city).press_enter()
        b.element('#submit').click()

    def close(self):
        b.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))

    def should_registered_user(self, first_name: str, last_name, email: str, gender: str, phone: str, year_birthday: str,
                               month_birthday: str, day_birthday: str, subject: str, hobby: str, name_image: str,
                               address: str, state: str, city: str):
        full_name = f'{first_name} {last_name}'
        b.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
        b.all('.table-responsive>table>tbody>tr').should(have.size(10))
        b.element('.table').all('td').even.should(
            have.exact_texts(
                full_name,
                email,
                gender,
                phone,
                f'{day_birthday[1:]} {month_birthday},{year_birthday}',
                subject,
                f'{hobby}',
                name_image,
                address,
                f'{state} {city}'
            )
        )

    def close_modal_window(self):
        b.element('[id="closeLargeModal"]').click()


