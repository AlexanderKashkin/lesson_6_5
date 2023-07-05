from lesson_6_5 import StudentRegistrationForm


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

    reg_form.should_registered_user()

    reg_form.close_modal_window()
