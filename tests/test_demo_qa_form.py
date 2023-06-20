from config import browser as b
from selene import be, have


def test_form(set_window_size):
    first_name = 'Alexey'
    last_name = 'Ivanov'
    email = f'{first_name.lower()}_{last_name.lower()}@email.com'
    gender = 'Male'
    year_birthday = '1990'
    month_birthday = 'February'
    day_birthday = '006'
    subject = 'Maths'
    hobby = 'Sports'
    phone = '1234567890'
    address = 'my_address'
    state = 'NCR'
    city = 'Noida'

    b.open('automation-practice-form')
    b.should(have.title('DEMOQA'))
    b.element('[class="main-header"]').should(have.text('Practice Form'))

    b.element('#firstName').should(be.blank).click().type(first_name)
    b.element('#lastName').should(be.blank).click().type(last_name)
    b.element('#userEmail').should(be.blank).click().type(email)
    b.element('[for="gender-radio-1"]').click()
    b.element('#userNumber').should(be.blank).click().type(phone)

    b.element('#dateOfBirthInput').click()
    b.element('[class="react-datepicker__year-select"]').click().type(year_birthday).click()
    b.element('[class="react-datepicker__month-select"]').click().type(month_birthday).click()
    b.element(f'[class="react-datepicker__day react-datepicker__day--{day_birthday}"]').click()

    b.element('#subjectsInput').type(subject).press_enter()
    b.element(f'//label[contains(text(), "Sports")]').click()
    b.element('#currentAddress').should(be.blank).click().type(address)

    b.element('#state').click()
    b.element('#react-select-3-input').type(state).press_enter()
    b.element('#react-select-4-input').type(city).press_enter()
    b.element('#submit').click()

    b.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    b.all('.table-responsive>table>tbody>tr').should(have.size(10))

    b.all('.table-responsive tr').element_by(have.text('Student Name')).should(have.text(f'{first_name} {last_name}'))
    b.all('.table-responsive tr').element_by(have.text('Student Email')).should(have.text(f'{email}'))
    b.all('.table-responsive tr').element_by(have.text('Gender')).should(have.text(f'{gender}'))
    b.all('.table-responsive tr').element_by(have.text('Mobile')).should(have.text(f'{phone}'))
    b.all('.table-responsive tr').element_by(have.text('Date of Birth')).should(
        have.text(f'{day_birthday[1:]} {month_birthday},{year_birthday}'))
    b.all('.table-responsive tr').element_by(have.text('Subjects')).should(have.text(f'{subject}'))
    b.all('.table-responsive tr').element_by(have.text('Hobbies')).should(have.text(f'{hobby}'))
    b.all('.table-responsive tr').element_by(have.text('Address')).should(have.text(f'{address}'))
    b.all('.table-responsive tr').element_by(have.text('State and City')).should(have.text(f'{state} {city}'))

    b.element('[id="closeLargeModal"]').click()
