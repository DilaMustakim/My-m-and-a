import pandas as pd 
import sqlite3 as sql 
import warnings
# warnings.filterwarnings("ignore")

# Part I SQL to CSV.
# def sql_to_csv(database, table_name):
#     connection = sql.connect(database)
#     df = pd.read_sql(f"SELECT * FROM {table_name}", connection)
#     d = ['Karsdorf Fault']
#     df = df[~df['fault_name'].isin(d)]
#     df.to_csv("all_fault_lines.csv", index=False)
#     my_list = []
#     with open("all_fault_lines.csv") as f:
#         for line in f:
#             my_list.append(line)
#     return "".join(my_list)

# Part II CSV to SQL
def csv_to_sql(csv_content, database, table_name):
    connection = sql.connect(database)
    cursor = connection.cursor()
    df = pd.read_csv(csv_content)
    df = df.drop_duplicates()
    # a = ['Mega Basalt Field', 'Ethiopia']
    # if database == 'list_volcanos.db':
    #     df = df[~df['Volcano Name'].isin(a)]
    df.to_sql(table_name, connection, index=False, if_exists='replace')

# Part III
# if __name__ == '__main__':
#     print(sql_to_csv('all_fault_line.db','fault_lines'))
#     csv_content = open("list_volcano.csv")
#     csv_to_sql(csv_content, 'list_volcanos.db','volcanos')
