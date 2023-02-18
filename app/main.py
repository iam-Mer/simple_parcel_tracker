from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with

import time


def main():
    order_number = "820000000000"  # Your order number in lazada

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    # J&T Express PH uri for trace with track number
    driver.get("https://www.jtexpress.ph/index/query/gzquery.html")

    driver.find_element(By.ID, "billcode_list").send_keys(order_number + Keys.ENTER)

    driver.find_element(
        locate_with(By.TAG_NAME, "button").below({By.ID: "billcode_list"})
    ).click()

    time.sleep(10)

    driver.quit()


if __name__ == "__main__":
    main()
