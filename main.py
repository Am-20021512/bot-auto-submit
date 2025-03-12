from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Input data
name = "Ahmed Maher"
contact_number = "+201028098779"
city = "Cairo"

# Form URL
form_url = "https://docs.google.com/forms/d/e/1FAIpQLSeXQSGgV-fnleedkPjcEdFDdJ5AMDNaXHqWge2WtdK_VfudQg/viewform"

# Set up Chrome browser options
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

# Message counter
messages_sent = 0

# Run the bot infinitely
while True:
    driver.get(form_url)  # Open the form
    time.sleep(0.000001)  # Wait for the page to load

    try:
        # Find all the text fields
        fields = driver.find_elements(By.XPATH, "//input[@type='text']")

        # Enter data in the fields
        fields[0].send_keys(name)  # Name
        fields[1].send_keys(contact_number)  # Contact number
        fields[2].send_keys(city)  # City

        # Find the submit button and click it
        submit_button = driver.find_element(By.XPATH, "//span[text()='إرسال']")
        submit_button.click()

        # Update the counter
        messages_sent += 1
        print(f"✅ Data submitted successfully! (Total messages sent: {messages_sent})")

    except Exception as e:
        print(f"⚠️ Error: {e}")

    time.sleep(0.000001)  # Wait before restarting
    driver.refresh()  # Refresh the page
