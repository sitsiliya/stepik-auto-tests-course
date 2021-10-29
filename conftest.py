import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language. Use option --language=en")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    browser = None
    if language != None:
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        print("\n|||||||||||start chrome browser for test..||||||||||||")
        print(language)
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("Should be using option --language=en")
    yield browser
    print("\nquit browser..")
    browser.quit()