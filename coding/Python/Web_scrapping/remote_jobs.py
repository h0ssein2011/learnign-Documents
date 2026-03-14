from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
import pandas as pd

import time

# Initialize the WebDriver (make sure to download the correct driver for your browser)
driver = webdriver.Chrome()
service = Service(executable_path='/Users/hossein/Downloads/chromedriver-mac-arm64/chromedriver')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)


# Open the URL
driver.get("https://jobs.smartrecruiters.com/?keyword=data%20analyst&locationType=remote")

# Wait for the page to fully render (you can adjust the time)
time.sleep(5)

# Get the page source
html = driver.page_source

# Parsing the HTML with BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')
job_items = soup.find_all("a", {"class": "job"})

# df = pd.DataFrame(columns=['id','job_title','url','company_name'])
df = pd.read_excel('df.xlsx')
# Loop through job_items and print the job title
for job in job_items:
    title = job.find("h3", {"class": "job-title"}).text
    job_details = job.find("ul", {"class": "job-details"})
    if job_details:
        # Get the first <li> element which contains the company name
        company_name = job_details.find("li").text
    else:
        company_name = None

    link = job['href']
    id = link.split("/")[-1]
    id = id.split("-")[0]
    new_row = pd.DataFrame([[id,title, link,company_name]], columns=['id','job_title', 'url','company_name'])
    df = pd.concat([df, new_row], ignore_index=True)


# Close the browser
driver.quit()
df['id'].astype(int)
df = df.drop_duplicates(subset=['job_title','company_name'])
df.to_excel('df.xlsx',index=False)



