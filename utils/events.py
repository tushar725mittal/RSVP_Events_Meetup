import time


def get_event_links(driver, links):
    """Extracts the links of all the events from the groups where the user is a member and returns them as a list"""
    for link in links:
        driver.get(link + "/events")
        time.sleep(10)
        elems = driver.find_elements("xpath", "//a[@class='eventCard--link']")
        eventLinks = []
        for elem in elems:
            link = elem.get_attribute("href")
            eventLinks.append(link)
    return eventLinks
