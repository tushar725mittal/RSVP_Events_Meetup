from selenium import webdriver
from utils import auth, events, attend, groups
import sys


# write main function
def main():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome("./chromedriver", options=options)

    auth.auth_login(driver)
    grp_links = groups.extract_groups(driver)
    eventLinks = events.get_event_links(driver, grp_links)
    attend.click_attend(driver, eventLinks)


# call main function
if __name__ == "__main__":
    main()
