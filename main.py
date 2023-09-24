"""
a program to update the products
"""
from pathlib import Path
import pandas as pd
from argparse import ArgumentParser
from src.config_parser import config_parser
from src.woo_adapter import WooAdapter
from src.products import Products


def parse_args():
    parser = ArgumentParser()
    parser.add_argument("-a", "--action", required=True, dest="action")
    parser.add_argument("-i", "--internal-data-path", type=Path, required=False, dest="internals")
    parser.add_argument("-s", "--save-path", required=True, type=Path, dest="output")
    return parser.parse_args()


def convert_to_list(pd_frame):
    objs = []
    for index, row in pd_frame.iterrows():
        objs.append({
            "update": row["update"],
            "name": row["name"],
            "id": row["id"],
            "on_sale": row["on_sale"],
            "price": row["price"],
            "regular_price": row["regular_price"],
            "sku": row["sku"],
            "stock_quantity": row["stock_quantity"],
            "stock_status": row["stock_status"],
            "url": row["url"],
        })

    return objs


def main():
    """
    Main application function
    """
    args = parse_args()
    cfg = config_parser(Path("config.toml"))
    cfg_api = cfg.get('woocommerce-api')
    woo = WooAdapter(consumer_key=cfg_api.get('consumerKey'),
                     consumer_secret=cfg_api.get('consumerSecret'), )

    products_api = Products(woo)

    internal = args.internals.joinpath('products.xlsx')
    updated = args.output.joinpath('products.xlsx')

    if args.action == 'update':
        updated_df = pd.read_excel(str(updated))
        updated_rows = convert_to_list(updated_df)
        updated = [row for row in updated_rows if row.get('update', 0) != 0]
        products_api.update(updated)
    else:
        all_products = products_api.read_all()
        df = pd.DataFrame(data=all_products).T
        df = df.transpose()
        # df.to_excel(str(internal))
        df.to_excel(str(updated))


if __name__ == '__main__':
    main()
