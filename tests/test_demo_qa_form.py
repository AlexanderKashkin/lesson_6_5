from lesson_6_5 import StudentRegistrationForm
from tests.path import path_for_picture as path


def test_form(set_window_size):
    first_name = 'Alexey'
    last_name = 'Ivanov'
    email = f'{first_name}_{last_name}@mail.com'
    gender = 'Male'
    year_birthday = '1990'
    month_birthday = 'February'
    day_birthday = '006'
    subject = 'Maths'
    hobby = 'Sports'
    path_for_picture = path
    phone = '1234567890'
    address = 'my_address'
    state = 'NCR'
    city = 'Noida'
    name_image = 'meme.jpg'

    reg_form = StudentRegistrationForm()
    reg_form.open()
    reg_form.fill_first_name(first_name)
    reg_form.fill_last_name(last_name)
    reg_form.fill_email(email)
    reg_form.choose_gender()
    reg_form.fill_mobile(phone)
    reg_form.fill_data_of_birth(year_birthday, month_birthday, day_birthday)
    reg_form.fill_subj(subject)
    reg_form.choose_hobbies()
    reg_form.select_picture(path_for_picture)
    reg_form.fill_current_address(address)
    reg_form.fill_state(state)
    reg_form.fill_city(city)
    reg_form.close()

    reg_form.should_registered_user(first_name,
                                    last_name,
                                    email,
                                    gender,
                                    phone,
                                    year_birthday,
                                    month_birthday,
                                    day_birthday,
                                    subject,
                                    hobby,
                                    name_image,
                                    address,
                                    state,
                                    city)
    reg_form.close_modal_window()
