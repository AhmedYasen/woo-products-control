"""

"""


def _get_required_info(product):
    return {
        "update": 0,
        "name": product["name"],
        "id": product["id"],
        "on_sale": product["on_sale"],
        "sale_price": product["sale_price"],
        "regular_price": product["regular_price"],
        "sku": product["sku"],
        "stock_quantity": product["stock_quantity"],
        "stock_status": product["stock_status"],
        "url": product["_links"]["self"][0]["href"],
    }


def _updated_product(product):
    return {
        "sale_price": str(product['sale_price']),
        "regular_price": str(product["regular_price"]),
        "stock_quantity": str(product["stock_quantity"]),
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

    def update(self, updated_products, log_file=None):
        """
        Update all new values on the website
        """
        if log_file is not None:
            log_file = log_file.open('a')

        for product in updated_products:
            prod_id = int(product["id"])
            prod = _updated_product(product)
            ep = str(f"products/{prod_id}")
            resp = self._api.put(ep, prod)
            if prod_id == int(resp["id"]):
                print("Updated product: ", prod_id)
                log_file.write(f"Updated product: {prod_id}\n") if log_file else None
            else:
                print(f"Product with id {prod_id} not updated")
                log_file.write(f"Updated product: {prod_id}\n") if log_file else None
