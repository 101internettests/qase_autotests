import pytest
from config import bot, сhat_daily


@pytest.hookimpl(trylast=True)
def pytest_sessionfinish(session, exitstatus):
    bot.send_message(сhat_daily, "Пора на дэйли https://us06web.zoom.us/j/89233765337?pwd=akr7biplJEpGIIeWxbHbc29W3yMg13.1 (скоро здесь будет картинка кота)")