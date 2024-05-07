import pytest
from config import bot, chat_id


@pytest.hookimpl(trylast=True)
def pytest_sessionfinish(session, exitstatus):
    bot.send_message(chat_id, "Все формы отправил, отчет будет в ссылке")
