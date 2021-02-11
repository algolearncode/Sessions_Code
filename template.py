# zipline import
from zipline.pipeline.data import EquityPricing
from zipline.finance import slippage 
from zipline.api import (   symbol,
                            schedule_function,
                            date_rules,
                            time_rules,
                            order_percent,
                            order_target_percent,
                            get_open_orders,
                            cancel_order,
                            set_slippage)

# import pandas and numpy
import pandas as pd
import numpy as np

def initialize(context):

    # slippage model
    set_slippage(slippage.FixedSlippage(spread=0))

    # stock universe - list of tickers
    securities = ['AAPL', 'ADBE', 'AIG', 'AMGN', 'BA']
    # change string list of tickers into asset list using symbol function
    context.sec_symbols = [symbol(s) for s in securities]
    print(len(context.sec_symbols))

    # schedule functions
    schedule_function(trade_market_open, date_rules.every_day(), time_rules.market_open())
    schedule_function(cancel_open, date_rules.every_day(), time_rules.market_close())

def before_trading_start(context,data):
    pass

def trade_market_open(context,data):
    pass

def handle_data(context,data):
    pass

def cancel_open(context,data):
    oo = get_open_orders()
    for sec in oo:
        for order in oo[sec]:
            cancel_order(order.id)

