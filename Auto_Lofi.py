from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

driver = webdriver.Chrome("C:/Users/Jacob/chromedriver.exe")
driver.get("https://www.youtube.com/results?search_query=lofi+hip+hop")
videos = []

for x in range(1,11):  
    possible_videos = driver.find_element_by_xpath("//*[@id='contents']/ytd-video-renderer[" + str(x) + "]")
    videos.append(possible_videos)

videoIndex = random.randint(0,len(videos)-1)

chosen_vid = videos[videoIndex]
chosen_vid.click()
print("Lofi Video has been selected. Please keep the Terminal open to continue playing")




