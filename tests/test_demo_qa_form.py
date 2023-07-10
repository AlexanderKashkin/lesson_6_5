from config import browser as b
from selene import have
from lesson_6_5 import StudentRegistrationForm, UserStudent


def test_form(set_window_size):
    alexey_user = UserStudent()
    reg_form = StudentRegistrationForm()
    reg_form.open()
    reg_form.register(alexey_user)
    reg_form.close()
    reg_form.should_registered_user(alexey_user)