from cmdchess.config import configurations


def get_configurations():
    lightsqr = configurations.lightsqr
    darksqr = configurations.darksqr
    whitepiece = configurations.whitepiece
    blackpiece = configurations.blackpiece
    symbols = configurations.symbols
    return lightsqr, darksqr, whitepiece, blackpiece, symbols
