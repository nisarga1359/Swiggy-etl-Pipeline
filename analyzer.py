import pandas as pd
import logging


logging.basicConfig(level=logging.INFO,
                   format='%(asctime)s - %(levelname)s - %(message)s')

def get_city_revenue(engine):
    query = """
        SELECT City, 
               ROUND(SUM(`Price (INR)`), 2) as Total_Revenue,
               COUNT(*) as Total_Orders
        FROM swiggy_orders
        GROUP BY City
        ORDER BY Total_Revenue DESC
        LIMIT 10;
    """
    df = pd.read_sql(query, engine)
    logging.info("City revenue data fetched!")
    return df

def get_top_restaurants(engine):
    query = """
        SELECT `Restaurant Name`,
               City,
               ROUND(SUM(`Price (INR)`), 2) as Total_Revenue,
               ROUND(AVG(Rating), 2) as Avg_Rating
        FROM swiggy_orders
        GROUP BY `Restaurant Name`, City
        ORDER BY Total_Revenue DESC
        LIMIT 10;
    """
    df = pd.read_sql(query, engine)
    logging.info("Top restaurants data fetched!")
    return df


def get_category_analysis(engine):
    query = """
        SELECT Category,
               ROUND(SUM(`Price (INR)`), 2) as Total_Revenue,
               COUNT(*) as Total_Orders,
               ROUND(AVG(`Price (INR)`), 2) as Avg_Price
        FROM swiggy_orders
        GROUP BY Category
        ORDER BY Total_Orders DESC;
    """
    df = pd.read_sql(query, engine)
    logging.info("Category analysis data fetched!")
    return df


def get_monthly_trend(engine):
    query = """
        SELECT 
            DATE_FORMAT(`Order Date`, '%%Y-%%m') as Month,
            ROUND(SUM(`Price (INR)`), 2) as Total_Revenue,
            COUNT(*) as Total_Orders
        FROM swiggy_orders
        GROUP BY Month
        ORDER BY Month ASC;
    """
    df = pd.read_sql(query, engine)
    logging.info("Monthly trend data fetched!")
    return df