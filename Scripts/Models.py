
class SP500:
    """
    Simple Class to hold company financial data for one day to be written to DB
    """
    _symbol = ''
    _date = ""
    _open, _high, _low, _close = 0, 0, 0, 0
    _adj_close = 0
    _volume = 0


    def __init__(self, ticker, date):
        self._symbol = ticker
        self._date = date

    def fill_data(self, open, high, low, close, adj_close, volume):
        self._open = int(open)
        self._high = int(high)
        self._low = int(low)
        self._close = int(close)
        self._adj_close = int(adj_close)
        self._volume = int(volume)


    def export(self):
        return (self._date, self._open, self._high, self._low, self._close, self._adj_close, self._volume)
