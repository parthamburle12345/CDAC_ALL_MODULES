'''
- Object-Oriented Pipeline Design
- Schema Standardization (snake_case)
- String Normalization & Structural Mapping
- Automated Missing Value Imputation (Median / Mode)
- IQR-based Outlier Detection & Capping
- Logging & Type Annotations
'''
import logging
from typing import List,Dict,Optional
import numpy as np
import pandas as pd 

logging.basicConfig(
    level = logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)

class TransactionDataCleaner:
    def __init__(self, regional_mapping: Optional[Dict[str,str]] = None):
        self.regional_mapping = regional_mapping or{
            "blr": "Bengaluru",
            "bengaluru": "Bengaluru",
            "mum": "Mumbai",
            "mumbai": "Mumbai",
            "del": "Delhi",
            "delhi": "Delhi"            
        }
    def standardize_schema(self,df: pd.DataFrame) -> pd.DataFrame:  #Cleans column names (headers).
        df = df.copy()
        df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
        return df


    def sanitize_text(self,df: pd.DataFrame) -> pd.DataFrame: #Cleans actual text values inside columns.
        df = df.copy()
        string_cols = df.select_dtypes(include=["object","string"]).columns
        for col in string_cols:         #instead of lambada we use for loop1
            df[col] = df[col].str.strip()
            df[col] = df[col].str.lower()

        if "full_name" in df.columns:
            df["full_name"] = df["full_name"].str.title()
        return df
    

    def deduplicate(self,df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()
        df = df.drop_duplicates().reset_index(drop = True)
        return df


    def map_categoricals(self,df: pd.DataFrame) -> pd.DataFrame:   #Makes region names consistent.
        df = df.copy()
        if "region" in df.columns:
            df["region"] = df["region"].map(self.regional_mapping).fillna(df["region"])
        return df


    def cast_types(self,df: pd.DataFrame) -> pd.DataFrame:    # Converts data into correct types.
        df = df.copy()
        if "purchase_amount" in df.columns:
            df["purchase_amount"] = df["purchase_amount"].replace(
                r"[\$,]", "", regex=True
            ).str.strip()
            df["purchase_amount"] = pd.to_numeric(df["purchase_amount"], errors="coerce")

        if "join_date" in df.columns:
            df["join_date"] = pd.to_datetime(df["join_date"], errors="coerce")
        return df
    

    def impute_missing(self,df: pd.DataFrame) -> pd.DataFrame:  #Fills empty values.
        df = df.copy()
        if "purchase_amount" in df.columns:
            df["purchase_amount"] = df["purchase_amount"].fillna(df["purchase_amount"].median)

        if "age" in df.columns:
            df["age"] = df["age"].fillna(df["age"].median)

        if "region" in df.columns:
            df["region"] = df["region"].fillna(df["region"].mode()[0])
        return df


    def handle_outliers_iqr(self,df: pd.DataFrame , column:str ="purchase_amount") -> pd.DataFrame:
        if column not in df.column:
            return df
        df = df.copy()
        Q1
        return df


    def fit_transform(self,df: pd.DataFrame) -> pd.DataFrame:   #Runs all cleaning steps one by one.
        df_clean = (
            df.pipe(self.standardize_schema)
            .pipe(self.sanitize_text)
            .pipe(self.deduplicate)
            .pipe(self.map_categoricals)
            .pipe(self.cast_types)
            .pipe(self.impute_missing)
            .pipe(self.handle_outliers_iqr, column = "purchase_amount")

        )
        return df_clean
    




if __name__ == "__main__":
    raw_data = {
        " Customer_ID ": ["CUST_001", "CUST_002", "CUST_001", "CUST_004", "CUST_005", "CUST_006", "CUST_007"],
        " Full Name ": ["  aarav sharma ", "BHAVNA PATEL", "  aarav sharma ", "chirag gupta", "divya REDDY ", " eshan verma", "Fiona Gallagher"],
        " Purchase_Amount ": [" $1,200.50 ", " $450.00 ", " $1,200.50 ", " $89.99 ", " $15,000.00 ", " $150.25 ", np.nan],
        " Join Date ": ["2024-01-15", "2023-11-20", "2024-01-15", "2022-05-10", "2024-03-01", "2023-08-19", "2024-02-12"],
        " Region ": ["BLR", " Bengaluru ", "BLR", "MUM", " Mumbai ", "DEL", np.nan],
        " Age ": [28, 34, 28, np.nan, 42, 29, 31],
    }
    df_raw = pd.DataFrame(raw_data)
    
    print("\n" + "=" * 60)
    print("RAW INPUT DATAFRAME")
    print("=" * 60)
    print(df_raw)
    print("=" * 60 + "\n")
    
    regional_mapping = {
            "blr": "Bengalore",
            # "bengaluru": "Bengalore",
            "mum": "Bombay",
            # "mumbai": "Bombay",
            "del": "Delhi",
            # "delhi": "Delhi"
        }
    cleaner = TransactionDataCleaner(regional_mapping)
    df_cleaned = cleaner.fit_transform(df_raw)
    
    print("\n" + "=" * 60)
    print("CLEANED DATAFRAME")
    print("=" * 60)
    print(df_cleaned)
    print("=" * 60 + "\n")
    print("Column Types ",df_cleaned.dtypes)
    print("=" * 60 + "\n")