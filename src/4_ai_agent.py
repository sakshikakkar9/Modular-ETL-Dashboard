import csv

# 1. The "Knowledge Base" - Load your Gold Report
gold_path = 'data/gold/total_sales_report.csv'
knowledge_base = {}

try:
    with open(gold_path, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            knowledge_base[row['Category'].lower()] = row['Total_Sales']

    print("🤖 AI Agent: 'I have loaded the business data. Ask me anything about sales!'")

    # 2. The Simple "Agent" Loop
    while True:
        user_query = input("\n👤 You: ").lower()
        
        if 'exit' in user_query or 'quit' in user_query:
            print("🤖 AI Agent: 'Goodbye!'")
            break
            
        # Retrieval Logic
        found = False
        for category, total in knowledge_base.items():
            if category in user_query:
                print(f"🤖 AI Agent: 'The total sales for {category.title()} is ${float(total):,.2f}.'")
                found = True
                break
        
        if not found:
            print("🤖 AI Agent: 'I'm sorry, I only have sales data for Electronics, Office Supplies, and Furniture.'")

except Exception as e:
    print(f"❌ Error: {e}")