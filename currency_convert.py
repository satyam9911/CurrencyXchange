from currency_converter import CurrencyConverter
def convert_currency_amount(amount , currentcurrency , targetcurrency):
    try:
        if currentcurrency == targetcurrency:
            return_value = "Current Currency and Target Currency are same!"
        else:
            currency = CurrencyConverter()
            return_value = currency.convert(amount , currentcurrency , targetcurrency)
    except:
        return_value = "Something went wrong!"
    finally:
        return return_value
