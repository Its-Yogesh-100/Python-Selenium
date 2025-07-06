from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://acciojob.com/data-science-and-ai")
wait = WebDriverWait(driver, 10)

# Open modal
wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "brochure"))).click()
time.sleep(1)

# Fill name and number
wait.until(EC.presence_of_element_located((By.ID, "name"))).send_keys("Harsh")
driver.find_element(By.ID, "mobile").send_keys("9876543210")

def select_dropdown(placeholder_text):
    # Click the dropdown button using visible text (e.g., 'Select State')
    button = wait.until(EC.element_to_be_clickable((By.XPATH, f"//button[contains(text(), '{placeholder_text}')]")))
    driver.execute_script("arguments[0].scrollIntoView(true);", button)
    button.click()

    # Wait for <ul> to appear and select first <li>
    try:
        first_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//ul[@role='listbox']//li[1]")))
        driver.execute_script("arguments[0].scrollIntoView(true);", first_option)
        first_option.click()
        print(f"✅ Selected first option for: {placeholder_text}")
    except:
        print(f"❌ Failed to select option for: {placeholder_text}")
        driver.quit()

# Select all dropdowns
select_dropdown("Select State")
select_dropdown("Select Degree")
select_dropdown("Select Graduation Year")
select_dropdown("Job Status")

# Submit
wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "modal-submit-btn"))).click()
print("✅ Form submitted")

time.sleep(3)
driver.quit()
