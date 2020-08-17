import pytest
from colorama import Back, Fore
from cmdchess.config import Config, UNICODE


@pytest.fixture
def config():
    return Config(
        Back.WHITE,
        Back.YELLOW,
        Fore.LIGHTWHITE_EX,
        Fore.LIGHTBLACK_EX,
        UNICODE
    )


def test_initialize(config):
    assert config.lightsqr == Back.WHITE
    assert config.darksqr == Back.YELLOW
    assert config.whitepiece == Fore.LIGHTWHITE_EX
    assert config.blackpiece == Fore.LIGHTBLACK_EX
    assert config.symbols == UNICODE
