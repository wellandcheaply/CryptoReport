import requests as rq 
import json

# all USD-to-<SomeCoin> exchanges currently supported on Bittrex
usd_markets = {'BTC': 'Bitcoin',
                'ETH': 'Ethereum',
                'BCC': 'Bitcoin Cash',
                'ADA': 'Cardano',
                'TUSD': 'Tether',
                'LTC': 'Litecoin',
                'XRP': 'Ripple',
                'ETC': 'Ethereum Classic',
                'DASH': 'Dash',
                'XMR': 'Monero',
                'NEO': 'NEO',
                'OMG': 'OmiseGo',
                'ZEC': 'Z-Cash',
                'BTG': 'Bitcoin Gold',
                'TRX': 'Tron',
                'XVG': 'Verge',
                'SC': 'Siacoin',
                'NXT': 'Nxt',
                }

'''
call with no params to get names in Ticker form
call with any True value to get the 'actual names' of the coins.
'''
def trexUS(names_not_tickers=False):
	for market in usd_markets:
		price = rq.get('https://bittrex.com/api/v1.1/public/getticker?market=USDT-'+market
			).json()['result']['Last']
		if names_not_tickers:
			print('{}:	${}'.format(usd_markets[market], price))
		else:
			print('{}:	${}'.format(market, price))
