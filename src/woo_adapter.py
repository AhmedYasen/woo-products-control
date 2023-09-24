"""
woocommerce adapter
"""
from woocommerce import API

class WooAdapter:
    """
    wrap woocommerce api
    """
    def __init__(self, consumer_key: str, consumer_secret: str) -> None:
        self._api = API(
            url="https://100habbah.com",
            consumer_key=consumer_key,
            consumer_secret=consumer_secret,
            version="wc/v3"
        )

    def get(self, endpoint, params=None):
        """
        List all products
        """
        return self._api.get(endpoint=endpoint, params=params).json()
