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

    send_signed_request('POST', 'order', {
        'symbol': symbol,
        'side': 'sell',
        'type': 'limit',
        'quantity': coin_to_buy_balance,
        'price': price_to_sell_with,
        'timeInForce': 'GTC'
    })
    log('Created sell order ' + str(coin_to_buy_balance) + ' with price ' + str(price_to_sell_with))


def create_buy_order(coin_to_buy, coin_to_sell, symbol):
    coin_to_sell_balance = get_free_balance_of(coin_to_sell)

    # In case if you sell USDT to buy another coin, transaction price should be more than $10
    if coin_to_sell == 'USDT' and coin_to_sell_balance <= 10:
        log('Not enough resources: ' + str(coin_to_sell_balance))

    log('Current balance: ' + str(coin_to_sell_balance) + coin_to_sell)
    current_price = get_symbol_price(symbol)
    money_to_spend = coin_to_sell_balance / 2
    qty_to_buy = money_to_spend / current_price
    qty_to_buy = "%.5f" % qty_to_buy
    response = send_signed_request('POST', 'order', {'symbol': symbol, 'side': 'buy', 'type': 'market', 'quantity': qty_to_buy})

    bought_with_price = float(response['fills'][0]['price'])
    qty_bought = response['fills'][0]['qty']

    log('Bought ' + str(qty_bought) + ' ' + coin_to_buy + ' on '
        + str(response['cummulativeQuoteQty'])
        + ' ' + coin_to_sell + ' with '
        + str(bought_with_price) + ' price')

    price_to_sell_with = bought_with_price + 0.8
    create_sell_order(price_to_sell_with, coin_to_buy, symbol)
