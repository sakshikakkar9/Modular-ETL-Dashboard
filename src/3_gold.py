import csv
import os

silver_path = 'data/silver/clean_data.csv'
gold_total_path = 'data/gold/total_sales_report.csv'
gold_trend_path = 'data/gold/sales_trend_report.csv'

trend_data = {}

try:
    with open(silver_path, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            cat = row['Category']
            month = row['Year-Month']
            amount = float(row.get('Amount', 0))
            
            key = (cat, month)
            trend_data[key] = trend_data.get(key, 0) + amount

    # SORTING: This ensures 2024-01 comes before 2024-02
    sorted_trend = sorted(trend_data.items(), key=lambda x: (x[0][0], x[0][1]))

    with open(gold_trend_path, mode='w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(['Category', 'Month', 'Total_Sales'])
        for (cat, month), total in sorted_trend:
            writer.writerow([cat, month, round(total, 2)])
            
    print("✅ Success: Gold Trend Report is now sorted chronologically!")

except Exception as e:
    print(f"❌ Error: {e}")