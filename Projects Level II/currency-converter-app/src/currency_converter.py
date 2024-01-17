import requests
from loguru import logger


class CurrencyConverter:
    
    def __init__(self, base_currency, target_currency):
        
        self.base_currency = base_currency
        self.target_currency = target_currency
        
        self.data = self.get_date()
    
    
    def get_date(self):
        url = f"https://api.exchangerate-api.com/v4/latest/{self.base_currency}"
        response = requests.get(url)
        if response.ok:
            data = response.json()
            logger.info(f"Scraping Json data done!")
            return data
        else:
            logger.info(f"Error with Status code: {response.status_code}")
            return None
    
    def get_exchange_rate(self):
        try:
            result = self.data["rates"][self.target_currency]
            logger.info("Currency Exchange rate Crawler worked successfuly!")
            return result
        except:
            logger.info("Currency Exchange rate Crawler Failed!")
            return None
        
    def calculate_amount(self, amount):
        exchange_rate = self.get_exchange_rate()
        return amount * exchange_rate
        
    def get_all_currency(self):
        try:
            all_currency = self.data["rates"].keys()
            logger.info("Currency Ticker Crawler worked successfuly!")
            return all_currency
        except:
            logger.info("Currency Ticker Crawler Failed!")
            return None
    
        
if __name__ == "__main__":
    # Example "USD" to "CAD"
    obj = CurrencyConverter("USD", "CAD")
    print(obj.get_all_currency())
    print(obj.get_exchange_rate())