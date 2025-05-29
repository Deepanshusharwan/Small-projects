from utils import Stock, Portfolio

# Make Stock objects and then list them while initializing the Portfolio class
bns = Stock('bns','tse',100)
googl = Stock('googl','nasdaq',30)
shop = Stock('shop','tse',10)
msft = Stock('msft','nasdaq',2)

portfolio = Portfolio([bns,
                       googl,
                       shop,
                       msft])

portfolio.print_table()
print(f"Total portfolio value: ${portfolio.get_total_value():,.2f}.")


