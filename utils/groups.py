import time
from utils.urls import grp_url


def extract_groups(driver):
    """Extracts the links of all the groups the user is a member of and returns them as a list"""
    driver.get(grp_url)
    time.sleep(10)
    elems = driver.find_elements(
        "xpath", "//ul[@data-testid='user-groups-data-section']//a[@href]"
    )
    print("Your groups are: ")
    grp_links = []
    for elem in elems:
        link = elem.get_attribute("href")
        grp_links.append(link)
        print(link)
    return grp_links
