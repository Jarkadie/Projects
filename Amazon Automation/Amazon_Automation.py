import smtplib 
import os
import pickle
from selenium import webdriver
from email.mime.text import MIMEText
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from selenium.webdriver.common.keys import Keys


def getProductInfo(url):
    driver = webdriver.Chrome("C:/Users/Jacob/chromedriver.exe")
    driver.get(url)

    price_container =  driver.find_element_by_class_name("a-box-group")

    try:
        price = price_container.find_element_by_id("price").get_attribute('innerHTML')
    except:
        price = price_container.find_element_by_id("newBuyBoxPrice").get_attribute('innerHTML')

    #title = driver.find_element_by_id("productTitle").get_attribute('innerHTML').strip()

    driver.close()
    return float(price[1:])

def Send_Notification(to,subject,body):
    message = EmailMessage()
    message.set_content(body)
    message['subject'] = subject
    message['to'] = to
    user = "[ Senders Email Address]"

    
    password = "[Password Here]"
    
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(user,password)
    server.send_message(message)

    server.quit()

def loweredPriceMessage(title,oldPrice,newPrice,url):
    return title + " price has been lowered from $" + str(oldPrice) + " to $" + str(newPrice) + "!! \n Order Now:" + url


if __name__ == "__main__":
    for filename in os.listdir():
        if filename.endswith(".pickle"):
            print("Opening " + filename)
            productInfo = pickle.load(open(filename,"rb+"))
            newPrice = getProductInfo(productInfo[2])

            print("$"+ str(productInfo[1]) + "-----> $" + str(newPrice))

            if(newPrice < productInfo[1]):
                print("The Price has been lowered!")
                oldPrice = productInfo[1]
                productInfo[1] = newPrice
                pickle.dump(productInfo,open(filename,"wb"))
                Send_Notification(productInfo[3],"Price Update", loweredPriceMessage(productInfo[0],oldPrice,productInfo[1],productInfo[2]))
                
            else:
                print(productInfo[0] + " price has not changed from $" + str(productInfo[1]))
                Send_Notification(productInfo[3],"Price Update", productInfo[0] + " price has not changed from $" + str(productInfo[1]))



'''
AT&T: [number]@txt.att.net
Sprint: [number]@messaging.sprintpcs.com or [number]@pm .sprint.com
T-Mobile: [number]@tmomail.net
Verizon: [number]@vtext.com
Boost Mobile: [number]@myboostmobile.com
Cricket: [number]@sms.mycricket.com
Metro PCS: [number]@mymetropcs.com
Tracfone: [number]@mmst5.tracfone.com
U.S. Cellular: [number]@email.uscc.net
Virgin Mobile: [number]@vmobl.com
'''
