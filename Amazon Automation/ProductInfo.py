from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import csv
import pickle

class ProductInfo:
    url = ""
    price = 0
    name = ""
    recipient = ""

    def __init__(self,url):
        self.url = url
        self.getProductInfo(url)

    def getProductInfo(self,url):
        driver = webdriver.Chrome("C:/Users/Jacob/chromedriver.exe")
        driver.get(url)

        price_container =  driver.find_element_by_class_name("a-box-group")

        try:
            self.price = float(price_container.find_element_by_id("price").get_attribute('innerHTML')[1:])
        except:
            self.price = float(price_container.find_element_by_id("newBuyBoxPrice").get_attribute('innerHTML')[1:])

        self.title = driver.find_element_by_id("productTitle").get_attribute('innerHTML').strip()

        driver.close()
        

    def displayInfo(self):
        return ('The Current Price of "' + self.title +  '" is: $'  + str(self.price))

    def getInfo(self):
        return [self.title,self.price,self.url,self.recipient]

    def saveInfo(self):
        pickle_out = open(self.title[:10]+".pickle","wb")
        pickle.dump(self.getInfo(),pickle_out)
        pickle_out.close()







if __name__ == "__main__":
    print("Welcome to the Amazon Price Checking Automater Product Information Saver... \n")
    print("Here you enter the URL of the product you want to recieve updates for and save this information for the automater... \n")
    amznUrl =  str(input("Please Enter the Products URL address:   "))

    newProduct = ProductInfo(amznUrl)

    print(newProduct.displayInfo())

    saveInfo = str(input("Would you like to save this product information?(Y/N): "))
    if(saveInfo == "Y" or saveInfo == "y"):
        recepient = str(input("Please enter a recipient: "))
        newProduct.recipient = recepient
        newProduct.saveInfo()
        print("Product Information Saved. Thanks for Using the Amazon Price Checking Automater")
    else:
        print("Product Information Not Saved. Thanks for Using the Amazon Price Checking Automater")

        #https://www.amazon.com/gp/product/1941220975/ref=ox_sc_act_title_1?smid=ATVPDKIKX0DER&psc=1
        