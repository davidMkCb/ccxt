from ccxt.base.types import Entry


class ImplicitAPI:
    public_get_market_instruments = publicGetMarketInstruments = Entry('market/instruments', 'public', 'GET', {'cost': 1})
    public_get_market_tickers = publicGetMarketTickers = Entry('market/tickers', 'public', 'GET', {'cost': 1})
    public_get_market_books = publicGetMarketBooks = Entry('market/books', 'public', 'GET', {'cost': 1})
    public_get_market_trades = publicGetMarketTrades = Entry('market/trades', 'public', 'GET', {'cost': 1})
    public_get_market_candles = publicGetMarketCandles = Entry('market/candles', 'public', 'GET', {'cost': 1})
    public_get_market_mark_price = publicGetMarketMarkPrice = Entry('market/mark-price', 'public', 'GET', {'cost': 1})
    public_get_market_funding_rate = publicGetMarketFundingRate = Entry('market/funding-rate', 'public', 'GET', {'cost': 1})
    public_get_market_funding_rate_history = publicGetMarketFundingRateHistory = Entry('market/funding-rate-history', 'public', 'GET', {'cost': 1})
    private_get_asset_balances = privateGetAssetBalances = Entry('asset/balances', 'private', 'GET', {'cost': 1})
    private_get_trade_orders_pending = privateGetTradeOrdersPending = Entry('trade/orders-pending', 'private', 'GET', {'cost': 1})
    private_get_trade_fills_history = privateGetTradeFillsHistory = Entry('trade/fills-history', 'private', 'GET', {'cost': 1})
    private_get_asset_deposit_history = privateGetAssetDepositHistory = Entry('asset/deposit-history', 'private', 'GET', {'cost': 1})
    private_get_asset_withdrawal_history = privateGetAssetWithdrawalHistory = Entry('asset/withdrawal-history', 'private', 'GET', {'cost': 1})
    private_get_asset_bills = privateGetAssetBills = Entry('asset/bills', 'private', 'GET', {'cost': 1})
    private_get_account_balance = privateGetAccountBalance = Entry('account/balance', 'private', 'GET', {'cost': 1})
    private_get_account_positions = privateGetAccountPositions = Entry('account/positions', 'private', 'GET', {'cost': 1})
    private_get_account_leverage_info = privateGetAccountLeverageInfo = Entry('account/leverage-info', 'private', 'GET', {'cost': 1})
    private_get_account_batch_leverage_info = privateGetAccountBatchLeverageInfo = Entry('account/batch-leverage-info', 'private', 'GET', {'cost': 1})
    private_get_trade_orders_tpsl_pending = privateGetTradeOrdersTpslPending = Entry('trade/orders-tpsl-pending', 'private', 'GET', {'cost': 1})
    private_get_trade_orders_history = privateGetTradeOrdersHistory = Entry('trade/orders-history', 'private', 'GET', {'cost': 1})
    private_get_trade_orders_tpsl_history = privateGetTradeOrdersTpslHistory = Entry('trade/orders-tpsl-history', 'private', 'GET', {'cost': 1})
    private_post_trade_order = privatePostTradeOrder = Entry('trade/order', 'private', 'POST', {'cost': 1})
    private_post_trade_cancel_order = privatePostTradeCancelOrder = Entry('trade/cancel-order', 'private', 'POST', {'cost': 1})
    private_post_account_set_leverage = privatePostAccountSetLeverage = Entry('account/set-leverage', 'private', 'POST', {'cost': 1})
    private_post_trade_batch_orders = privatePostTradeBatchOrders = Entry('trade/batch-orders', 'private', 'POST', {'cost': 1})
    private_post_trade_order_tpsl = privatePostTradeOrderTpsl = Entry('trade/order-tpsl', 'private', 'POST', {'cost': 1})
    private_post_trade_cancel_batch_orders = privatePostTradeCancelBatchOrders = Entry('trade/cancel-batch-orders', 'private', 'POST', {'cost': 1})
    private_post_trade_cancel_tpsl = privatePostTradeCancelTpsl = Entry('trade/cancel-tpsl', 'private', 'POST', {'cost': 1})
    private_post_trade_close_position = privatePostTradeClosePosition = Entry('trade/close-position', 'private', 'POST', {'cost': 1})
    private_post_asset_transfer = privatePostAssetTransfer = Entry('asset/transfer', 'private', 'POST', {'cost': 1})
