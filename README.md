
# Binance Pybot

A simple bot for a trading on Binance with a simple algorithm.

![image](https://user-images.githubusercontent.com/22774727/202932524-2967f43d-14fa-4e0f-8f75-0056d7f7e05e.png)


## Philosophy 
I decided to start trading on Binance with BTC (or something similar) + USDT. Since I am new to trading and the financial market, I decided to start trading with a simple algorithm: buy BTC (or whatever) at X price and then immediately sell it at X + a few cents price. Since there is no commission on BTCUSDT, this algorithm works like a charm. But doing it manually will take a lot of time and effort, so I decided to make a bot that will do it for me. The only risk of trading with this algorithm is that the bot (or you) will buy BTC for, say, $16,600 and the price will immediately fall below $16,600 forever :)
But as it's a Binance and BTC, the price grows up and falls down very fast in milliseconds and there is a real profit.

## Algorithm and the way bot works
The bot connects to the Binance with API key and secret you provide, checks the USDT (or whatever you want to sell) balance you have, then buys BTC(or whatever you want). The bot buys BTC with market price on 50% of your balance, that means it will not create a buy order but instead buy BTC immediatelly with current price. Then adds 80 cents and creates an order to sell.

For example: you have $30 and one BTC price is $16.000. The bot will buy BTC on $15 with price $16.000 and immediatelly create a sell order to sell BTC you just bought with price $16.000 + 0.80 = $16.000,80
After this transaction you will have $30.00075.
As the price grows up and falls down very fast, the orders creations take seconds or milliseconds. And since this algorithm is a geometric progression, you will have more cents in the near future :D

But there can be one sad thing: you buy with $16.000 and create an order to sell with $16.000,80 and at that moment BTC price falls down to, let's say, $15.900 and keeps to be on it for an hours. No need to panic, it's very possible the price will be back to $16.000+

## Hours of testing
I ran this script about 48 hours and: it traded with my USDT balance $95 and after 48 hours my balance became about $99. Little, but strong growth. Some sell orders took milliseconds to finish, some of them hours.
So I believe this bot can make some cents on your passive balance. **But use it at your own risk.**


## Installation

Clone, venv, pip install, env conf

```bash
  git clone git@github.com:alkhachatryan/binance-pybot.git
  
  cd binance-pybot
  
  virtualenv venv # create your virtual env

  pip install -r requirements.txt

  cp .env.example .env # and then fill your binance api key and secret, no need to change base url
```

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`BINANCE_API_KEY`

`BINANCE_API_SECRET`

To get them:

- Go to https://www.binance.com/en/my/settings/api-management
- Create an API
- Edit API restriction and Enable Spot & Margin Trading option
- You also can restrict access to trusted IPs, but in case if you have dynamic IP - this will provide problems
- Get and use your KEY and SECRET API keys
## Usage

```bash
python main.py --buy=BTC --sell=USDT
```


## Logging
Everything is printed on console also append to log file, which can be found at /logs. The file name is current date, so you can debug the code and monitor your transactions with ease
## Contributing

Contributions are always welcome!
Feel free to open your PR with fixes and new features/trading algos


## License

[MIT](https://github.com/alkhachatryan/binance-pybot/blob/master/LICENCE.md)


## Appendix

This is for personal usage only. The author is not responsible for the use of this script. **Use it at your own risk.**

