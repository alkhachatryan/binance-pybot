import argparse

parser = argparse.ArgumentParser(
    prog='BinancePyBot',
    description='A simple binance trading bot'
)

parser.add_argument('-b', '--buy', required=True)
parser.add_argument('-s', '--sell', required=True)
cli_args = parser.parse_args()
