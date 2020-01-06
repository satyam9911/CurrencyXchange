from credentials import currencyCredentials
from sql_connections import insert_user_data
import sys
#%%
def upload_image(image_name,update):
    try:
        if not currencyCredentials.APP_USER:
            return_value = "Please sign in"
        elif str(update) =='True':
            insert_query = "update user_profile_Picture set profile_Picture = (select bulkcolumn from openrowset(bulk N'"+image_name+"',single_blob) image) where username = '"+currencyCredentials.APP_USER+"'"
            insert_user_data(insert_query)
            return_value = "Profile Photo updated sucessfully"
        else:
            insert_query = "insert into user_profile_Picture (username,profile_Picture) select '"+currencyCredentials.APP_USER+"',bulkcolumn from openrowset(bulk N'"+image_name+"',single_blob) image;" 
            insert_user_data(insert_query)
            return_value = "Profile photo uploaded Successfully"
    except:
        print(sys.exc_info()[1])
        return_value = 'Unable to Upload image'
    finally:
        return return_value

def convertToBinaryData(filename):
    with open(filename, 'rb') as image:
        binaryData = image.read()
    print(binaryData)
    return binaryData
#%%
upload_image('F:\\saved_img-final.jpg','True')