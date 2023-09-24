"""

"""

def _get_required_info(product):
    return {
        "name": product["name"],
        "id": product["id"],
        "on_sale": product["on_sale"],
        "price": product["price"],
        "regular_price": product["regular_price"],
        "sku": product["sku"],
        "stock_quantity": product["stock_quantity"],
        "stock_status": product["stock_status"],
        "url": product["_links"]["self"][0]["href"],
    }

class Products:
    """
    Products api handling
    """
    def __init__(self, wcapi) -> None:
        self._api = wcapi

    def read_all(self):
        """
        Read all products
        """
        all_products = self._api.get("products")
        all_products = [_get_required_info(product) for product in all_products]
        print(all_products)
        return all_products

    def update(self):
        pass
