from credentials import currencyCredentials
from sql_connections import insert_user_data
import sys
#%%
def upload_image(image_name,update):
    try:
        if not currencyCredentials.APP_USER:
            return_value = "Please sign in"
        elif str(update) =='True':
            insert_query = "UPDATE user_profile_Picture SET profile_picture = '"+image_name+"' WHERE username = '"+currencyCredentials.APP_USER+"'"
            insert_user_data(insert_query)
            return_value = "Profile Photo updated sucessfully"
        else:
            insert_query = "insert into user_profile_picture (username,profile_Picture) values ('"+currencyCredentials.APP_USER+"','"+image_name+"')" 
            insert_user_data(insert_query)
            return_value = "Profile photo uploaded Successfully"
    except:
        print(sys.exc_info()[1])
        return_value = 'Unable to Upload image'
    finally:
        return return_value