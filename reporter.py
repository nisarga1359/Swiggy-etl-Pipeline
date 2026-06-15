import pandas as pd
import matplotlib 
matplotlib.use('Agg')  # Use non-interactive backend for server environments
from fpdf import FPDF
import matplotlib.pyplot as plt
import logging 
import os


logging.basicConfig(level=logging.INFO,
                   format='%(asctime)s - %(levelname)s - %(message)s')

def create_charts(city_df, restaurant_df, category_df, trend_df):
    logging.info("Creating charts...")

    # Chart 1 - City Revenue
    plt.figure(figsize=(10, 6))
    plt.barh(city_df['City'], city_df['Total_Revenue'], color='#FF6B35')
    plt.title('Top 10 Cities by Revenue', fontsize=14, fontweight='bold')
    plt.xlabel('Total Revenue (INR)')
    plt.tight_layout()
    plt.savefig('output/city_revenue.png', dpi=150)
    plt.close()
    logging.info("City revenue chart created!")


    # Chart 2 - Monthly Trend
    plt.figure(figsize=(12, 5))
    plt.plot(trend_df['Month'], trend_df['Total_Revenue'], 
             color='#2196F3', linewidth=2, marker='o')
    plt.title('Monthly Revenue Trend', fontsize=14, fontweight='bold')
    plt.xlabel('Month')
    plt.ylabel('Total Revenue (INR)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('output/monthly_trend.png', dpi=150)
    plt.close()
    logging.info("Monthly trend chart created!")

    

    # Chart 3 - Category Bar Chart
    top_categories = category_df.head(10)
    plt.figure(figsize=(12, 8))
    plt.barh(top_categories['Category'], 
             top_categories['Total_Orders'],
             color='#FF5722')
    plt.title('Orders by Category', fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.savefig('output/category_analysis.png', dpi=150)
    plt.close()
    logging.info("Category chart created!")

    # Chart 4 - Top Restaurants
    plt.figure(figsize=(10, 6))
    plt.barh(restaurant_df['Restaurant Name'], 
             restaurant_df['Total_Revenue'], 
             color='#4CAF50')
    plt.title('Top 10 Restaurants by Revenue', fontsize=14, fontweight='bold')
    plt.xlabel('Total Revenue (INR)')
    plt.tight_layout()
    plt.savefig('output/top_restaurants.png', dpi=150)
    plt.close()
    logging.info("Restaurant chart created!")
    
    return ['output/city_revenue.png', 'output/monthly_trend.png',
            'output/category_analysis.png', 'output/top_restaurants.png']




def build_pdf(chart_paths, city_df, restaurant_df):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    
    # Title Page
    pdf.add_page()
    pdf.set_font('Arial', 'B', 24)
    pdf.cell(0, 20, 'Swiggy Analytical Report', ln=True, align='C')
    pdf.set_font('Arial', '', 12)
    pdf.cell(0, 10, 'Weekly  Food Delivery Analytics', ln=True, align='C')
    logging.info("PDF title page created!")


    # Dynamic summary
    top_city = city_df.iloc[0]['City']
    top_restaurant = restaurant_df.iloc[0]['Restaurant Name']
    total_orders = city_df['Total_Orders'].sum()
    
    pdf.ln(20)
    pdf.set_font('Arial', 'B', 14)
    pdf.cell(0, 10, 'Report Summary', ln=True)
    pdf.set_font('Arial', '', 11)
    pdf.multi_cell(0, 8, f"""
This report provides weekly Swiggy food delivery performance analysis.

Key Highlights:
- {top_city} is the highest revenue generating city
- {top_restaurant} is the top performing restaurant  
- Total Orders analyzed: {total_orders:,}

Data Source: Swiggy Orders Database | Total Records: 1,97,403
    """)
    logging.info("PDF summary added!")

    # Add charts to PDF
    for chart_path in chart_paths:
        pdf.add_page()
        pdf.image(chart_path, x=10, y=30, w=190)
    
    # Save PDF
    pdf.output('output/Swiggy_Analytical_Report.pdf')
    logging.info("PDF saved successfully!")


def generate_report(city_df, restaurant_df, category_df, trend_df):
    chart_paths = create_charts(city_df, restaurant_df, category_df, trend_df)
    build_pdf(chart_paths, city_df, restaurant_df)
    logging.info("Report generated successfully!")