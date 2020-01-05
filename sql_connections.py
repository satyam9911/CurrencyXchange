import pyodbc
from credentials import currencyCredentials
import sys

def check_user_existence(user_existence_query):
    try:
        print('check_user_existence method called')
        mssqlConnection = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER='+currencyCredentials.MSSQL_IP_ADDRESS+';DATABASE='+currencyCredentials.MSSQL_DATABASE+';UID='+currencyCredentials.MSSQL_USER_NAME+';PWD='+currencyCredentials.MSSQL_PASSWORD)
        print('Got the mssqlConnection:',mssqlConnection)
        with mssqlConnection:
            mssqlCursor = mssqlConnection.cursor()
#            print('Executing the query:',user_existence_query)
            mssqlCursor.execute(user_existence_query)
#            print('Query executed')
            user_existence = mssqlCursor.fetchall()
#            print('Data extracted')
            return user_existence
    except:
        print('check_user_existence->catch block->There was an issue while getting data from database')
        return 'User existence verification failed'

def insert_user_data(insert_query):
    try:
        print('insert_new_user method called')
        mssqlConnection = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER='+currencyCredentials.MSSQL_IP_ADDRESS+';DATABASE='+currencyCredentials.MSSQL_DATABASE+';UID='+currencyCredentials.MSSQL_USER_NAME+';PWD='+currencyCredentials.MSSQL_PASSWORD)
        print('Got the mssqlConnection:',mssqlConnection)
        with mssqlConnection:
            mssqlCursor = mssqlConnection.cursor()
#            print('Executing the query:',insert_query)
            mssqlCursor.execute(insert_query)
            mssqlCursor.commit()
        return 'success'
    except:
        print('insert_new_user->catch block->There was an issue while inserting data into database')
        print(sys.exc_info()[1])
        return 'failed'