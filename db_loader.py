import pandas as pd
import logging
from sqlalchemy import create_engine

logging.basicConfig(level=logging.INFO,
                   format='%(asctime)s - %(levelname)s - %(message)s')


def connect_to_db():
    engine = create_engine('mysql+pymysql://root:nisarga1709@localhost/swiggybi')
    logging.info("Connected to MySQL database!")
    return engine

def load_to_db(df, engine):
    df.to_sql('swiggy_orders', con=engine, if_exists='replace', index=False)
    logging.info("Data loaded to MySQL successfully!")

    