import shutil
import os

# 1. Define paths
source_file = 'input_data.csv'
destination = 'data/bronze/raw_data.csv'

# 2. Use SHUTIL instead of PANDAS (No NumPy needed!)
try:
    if not os.path.exists('data/bronze'):
        os.makedirs('data/bronze')
        
    shutil.copy(source_file, destination)
    print("✅ Success: Raw data copied to Bronze using Shutil (No NumPy error!)")
except Exception as e:
    print(f"❌ Error: {e}")