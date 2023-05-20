import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# URL for the ACNC Charity Register website
url = f"https://www.acnc.gov.au/charity/charities?search="
# Path for the csv file of ABN numbers
path = 'data/1000 ABN.csv'

new_urls = []

# Load the ABN numbers from the CSV file
abn_numbers = []
with open(path, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        abn_numbers.extend(row)

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Open the ACNC Charity Register website


person_associations = {}

try:
    for abn in abn_numbers[1:]:
        driver.get(url + f'{abn}')

        time.sleep(5)

        link_element = driver.find_element(By.CSS_SELECTOR, "a.name")


        # Extract the URL from the href attribute
        link_url = link_element.get_attribute("href")

        url_parts = link_url.split('/')

        print(url_parts[5])

        new_url = f'https://www.acnc.gov.au/charity/charities/{url_parts[5]}/people'

        time.sleep(300)

        # driver.get(new_url)

        new_urls.append(new_url)


        # # Step 4: Click on the specified link within the results
        # result_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.name")))
        # result_link.click()

        # # Step 5: Click on the specified link containing the "People" span
        # people_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'nav-link') and span[text()='People']]")))
        # people_link.click()

        # # Step 6: Collect names of people
        # people_names = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.row.row-cols-1.row-cols-md-2.row-cols-lg-3.row-cols-xl-4.g-4 div.col h4.h5.card-title.text-primary")))
        # people_associations = {}

        # for person in people_names:
        #     associations = int(person.text.split()[0])  # Assuming the number of associations is at the beginning of the name
        #     name = person.text.split()[1]  # Assuming the person's name is the second word
        #     people_associations[name] = associations

        # # Step 7: Store the associations for the current ABN
        # person_associations[abn] = people_associations


    # # Find the person with the maximum association count across all ABNs
    # max_associations_person = max((person for associations in person_associations.values() for person in associations), key=person_associations.get)

    # print("The individual with the most charity associations is:", max_associations_person)

except Exception as e:
    print("An error occurred:", str(e))

finally:
    driver.quit()