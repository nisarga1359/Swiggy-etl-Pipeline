import pandas as pd
import os
import logging

logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def load_data(filepath):
    if not os.path.exists(filepath):
        logging.error(f"File {filepath} does not exist.")
        return None
    
    df = pd.read_excel(filepath)
    logging.info(f"Data loaded successfully! Shape: {df.shape}")
    return df

def clean_data(df):
    before = len(df)
    logging.info(f"Initial number of rows: {before}")
    df = df.drop_duplicates()
    logging.info(f"Number of rows after dropping duplicates: {before - len(df)} rows dropped")
    
    # Fix date column
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    logging.info("Order Date converted to datetime!")

    # Fix text columns
    df['Restaurant Name'] = df['Restaurant Name'].str.strip().str.title()
    df['City'] = df['City'].str.strip().str.title()
    df['Category'] = df['Category'].str.strip().str.title()
    logging.info("Text columns cleaned!")

    df = df[df['Price (INR)'] > 0]
    logging.info("Invalid prices removed!")

    after = len(df)
    logging.info(f'Cleaning Complete! Rows before: {before}, Rows after: {after}')
    return df