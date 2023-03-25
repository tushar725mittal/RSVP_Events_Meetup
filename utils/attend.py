import time
from selenium.webdriver.common.action_chains import ActionChains


def click_attend(driver, eventLinks):
    """Clicks the attend button on all the events for the events in the eventLinks list"""
    print("You are RSVPing for the following events: ")
    actions = ActionChains(
        driver
    )  # need to create actions to move to button element because we need to scroll to click
    for link in eventLinks:
        driver.get(link)
        time.sleep(10)
        element = driver.find_element(
            "xpath",
            "//button[@data-testid='attend-online-btn'] | //button[@data-testid='attend-irl-btn']",
        )
        if element:
            actions.move_to_element(element).click().perform()
        print(link)
