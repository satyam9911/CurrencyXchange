import sys
class currencyCredentials():
    MSSQL_IP_ADDRESS = 'DA6GMLT78LK0N'
    MSSQL_DATABASE = 'CurrencyXchange'
    MSSQL_USER_NAME = 'sa'
    MSSQL_PASSWORD = 'pass$123'
    APP_USER = 'satyam'
    
    def loadConfigurations(requestInput):
        try:
            currencyCredentials.MSSQL_IP_ADDRESS = requestInput.args['MSSQL_IP_ADDRESS']
            currencyCredentials.MSSQL_DATABASE = requestInput.args['MSSQL_DATABASE']
            currencyCredentials.MSSQL_USER_NAME = requestInput.args['MSSQL_USER_NAME']
            currencyCredentials.MSSQL_PASSWORD = requestInput.args['MSSQL_PASSWORD']
            return 'success'
        except:
             return sys.exc_info()[1]
    
    def loaduserdata(requestInput):
        try:
            currencyCredentials.APP_USER = requestInput.args['user_name']
            return 'success'
        except:
             return sys.exc_info()[1]