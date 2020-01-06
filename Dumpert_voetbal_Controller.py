from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

# list of tags found on the video on website
tags = ["//a[@href='/tag/voetbal']",
        "//a[@href='/tag/soccer']",
        "//a[@href='/tag/wk']",
        "//a[@href='/tag/VI']",
        "//a[@href='/tag/vi']",
        "//a[@href='/tag/vi inside']"
        ]

Downvotecounter = 0
driver = webdriver.Firefox()
driver.set_page_load_timeout("10")

driver.get("https://www.dumpert.nl/latest")
driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/a").click() #cookie click

while True: #loops entire process every 60seconds
    driver.find_element_by_xpath("/html/body/div/div/div[3]/div[1]/section/div/div[2]/a[1]/div[2]/div[2]/span[1]").click() #click on latest video

    def check_if_tag_exists(tag): #checks if video has tag in list Tags then makes it True, otherwise false
        try:
            driver.find_element_by_xpath(tag)
        except NoSuchElementException:
            return False
        return True

    for x in tags:
        if check_if_tag_exists(x):
            driver.find_element_by_xpath("/html/body/div/div/div[3]/div[1]/section/section[1]/div/div[2]/div[2]/div[3]").click()        #clicks downvote button
            print("Voetbal video succesfully downvoted")
            Downvotecounter + 1

    driver.back()
    driver.refresh() #To fix the black page/inproperly loaded page issue
    print(Downvotecounter, "min kudo's uitgedeeld")
    time.sleep(30)

