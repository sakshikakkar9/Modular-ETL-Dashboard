import streamlit as st
import csv
import os

# 1. Page Configuration
st.set_page_config(page_title="Data Movie: Advanced Analytics", page_icon="📈", layout="wide")

st.title("🎬 The Data Movie: Business Insights Dashboard")
st.markdown("---")

# 2. Paths to your Gold Reports
total_sales_path = 'src/data/gold/total_sales_report.csv'
trend_sales_path = 'src/data/gold/sales_trend_report.csv'

# --- SECTION 1: KEY PERFORMANCE INDICATORS (KPIs) ---
if os.path.exists(total_sales_path):
    categories = []
    totals = []
    
    with open(total_sales_path, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            categories.append(row['Category'])
            totals.append(float(row['Total_Sales']))

    st.subheader("📍 Real-Time Category Totals")
    cols = st.columns(len(categories))
    for i, cat in enumerate(categories):
        cols[i].metric(label=cat, value=f"${totals[i]:,.0f}")
    
    st.markdown("---")

    # --- SECTION 2: COMPARATIVE & TREND ANALYSIS ---
    col_left, col_right = st.columns([1, 1])
    
    # Left Side: Bar Chart
    with col_left:
        st.subheader("📊 Sales Distribution")
        chart_data = dict(zip(categories, totals))
        st.bar_chart(chart_data)

    # Right Side: Trend Logic
    with col_right:
        st.subheader("📅 Monthly Trend Analysis")
        if os.path.exists(trend_sales_path):
            trend_list = []
            with open(trend_sales_path, mode='r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    trend_list.append(row)

            target_cat = st.selectbox("Select Category to View Trend:", categories)
            
            months = []
            monthly_sales = []
            for item in trend_list:
                if item['Category'] == target_cat:
                    months.append(item['Month'])
                    monthly_sales.append(float(item['Total_Sales']))

            if months:
                st.line_chart(dict(zip(months, monthly_sales)))
                
                # --- NEW: BUSINESS HEALTH CHECK (DELTA METRIC) ---
                if len(monthly_sales) >= 2:
                    current_val = monthly_sales[-1]
                    previous_val = monthly_sales[-2]
                    growth = ((current_val - previous_val) / previous_val) * 100
                    
                    st.metric(
                        label=f"Latest {target_cat} Performance", 
                        value=f"${current_val:,.0f}", 
                        delta=f"{growth:.1f}% vs Last Month"
                    )
            else:
                st.info("No trend data available for this category.")

    # --- SECTION 3: AI SALES ASSISTANT (SIDEBAR) ---
    st.sidebar.header("🤖 AI Sales Assistant")
    st.sidebar.info("Retrieving insights from your Gold layer.")
    query = st.sidebar.text_input("Ask about a category (e.g., Furniture):")
    
    if query:
        found = False
        for i, cat in enumerate(categories):
            if query.lower() in cat.lower():
                st.sidebar.success(f"The total for {cat} is ${totals[i]:,.2f}")
                found = True
        if not found:
            st.sidebar.warning("Category not found in data.")

else:
    st.error("❌ Gold report not found! Please ensure your pipeline has run successfully.")


# import streamlit as st
# import csv
# import os

# # 1. Page Configuration
# st.set_page_config(page_title="Data Movie: Advanced Analytics", page_icon="📈", layout="wide")

# st.title("🎬 The Data Movie: Business Insights Dashboard")
# st.markdown("---")

# # 2. Paths to your Gold Reports
# total_sales_path = 'src/data/gold/total_sales_report.csv'
# # Note: Ensure you run the updated 3_gold.py to generate this trend file!
# trend_sales_path = 'src/data/gold/sales_trend_report.csv'

# # --- SECTION 1: KEY PERFORMANCE INDICATORS (KPIs) ---
# if os.path.exists(total_sales_path):
#     categories = []
#     totals = []
    
#     with open(total_sales_path, mode='r', encoding='utf-8') as f:
#         reader = csv.DictReader(f)
#         for row in reader:
#             categories.append(row['Category'])
#             totals.append(float(row['Total_Sales']))

#     # Display Metrics in Columns
#     st.subheader("📍 Real-Time Category Totals")
#     cols = st.columns(len(categories))
#     for i, cat in enumerate(categories):
#         cols[i].metric(label=cat, value=f"${totals[i]:,.0f}")
    
#     st.markdown("---")

#     # --- SECTION 2: COMPARATIVE ANALYSIS (BAR CHART) ---
#     col_left, col_right = st.columns([2, 1])
    
#     with col_left:
#         st.subheader("📊 Sales Distribution")
#         chart_data = dict(zip(categories, totals))
#         st.bar_chart(chart_data)

#     # --- SECTION 3: AI SALES ASSISTANT (SIDEBAR) ---
#     st.sidebar.header("🤖 AI Sales Assistant")
#     st.sidebar.info("I can retrieve specific totals from your Gold layer.")
#     query = st.sidebar.text_input("Enter a category (e.g., Electronics):")
    
#     if query:
#         found = False
#         for i, cat in enumerate(categories):
#             if query.lower() in cat.lower():
#                 st.sidebar.success(f"The total for {cat} is ${totals[i]:,.2f}")
#                 found = True
#         if not found:
#             st.sidebar.warning("Category not found in data.")

#     # --- SECTION 4: TREND ANALYSIS (ADVANCED STEP) ---
#     st.markdown("---")
#     st.subheader("📅 Monthly Trend Analysis")
    
#     if os.path.exists(trend_sales_path):
#         trend_list = []
#         with open(trend_sales_path, mode='r', encoding='utf-8') as f:
#             reader = csv.DictReader(f)
#             for row in reader:
#                 trend_list.append(row)

#         # Dropdown to filter trends
#         target_cat = st.selectbox("Select Category to View Trend:", categories)
        
#         # Filter data for the line chart
#         months = []
#         monthly_sales = []
#         for item in trend_list:
#             if item['Category'] == target_cat:
#                 months.append(item['Month'])
#                 monthly_sales.append(float(item['Total_Sales']))

#         if months:
#             st.line_chart(dict(zip(months, monthly_sales)))
#         else:
#             st.write("No trend data available for this category.")
#     else:
#         st.info("💡 To see trends, please run your updated '3_gold.py' script first.")

# else:
#     st.error("❌ Gold report not found! Please ensure your pipeline has run successfully.")