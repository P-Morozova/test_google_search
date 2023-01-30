from selenium.webdriver.common.by import By
import time


def test_google_search(driver):
    driver.get("https://www.google.com/")
    search_text = "QA engineer"
    title_before_search = driver.find_element(By.XPATH, "/html[1]/head[1]/title[1]")
    driver.find_element(By.XPATH, "//body//input[1]").send_keys(search_text)

    time.sleep(1)
    driver.find_element(By.XPATH, "//body//center[1]/input[1]").click()

    title_after_search = driver.find_element(By.XPATH, "/html[1]/head[1]/title[1]")

    assert title_before_search != title_after_search, "Title didn't change after search, expected that change."

    header_text = driver.find_element(By.XPATH, "//body/div[@id='main']/div[@id='cnt']/div[@id='rcnt']//h3[1]").text.lower()
    search_text_lower = search_text.lower()

    assert header_text.__contains__(
        search_text_lower), "Header of first result not contain search text, expected: " + search_text