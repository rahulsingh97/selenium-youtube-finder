# import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#imports for selenium try catch
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#imports for selenium try catch

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.youtube.com")
#driver.close() close tab
#driver.quit() close browser
print(driver.title)
print(driver.get_window_size())
"""

"""
search = driver.find_element_by_name("search_query")
search.send_keys("Bad Candy Lover")
search.send_keys(Keys.ENTER)

#make selanium wait
try:
    main = WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.ID, "contents"))
    )
  #  main = driver.find_element_by_id("contents")
    articles = main.find_elements_by_tag_name("ytd-channel-renderer")
    for article in articles:
      header = article.find_element_by_class_name("style-scope ytd-channel-name")
    if(header.text != "Bad Candy Lover"):
            driver.quit()
    else:
        print(header.text)
        header.click()
except:
#finally:
    print("channel find error")
   # driver.quit()

try:
    main1 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='tabsContent']/paper-tab[2]"))
    )
    main1.click()
except:
    print("video find error")
try:
    main2 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "ytd-grid-renderer"))
    )
    titles = main2.find_elements_by_id("items")
    for title in titles:
        titlehead = title.find_element_by_class_name("style-scope ytd-channel-name")
        print(titlehead.text)

except:
    print("title find error")
#print(driver.page_source)
#time.sleep(5)
#print("done")
#driver.quit()
