import pandas as pd
from io import StringIO
from my_ds_babel import csv_to_sql
from functions import *
import warnings
warnings.filterwarnings("ignore")

def my_m_and_a (data, data2, data3):
    # Cleaning DataFrames

    # DATAFRAME 1
    # df1 = df1.drop(['UserName'], axis=1)
    df1 = pd.read_csv(data)
    del df1['UserName']
    clean_gender(df1, 'Gender')   # Gender
    clean_name(df1, 'FirstName')   # FirstName
    clean_name(df1, 'LastName')   # LastName
    clean_email(df1, 'Email')   # Email
    clean_city(df1, 'City')   # City
    clean_country(df1, 'Country')   # Country

    # DATAFRAME 2
    df2 = pd.read_csv(data2, sep=';', header=None, names=['Age', 'City', 'Gender', 'Name', 'Email'])
    clean_age(df2, 'Age')   # Age 
    clean_city(df2, 'City')   # City
    clean_gender(df2, 'Gender')   # Gender
    df2['Name'] = df2['Name'].str.replace('\W', ' ')    # Name
    df2['Name'] = df2['Name'].str.replace('    ', ' ')  # Name
    df2['Name'] = df2['Name'].str.replace('  ', ' ')    # Name
    df2['Name'] = df2['Name'].str.strip()   # Name
    df2['Name'] = df2['Name'].str.title()   # Name
    FirstName_and_LastName(df2, 'Name')    # from name FirstName and LastName
    clean_email(df2, 'Email')    # Email

    # DATAFRAME 3
    df3 = pd.read_csv(data3, sep='\t', skiprows=1, names=['Gender', 'Name', 'Email', 'Age', 'City', 'Country'])
    clean_gender(df3, 'Gender') # Gender
    df3.Name = df3.Name.str.title() # Name
    FirstName_and_LastName(df3, 'Name') # Name
    df3.LastName = df3.LastName.str.replace('"', '')    # Name
    clean_email(df3, 'Email')   # Email
    clean_age(df3, 'Age')   # Age
    clean_city(df3, 'City') # City
    clean_country(df3, 'Country')   # Country
    [drop_string_integer(df3, column) for column in df3.columns]

    # Connecting dataframes
    merged_df = pd.concat([df1, df2, df3], ignore_index=True, names=["Gender", "FirstName", "LastName",  
                                                                        "Email", "Age", "City", "Country"])
    merged_df['Country'].fillna(value = "USA", inplace = True)
    merged_df['Age'] = merged_df['Age'].astype('str')
    merged_df['FirstName'] = merged_df['FirstName'].astype('str')
    merged_df['LastName'] = merged_df['LastName'].astype('str')
    
    # print(merged_df.dtypes)

    return merged_df

def main():
    csv1 = "file:///home/docode/project/only_wood_customer_us_1.csv"
    csv2 = "file:///home/docode/project/only_wood_customer_us_2.csv"
    csv3 = "file:///home/docode/project/only_wood_customer_us_3.csv"

    # Importing Data
    content_database_1 = pd.read_csv(csv1)
    content_database_2 = pd.read_csv(csv2, sep=';', header=None, names=['Age', 'City', 'Gender', 'Name', 'Email'])
    content_database_3 = pd.read_csv(csv3, sep='\t', skiprows=1, names=['Gender', 'Name', 'Email', 'Age', 'City', 'Country'])

    merged_csv = my_m_and_a(content_database_1,content_database_2, content_database_3)
    # merged_csv = my_m_and_a(StringIO(content_database_1), StringIO(content_database_2), StringIO(content_database_3))


    csv_to_sql(merged_csv, 'plastic_free_boutique.db', 'customers')

if __name__ == "__main__":
    main()
