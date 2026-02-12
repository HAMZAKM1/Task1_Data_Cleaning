import pandas as pd

df = pd.read_csv(r"C:\Users\hamza\Downloads\archive\Task1_Data_Cleaning\Mall_Customers.csv")

df = df.drop_duplicates()
df['Gender'] = df['Gender'].str.lower().str.strip()
df.rename(columns={'CustomerID':'customer_id','Gender':'gender','Age':'age','Annual Income (k$)':'annual_income_k','Spending Score (1-100)':'spending_score'}, inplace=True)
cleaned_file = r"C:\Users\hamza\Downloads\archive\Task1_Data_Cleaning\Mall_Customers_cleaned.csv"
df.to_csv(cleaned_file, index=False)
print("Cleaning Summary:")
print(f"Total rows: {df.shape[0]}")
print(f"Columns: {df.columns.tolist()}")
print("Duplicate rows removed (if any)")
print("Gender standardized to lowercase")
print("Column names cleaned and simplified")
print(f"\\nCleaned dataset saved as: {cleaned_file}")
