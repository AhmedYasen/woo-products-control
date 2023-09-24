"""

"""


def _get_required_info(product):
    return {
        "update": 0,
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


def _updated_product(product):
    return {
        "price": product["price"],
        "regular_price": product["regular_price"],
        "stock_quantity": product["stock_quantity"],
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
        PER_PAGE = 100
        total_pages = int(self._api.head("products", params={"per_page": PER_PAGE}).get("X-WP-TotalPages"))
        all_products = []

        for page in range(total_pages):
            print("Reading page: ", page + 1)
            products = self._api.get("products", params={"per_page": PER_PAGE, "page": page + 1})
            all_products += products

        all_products = [_get_required_info(product) for product in all_products]
        return all_products

    def update(self, updated_products):
        """
        Update all new values on the website
        """
        for product in updated_products:
            prod_id = int(product["id"])
            prod = _updated_product(product)
            resp = self._api.put(f"products/{prod_id}", {'price': 3})
            print("Updated product: ", prod)
            print("Update Status: ", resp)
