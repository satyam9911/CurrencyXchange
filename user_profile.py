from credentials import currencyCredentials
from sql_connections import insert_user_data
import sys
#%%
def upload_image(image_name,update):
    try:
        if not currencyCredentials.APP_USER:
            return_value = "Please sign in"
        elif str(update) =='True':
            image_binary = str(convertToBinaryData(image_name))
            insert_query = "UPDATE user_profile_Picture SET profile_picture = '"+image_binary+"' WHERE username = '"+currencyCredentials.APP_USER+"'"
            insert_user_data(insert_query)
            return_value = "Profile Photo updated sucessfully"
        else:
            image_binary = convertToBinaryData(image_name)
            insert_query = "insert into user_profile_picture (username,profile_Picture) values ('"+currencyCredentials.APP_USER+"','"+image_binary+"')" 
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
#upload_image('C:\\Users\\Administrator\\Desktop\\currency_change\\saved_img-final.jpg','True')