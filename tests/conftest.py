import pytest
from config import browser


@pytest.fixture(scope='function')
def set_window_size():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
