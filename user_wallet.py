from credentials import currencyCredentials
from sql_connections import check_user_existence,insert_user_data
import sys

def create_user_wallet():
    try:
        if not currencyCredentials.APP_USER:
            return_value = "Please sign in"
        else:
            user_existence_query = "select 'exist' from userWalletData where username = '"+currencyCredentials.APP_USER+"'"
            user_existence = check_user_existence(user_existence_query)
            if user_existence is not None:
                return_value = "You already have a wallet!"
            else:
                insert_query = "insert into userWalletData (username,currentBalance) values ('"+currencyCredentials.APP_USER+"',0)"
                insert_user_data(insert_query)
                return_value = "Wallet created Successfully"
    except:
        print(sys.exc_info()[1])
        return_value = "Something went wrong! Please try again"
    finally:
        return return_value

def read_wallet_amount():
    try:
        user_existence_query = "select 'exist' from userWalletData where username = '"+currencyCredentials.APP_USER+"'"
        user_existence = check_user_existence(user_existence_query)
        if not currencyCredentials.APP_USER:
            return_value = "Please sign in"
        elif user_existence is None:
            return_value = "You do not have wallet!"
        else:
            user_wallet_read_query = "select currentBalance from userWalletData where username = '"+currencyCredentials.APP_USER+"'"
            wallet_data = check_user_existence(user_wallet_read_query)
#            transaction_read_query = "select transactionType , transactionTime , amount from userTransactionsData where username = '"+currencyCredentials.APP_USER+"' order by transactionTime desc"
            transaction_read_query = "select transactionType , transactionTime , amount from userTransactionsData where username = '"+currencyCredentials.APP_USER+"' order by transactionTime desc"
            transaction_data = check_user_existence(transaction_read_query)
            return_value = [wallet_data[0] , transaction_data]
            print("Wallet money------------------>"+str(return_value))
    except:
        print(sys.exc_info()[1])
        return_value = "Something went wrong! Please try again"
    finally:
        return return_value

def update_wallet_amount(amount , tran_type):
    try:
        user_wallet_read_query = "select currentBalance from userWalletData where username = '"+currencyCredentials.APP_USER+"'"
        user_wallet_data = check_user_existence(user_wallet_read_query)
        print("user wallet data --------------->"+str(user_wallet_data))
        if not currencyCredentials.APP_USER:
            return_value = "Please sign in"
        elif user_wallet_data is None:
            return_value = "You do not have wallet!"
        else:
            if str(tran_type) == "Dr":
                newWalletAmount = int(user_wallet_data[0]) - int(amount)
            else:
                newWalletAmount = int(user_wallet_data[0]) + int(amount)
            transaction_query = "Insert into userTransactionsData (username,transactionType,transactionTime,amount) values ('"+currencyCredentials.APP_USER+"','"+tran_type+"',GETDATE(),"+str(amount)+")"
            insert_user_data(transaction_query)
            update_wallet_query = "Update userWalletData set currentBalance = '"+str(newWalletAmount)+"' where username = '"+currencyCredentials.APP_USER+"'"
            insert_user_data(update_wallet_query)
            return_value = "Wallet updated successfully"
    except:
        print(sys.exc_info()[1])
        return_value = "Something went wrong! Please try again"
    finally:
        return return_value