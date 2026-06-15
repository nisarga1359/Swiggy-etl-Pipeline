# 🍊 Swiggy Automated ETL Pipeline

An end-to-end automated data pipeline built using Python that extracts, cleans, analyzes, and reports on Swiggy food delivery data (197,000+ records).

---

## 🛠️ Tech Stack
- **Python** (pandas, matplotlib, fpdf2, mysql-connector)
- **MySQL** – data storage and querying
- **Matplotlib** – data visualization
- **FPDF2** – automated PDF report generation

---

## 📁 Project Structure

| File | Description |
|------|-------------|
| `cleaner.py` | Handles missing values, duplicates, and data type fixes |
| `db_loader.py` | Loads cleaned data into MySQL database |
| `analyzer.py` | Performs exploratory data analysis and generates insights |
| `reporter.py` | Auto-generates a PDF report with charts and summaries |
| `emailer.py` | Sends the report via email automatically |
| `main.py` | Orchestrates the full pipeline end to end |

---

## 🔄 Pipeline Flow

Raw CSV → Clean Data → MySQL DB → Analysis → PDF Report → Email

---

## 💡 Key Features
- Automated cleaning of 197,000+ Swiggy records
- MySQL integration for structured storage
- Visual insights using Matplotlib
- Auto-generated PDF reports
- Email automation for report delivery

---

## 👩‍💻 Author
**Nisarga** 
