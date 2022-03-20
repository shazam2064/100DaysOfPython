from selenium import webdriver

chrome_driver_path = "E:\gabriel\chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")

# price = driver.find_element_by_id("priceblock_ourprice")
# print(price.text)

# search_bar = driver.find_element_by_name("q")
# print(search_bar.get_attribute("placeholder"))

# logo = driver.find_element_by_class_name("python-logo")

# documentation_link = driver.find_element_by_css_selector(".documentation-widget a")
# print(documentation_link.text)

# bug_link = driver.find_element_by_xpath('//*[@id="container"]/li[5]/a')
# print(bug_link.text)

event_times = driver.find_element_by_css_selector(".event-widget time")
event_names = driver.find_element_by_css_selector(".event-widget li a")
events = {}

for time in event_times:
    print(time.text)

for name in event_names:
    print(name.text)

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n],
        "name": event_names[n],
    }

driver.quit()
