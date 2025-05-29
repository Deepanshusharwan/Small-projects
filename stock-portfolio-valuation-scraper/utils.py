from tabulate import tabulate
from bs4 import BeautifulSoup
from dataclasses import dataclass
import requests
# This script scrapes the stock info from google-stock exchange and then presents it in a table format 

def main():
    price_getter()


@dataclass
class Stock:
    ticker: str
    exchange: str
    quantity: int
    price: float = 0
    market_value: float = 0

    def __post_init__(self):
        self.ticker = self.ticker.upper()
        self.exchange = self.exchange.upper()
        self.price = price_getter(self.ticker,self.exchange)
        self.market_value = self.price * self.quantity


@dataclass
class Portfolio:
    positions: list[Stock]

    def get_total_value(self):
        total_portfolio_value = 0
        for position in self.positions:
            total_portfolio_value += position.market_value
        return total_portfolio_value
    
    def print_table(self,table_format="rounded_grid"):
        total_portfolio_value = self.get_total_value()
        position_data = [
            [
                stock.ticker,
                stock.exchange,
                stock.quantity,
                f"${stock.price:.2f}",
                f"${stock.market_value:.2f}", 
                f"{(stock.market_value / total_portfolio_value) * 100:.2f}%"  
            ]
            for stock in self.positions
        ]

        print(tabulate(position_data,headers=["Ticker","Exchange","Quantity","Price","Market Value","% Allocation"],tablefmt=table_format))


def price_getter(ticker,exchange):
    url = f'https://www.google.com/finance/quote/{ticker.upper()}:{exchange.upper()}'
    soup = BeautifulSoup(requests.get(url).content,'html.parser')
    price_div = soup.find('div',attrs={"data-last-price": True})
    price = float(price_div.get('data-last-price',"Couldn't get the price."))
    data_currency_code = price_div.get('data-currency-code')

    if data_currency_code != "USD":
        price = change_currency_to_dollar(data_currency_code,price)

    return price


def change_currency_to_dollar(currency_code,amount):
    url = f'https://www.google.com/finance/quote/{currency_code}-USD'
    soup = BeautifulSoup(requests.get(url).content,'html.parser')
    currency_exhange_rate = float(soup.find('div',attrs={"data-last-price":True}).get("data-last-price"))
    new_price = currency_exhange_rate * amount
    return round(new_price,2)

# Make Stock objects and then list them while initializing the Portfolio class
#bns = Stock('bns','tse',100)
#googl = Stock('googl','nasdaq',30)
#shop = Stock('shop','tse',10)
#msft = Stock('msft','nasdaq',2)

#portfolio = Portfolio([bns,
#                       googl,
#                       shop,
#                       msft])
#
#portfolio.print_table()
#print(f"Total portfolio value: ${portfolio.get_total_value():,.2f}.")


