import sys

from binance_utils import *
from logger import log


def get_symbol_price(symbol):
    return float(send_public_request('ticker/price', {'symbol': symbol})['price'])


def get_open_orders(symbol):
    return send_signed_request('GET', 'openOrders', {'symbol': symbol})


def get_free_balance_of(coin):
    return float(
        list(
            filter(
                lambda balance: balance['asset'] == coin, send_signed_request('GET', 'account', {})['balances'])
        )[0]['free']
    )


def create_sell_order(price_to_sell_with, coin_to_buy, symbol):
    coin_to_buy_balance = get_free_balance_of(coin_to_buy)

    res = send_signed_request('POST', 'order', {
        'symbol': symbol,
        'side': 'sell',
        'type': 'limit',
        'quantity': "%.5f" % coin_to_buy_balance,
        'price': "%.5f" % price_to_sell_with,
        'timeInForce': 'GTC'
    })

    # Got an error from Binance API
    if 'code' in res:
        log(res)
        sys.exit(1)

    log('Created sell order ' + str(coin_to_buy_balance) + ' with price ' + str(price_to_sell_with))


def create_buy_order(coin_to_buy, coin_to_sell, symbol, money_to_spend):
    current_price = get_symbol_price(symbol)
    qty_to_buy = money_to_spend / current_price
    qty_to_buy = "%.5f" % qty_to_buy
    response = send_signed_request('POST', 'order',
                                   {'symbol': symbol, 'side': 'buy', 'type': 'market', 'quantity': qty_to_buy})

    bought_with_price = float(response['fills'][0]['price'])
    qty_bought = response['fills'][0]['qty']

    log('Bought ' + str(qty_bought) + ' ' + coin_to_buy + ' on '
        + str(response['cummulativeQuoteQty'])
        + ' ' + coin_to_sell + ' with '
        + str(bought_with_price) + ' price')

    price_to_sell_with = bought_with_price + 0.8
    create_sell_order(price_to_sell_with, coin_to_buy, symbol)
