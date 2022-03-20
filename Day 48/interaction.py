from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "E:\gabriel\chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# article_count = driver.find_elements_by_css_selector("#articlecount a")
# # print(article_count.text)
# # article_count.click()
#
# all_portals = driver.find_element_by_partial_link_text("All portals")
# # all_portals.click()
#
# search = driver.find_element_by_name("search")
# search.send_keys("JoJo's Bizarre Adventure")
# search.send_keys(Keys.ENTER)

driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element_by_name("fName")
first_name.send_keys("Joe")
last_name = driver.find_element_by_name("lName")
last_name.send_keys("MaMa")
email = driver.find_element_by_name("email")
email.send_keys("sussy_amogus@mom.com")

submit = driver.find_element_by_css_selector("form button")
# submit.click()
