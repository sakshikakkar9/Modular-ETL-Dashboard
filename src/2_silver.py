import csv
import os
from datetime import datetime

bronze_path = 'data/bronze/raw_data.csv'
silver_path = 'data/silver/clean_data.csv'

if not os.path.exists('data/silver'):
    os.makedirs('data/silver')

print("🧪 Refining Silver Layer: Standardizing Dates...")

try:
    with open(bronze_path, mode='r', encoding='utf-8-sig') as infile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames + ['Year-Month'] # Adding our new column
        
        with open(silver_path, mode='w', newline='', encoding='utf-8') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            
            clean_count = 0
            for row in reader:
                if row.get('Order ID'):
                    # --- DATE FORMATTING LOGIC ---
                    raw_date = row.get('Order Date', '')
                    try:
                        # Try common formats (MM/DD/YYYY or DD-MM-YYYY)
                        for fmt in ("%m/%d/%Y", "%d-%m-%Y", "%Y-%m-%d"):
                            try:
                                dt_obj = datetime.strptime(raw_date, fmt)
                                # Create a sortable format: 2024-01, 2024-02
                                row['Year-Month'] = dt_obj.strftime('%Y-%m')
                                break
                            except ValueError:
                                continue
                    except:
                        row['Year-Month'] = "Unknown"

                    # Standardize Category
                    if 'Category' in row and row['Category']:
                        row['Category'] = row['Category'].strip().title()
                    
                    writer.writerow(row)
                    clean_count += 1
                    
    print(f"✅ Success: {clean_count} rows cleaned with chronological dates!")

except Exception as e:
    print(f"❌ Error during cleaning: {e}")