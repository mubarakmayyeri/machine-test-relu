import csv
import requests
from bs4 import BeautifulSoup

# Load the ABN numbers from the CSV file
path = 'data/1000 ABN.csv'
abn_list = []
with open(path, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        abn_list.extend(row)

print(abn_list)

# # Dictionary to store the count of associations for each person
# associations_count = {}

# # Iterate over the ABN numbers
# for abn in abn_list:
#     # Construct the URL for the ACNC Charity Register website
#     url = f'https://www.acnc.gov.au/charity/{abn}'

#     # Send a GET request to the website
#     response = requests.get(url)

#     # Parse the HTML content of the response
#     soup = BeautifulSoup(response.content, 'html.parser')

#     # Find the People tab and extract the names of associated individuals
#     people_tab = soup.find('div', {'id': 'tab-people'})
#     if people_tab:
#         people_names = [name.text.strip() for name in people_tab.find_all('a')]
#         for name in people_names:
#             # Increment the count for the associated individual
#             associations_count[name] = associations_count.get(name, 0) + 1

# # Find the individual with the most charity associations
# most_associations = max(associations_count, key=associations_count.get)

# # Print the result
# print(most_associations)
