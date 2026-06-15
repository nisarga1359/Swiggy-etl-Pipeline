from cleaner import load_data, clean_data
from db_loader import connect_to_db, load_to_db
from analyzer import get_city_revenue, get_top_restaurants, get_category_analysis, get_monthly_trend
from reporter import generate_report
from emailer import send_email
import schedule
import time
import logging



logging.basicConfig(level=logging.INFO,
                   format='%(asctime)s - %(levelname)s - %(message)s')

def run_pipeline():
    logging.info("Swiggy Pipeline Started!")
    
    # Step 1 - Load and clean data
    df = load_data('data/swiggy_data.xlsx')
    if df is None:
        logging.error("Pipeline stopped - file not found!")
        return
    df = clean_data(df)
    
    # Step 2 - Connect to MySQL and load data
    engine = connect_to_db()
    load_to_db(df, engine)
    
    # Step 3 - Get insights from MySQL
    city_df = get_city_revenue(engine)
    restaurant_df = get_top_restaurants(engine)
    category_df = get_category_analysis(engine)
    trend_df = get_monthly_trend(engine)
    
    # Step 4 - Generate PDF report
    generate_report(city_df, restaurant_df, category_df, trend_df)
    
    # Step 5 - Send email
    send_email(
        sender_email='nisargagouday@gmail.com',
        sender_password='okumsmnpymjhzfta',
        receiver_email='sanjana91407@gmail.com',
        pdf_path='output/Swiggy_Analytical_Report.pdf'
    )
    
    logging.info("Pipeline completed successfully!")


# Run once immediately
run_pipeline()

# Schedule every Monday
schedule.every().monday.at("08:00").do(run_pipeline)

logging.info("Scheduler started - runs every Monday 8AM!")

while True:
    schedule.run_pending()
    time.sleep(60)