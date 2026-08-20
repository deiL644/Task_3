from __future__ import annotations

import pytest

from helpers.api_client import StellarApiClient
from helpers.browser_factory import WebdriverFactory


def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption(
        "--browser",
        action="store",
        default="all",
        choices=("all", "chrome", "firefox"),
        help="Browser for UI tests. By default tests run in Chrome and Firefox.",
    )


def pytest_generate_tests(metafunc: pytest.Metafunc) -> None:
    if "browser_name" in metafunc.fixturenames:
        selected_browser = metafunc.config.getoption("--browser")
        browsers = ["chrome", "firefox"] if selected_browser == "all" else [selected_browser]
        metafunc.parametrize("browser_name", browsers)


@pytest.fixture
def api_client() -> StellarApiClient:
    return StellarApiClient()


@pytest.fixture
def test_user(api_client: StellarApiClient) -> dict[str, str]:
    user = api_client.create_user()
    yield user
    api_client.delete_user(user["access_token"])


@pytest.fixture
def driver(browser_name: str):
    browser = WebdriverFactory.getWebdriver(browser_name)
    browser.set_window_size(1440, 1000)
    yield browser
    browser.quit()
