import pytest
from config import bot, chat_id


@pytest.hookimpl(trylast=True)
def pytest_sessionfinish(session, exitstatus):
    bot.send_message(chat_id, "Теговые тесты сделал, отчет по ссылке - https://101internettests.github.io/autotests/")