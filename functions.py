def drop_string_integer(DataFrame, column_name):
    DataFrame[column_name] = DataFrame[column_name].str.replace('string_', '')
    DataFrame[column_name] = DataFrame[column_name].str.replace('String_', '')
    DataFrame[column_name] = DataFrame[column_name].str.replace('String ', '')
    DataFrame[column_name] = DataFrame[column_name].str.replace('integer_', '')

def drop_(DataFrame, column_name):
    DataFrame.pop(column_name)

def clean_gender(DataFrame, column_name):
    DataFrame[column_name] = DataFrame[column_name].replace('0', 'Male')
    DataFrame[column_name] = DataFrame[column_name].replace('1', 'Female')
    DataFrame[column_name] = DataFrame[column_name].replace('M', 'Male')
    DataFrame[column_name] = DataFrame[column_name].replace('F', 'Female')
    DataFrame[column_name] = DataFrame[column_name].replace('boolean_1', 'Male')
    DataFrame[column_name] = DataFrame[column_name].replace('character_M', 'Male')
    DataFrame[column_name] = DataFrame[column_name].replace('boolean_0', 'Female') 

def clean_name(DataFrame, column_name):
    DataFrame[column_name] = DataFrame[column_name].str.replace('\W','')
    DataFrame[column_name] = DataFrame[column_name].str.title()

def clean_email(DataFrame, column_name):
    DataFrame[column_name] = DataFrame[column_name].str.lower()

def clean_city(DataFrame, column_name):
    DataFrame[column_name] = DataFrame[column_name].str.replace('_', ' ')
    DataFrame[column_name] = DataFrame[column_name].str.title()

def clean_country(DataFrame, column_name):
    DataFrame[column_name] = 'USA'

def clean_age(DataFrame, column_name):
    DataFrame[column_name] = DataFrame[column_name].str.replace('\D', '')

def FirstName_and_LastName(DataFrame, column_name):
    name = DataFrame[column_name].str.split(expand=True)
    DataFrame['FirstName'], DataFrame['LastName'] = name[0], name[1]
    DataFrame.drop('Name', axis=1, inplace=True)
