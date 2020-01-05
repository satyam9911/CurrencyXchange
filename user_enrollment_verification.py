from sql_connections import check_user_existence , insert_user_data
import sys
#%%
def user_sign_up(user_name,password,confirm_password,update):
    try:
        if password == confirm_password:
            user_existence_query = "select 'exist' from userConfidentialData where username = '"+user_name+"'"
            user_existence = check_user_existence(user_existence_query)
            print("Update value-------------->"+ update)
            if str(update) == 'True':
                if user_existence is None:
                    return_value = "User does not exist"
                else:
                    user_insert_query = "UPDATE userConfidentialData SET userPassword = '"+password+"' WHERE username = '"+user_name+"'"
                    insert_user_data(user_insert_query)
                    return_value = "Password updated successfully"
            elif user_existence is None and not update:
                return_value = "User already exist"
            else:
                user_insert_query = "insert into userConfidentialData (username,userPassword) values ('"+user_name+"','"+password+"')"
                insert_user_data(user_insert_query)
                return_value = "User enrolled successfully"
        else:
            return_value = 'Entered password does not match confirm password'
    except:
        print(sys.exc_info()[1])
        return_value = "Something went wrong! Please try again"
    finally:
        return return_value
        
def user_sign_in(user_name,password):
    try:
        user_existence_query = "select * from userConfidentialData where username = '"+user_name+"'"
        user_existence = check_user_existence(user_existence_query)
        print("user existence data -------------->"+str(user_existence))
        if user_existence is None:
            return_value = "User does not exist"
        elif user_existence[0][1] == password:
            return_value = ["Welcome "+user_name,"Success"]
        else :
            return_value = ["Invalid Password" , "Failure"]
        return return_value
    except:
        print(sys.exc_info()[1])
        return_value = ["Something went wrong! Please try again" , "Failure"]
        return return_value

#%%
#user_sign_up('suraj','pass','pass')
#user_sign_in('satyam','pass')