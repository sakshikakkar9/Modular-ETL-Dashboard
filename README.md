# 🎬 Project Silver-Link: End-to-End Medallion Data Pipeline

**Project Silver-Link** is a modular Data Engineering and Business Intelligence (BI) project. It transforms raw, unorganized sales data into actionable business insights using a three-tier "Medallion" architecture, culminating in an interactive, AI-enhanced web dashboard.

---

## The Architecture (Medallion Flow)
This project follows the industry-standard Medallion Architecture to ensure data quality and reliability:

1.  **🥉 Bronze (Raw)**: Automated ingestion of source CSV files using resilient Python protocols.
2.  **🥈 Silver (Cleaned)**: Standardizes data types, handles date-time formatting (YYYY-MM), and enforces category naming conventions.
3.  **🥇 Gold (Curated)**: Aggregates high-level business metrics and chronological trend analysis ready for the UI layer.



---

## Key Features
* **Automated ETL Pipeline**: Fully scripted Python modules for Extract, Transform, and Load processes.
* **Chronological Trend Analysis**: Time-series visualization tracking business performance across years/months.
* **AI-Powered Sales Assistant**: A built-in retrieval agent in the dashboard for natural language data querying.
* **Zero-Dependency Logic**: Custom-built CSV handling to ensure high performance even in low-resource environments.

---

## Tech Stack
* **Language**: Python 3.x
* **Frontend/UI**: Streamlit
* **Data Processing**: Standard CSV & Datetime Libraries (NumPy/Pandas compatible)
* **Environment**: Anaconda / Kaggle Notebooks

---

## Project Structure
```text
Data_Movie_Project/
├── data/
│   ├── bronze/          # Original, raw CSV files
│   ├── silver/          # Cleaned, standardized data
│   └── gold/            # Aggregated reports (Trend & Totals)
├── src/
│   ├── 1_bronze.py      # Ingestion script
│   ├── 2_silver.py      # Cleaning & formatting script
│   └── 3_gold.py        # Business logic & aggregation
├── dashboard.py         # Streamlit Web Application
└── requirements.txt     # Python dependencies
