"""
a program to update the products
"""
from pathlib import Path
from src.config_parser import config_parser
from src.woo_adapter import WooAdapter
from src.products import Products
import pandas as pd
def main():
    """
    Main application function
    """
    cfg = config_parser(Path("config.toml"))
    cfg_api = cfg.get('woocommerce-api')
    print(cfg_api.get('consumerKey'), cfg_api.get('consumerSecret'))
    woo = WooAdapter(consumer_key=cfg_api.get('consumerKey'),
                     consumer_secret=cfg_api.get('consumerSecret'),)
    
    products_api = Products(woo)
    all_products = products_api.read_all()
    df = pd.DataFrame(data=all_products).T
    df.to_excel('products.xlsx')


if __name__ == '__main__':
    main()
