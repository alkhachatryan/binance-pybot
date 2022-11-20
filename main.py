#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cli_args_parser import cli_args
from func import *


def trade(coin_to_buy, coin_to_sell):
    symbol = coin_to_buy + coin_to_sell

    while True:
        no_open_order = len(get_open_orders(symbol)) == 0

        # After hours of tests the best limitation in second between orders creations
        time.sleep(4)

        if no_open_order:
            create_buy_order(coin_to_buy, coin_to_sell, symbol)


def main():
    coin_to_buy = cli_args.buy.upper()
    coin_to_sell = cli_args.sell.upper()
    trade(coin_to_buy, coin_to_sell)
    return 0


if __name__ == "__main__":
    main()
