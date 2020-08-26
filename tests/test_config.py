import pytest
from colorama import Back, Fore
from cmdchess.config import Config, UNICODE, configurations
from ._mock_config import get_configurations


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
    assert config is not None


def test_properties_getter(config):
    config = Config(
        Back.WHITE,
        Back.YELLOW,
        Fore.LIGHTWHITE_EX,
        Fore.LIGHTBLACK_EX,
        UNICODE
    )

    assert config.lightsqr == Back.WHITE
    assert config.darksqr == Back.YELLOW
    assert config.whitepiece == Fore.LIGHTWHITE_EX
    assert config.blackpiece == Fore.LIGHTBLACK_EX
    assert config.symbols == UNICODE


def test_properties_setter(config):
    config.lightsqr = 'NEW LIGHTSQR'
    config.darksqr = 'NEW DARKSQR'
    config.whitepiece = 'NEW WHITEPIECE'
    config.blackpiece = 'NEW BLACKPIECE'
    config.symbols = 'NEW SYMBOLS'

    assert 'NEW LIGHTSQR' == config.lightsqr
    assert 'NEW DARKSQR' == config.darksqr
    assert 'NEW WHITEPIECE' == config.whitepiece
    assert 'NEW BLACKPIECE' == config.blackpiece
    assert 'NEW SYMBOLS' == config.symbols


def test_config_acrros_files():
    default_lightsqr, default_darksqr, default_whitepiece, default_blackpiece, default_symbols = get_configurations()

    configurations.lightsqr = 'NEW LIGHTSQR'
    configurations.darksqr = 'NEW DARKSQR'
    configurations.whitepiece = 'NEW WHITEPIECE'
    configurations.blackpiece = 'NEW BLACKPIECE'
    configurations.symbols = 'NEW SYMBOLS'

    new_lightsqr, new_darksqr, new_whitepiece, new_blackpiece, new_symbols = get_configurations()

    assert default_lightsqr != new_lightsqr
    assert default_darksqr != new_darksqr
    assert default_whitepiece != new_whitepiece
    assert default_blackpiece != new_blackpiece
    assert default_symbols != new_symbols

    assert 'NEW LIGHTSQR' == new_lightsqr
    assert 'NEW DARKSQR' == new_darksqr
    assert 'NEW WHITEPIECE' == new_whitepiece
    assert 'NEW BLACKPIECE' == new_blackpiece
    assert 'NEW SYMBOLS' == new_symbols
