#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cli_args_parser import cli_args
from func import *

current_balance = 0


def trade(coin_to_buy, coin_to_sell):
    global current_balance
    symbol = coin_to_buy + coin_to_sell

    while True:
        no_open_order = len(get_open_orders(symbol)) == 0

        if no_open_order:
            # After hours of tests the best limitation in second between orders creations
            time.sleep(2)

            coin_to_sell_balance = get_free_balance_of(coin_to_sell)

            # Sometimes Binance API doesn't provide a correct balance after completed order
            # When your order completed Binance shows old balance
            # In that case wait additional second before continuing the trading process
            if current_balance > coin_to_sell_balance:
                log('Old balance returned from API, waiting a second')
                time.sleep(1)
                return trade(coin_to_buy, coin_to_sell)

            current_balance = coin_to_sell_balance

            # In case if you sell USDT to buy another coin, transaction price should be more than $10
            if coin_to_sell == 'USDT' and coin_to_sell_balance <= 10:
                log('Not enough resources: ' + str(coin_to_sell_balance))

            log('Current balance: ' + str(coin_to_sell_balance) + coin_to_sell)
            money_to_spend = coin_to_sell_balance / 2

            create_buy_order(coin_to_buy, coin_to_sell, symbol, money_to_spend)


def main():
    coin_to_buy = cli_args.buy.upper()
    coin_to_sell = cli_args.sell.upper()
    trade(coin_to_buy, coin_to_sell)
    return 0


if __name__ == "__main__":
    main()
