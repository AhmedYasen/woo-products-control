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
        send get request
        """
        return self._api.get(endpoint=endpoint, params=params).json()

    def put(self, endpoint, data):
        """
        send update request
        """
        return self._api.put(endpoint, data).json()

    def post(self, endpoint, data):
        """
        send post request
        """
        return self._api.post(endpoint, data).json()
    
    def head(self, endpoint, params=None):
        """
        Get Header information for endpoint
        """
        return self._api.get(endpoint=endpoint, params=params).headers
