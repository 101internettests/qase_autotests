import pytest
from config import bot, chat_id
from selenium import webdriver


@pytest.hookimpl(trylast=True)
def pytest_sessionfinish(session, exitstatus):
    bot.send_message(chat_id, "Утренний поиск сделан, ура!")



