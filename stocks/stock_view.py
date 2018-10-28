"""
creates a string from a StockModel
Note: this class does NOT have a constructor
"""


class StockView:

    def params(self, model):
        """
        Extracts items from StockModel that are needed for rendering.


        :param model:  an instance of StockModel
        :return: dict: selected StockModel values
        """

        # get recommendation
        if model.is_bullish():
            sentiment = 'Bullish'
        else:
            sentiment = 'Bearish'

        return {
            'name': model.symbol,
            'price': model.close_price,
            'sentiment': sentiment,
        }

    def render(self, model):
        """
        Creates a formatted string for a text renderer

        :param model:
        :return:
        """

        params = self.params(model)
        return '{name}: ${price:0.2f} ({sentiment})'.format_map(params)
