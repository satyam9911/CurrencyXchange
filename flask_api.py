from flask import Flask, jsonify, request
import credentials as cred
import sys
from flask_cors import CORS

#%%

app = Flask(__name__)
CORS(app)
    

@app.route('/status',methods=['GET'])
def status():
    try:
        print("Processing the parameters")
        output=cred.currencyCredentials.loadConfigurations(request)
        print("loaded the parameters with staus:",output)
        var = {"result":output}
    except:
        var = {"result":"Something is wrong with api"}
        print(sys.exc_info()[1])
    finally:
        return jsonify(var)

@app.route('/userSignUp')
def userSignUp():
    try:
        username = request.args['user_name']
        password = request.args['password']
        confirmpassword = request.args['confirm_password']
        update = request.args['update']
        import user_enrollment_verification as user_enroll
        output = user_enroll.user_sign_up(username, password, confirmpassword, update)
        var = {"result":output}
    except:
        var = {"result":"Something is wrong with api"}
        print(sys.exc_info()[1])
    finally:
        return jsonify(var)

@app.route('/userSignIn')
def userSignIn():
    try:
        username = request.args['user_name']
        password = request.args['password']
        import user_enrollment_verification as user_sign
        output = user_sign.user_sign_in(username, password)
        if output[1] == "Success":
            cred.currencyCredentials.loaduserdata(request)
            print("User Data Loaded successfully")
        var = {"result":output[0]}
    except:
        var = {"result":"Something is wrong with api"}
        print(sys.exc_info()[1])
    finally:
        return jsonify(var)

@app.route('/createWallet')
def createWallet():
    try:
        import user_wallet
        output = user_wallet.create_user_wallet()
        var = {"result":output}
    except:
        var = {"result":"Something is wrong with api"}
        print(sys.exc_info()[1])
    finally:
        return jsonify(var)

@app.route('/readWallet')
def readWallet():
    try:
        import user_wallet
        output = user_wallet.read_wallet_amount()
        var = {"Current Balance":output[0][0]}
        if not output[0][0] == "0":
            number = 0
            for index in output[1]:
                print("Inside for loop")
                print("index value------>"+str(index))
                key = "Transaction "+str(number)
                var[key]=(index[0],str(index[1]),index[2])
                number+=1
        else:
            var["Transaction"]="You have no transactions"
        print(var)
        
    except:
        var = {"result":"Something is wrong with api"}
        print(sys.exc_info()[1])
    finally:
        return jsonify(var)

@app.route('/updateWallet')
def updateWallet():
    try:
        amount = request.args['amount']
        tran_type = request.args['transaction_type']
        import user_wallet
        output = user_wallet.update_wallet_amount(amount, tran_type)
        var = {"result":output}
    except:
        var = {"result":"Something is wrong with api"}
        print(sys.exc_info()[1])
    finally:
        return jsonify(var)

@app.route('/convertCurrency')
def convertCurrency():
    try:
        amount = request.args['amount']
        current_currency = request.args['current_currency']
        target_currency = request.args['target_currency']
        import currency_convert
        output = currency_convert.convert_currency_amount(amount, current_currency, target_currency)
        var = {"result":output}
    except:
        var = {"result":"Something is wrong with api"}
        print(sys.exc_info()[1])
    finally:
        return jsonify(var)

@app.route('/setImage')
def setImage():
    try:
        image = request.args['Image']
        update = request.args['update']
        import user_profile
        output = user_profile.upload_image(image,update)
        var = {"result":output}
    except:
        var = {"result":"Something is wrong with api"}
        print(sys.exc_info()[1])
    finally:
        return jsonify(var)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)