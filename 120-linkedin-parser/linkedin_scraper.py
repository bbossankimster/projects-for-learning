import requests
import settings
from bs4 import BeautifulSoup

client = requests.Session()

HOMEPAGE_URL = 'https://www.linkedin.com'
LOGIN_URL = 'https://www.linkedin.com/uas/login-submit'
CONNECTIONS_URL = 'https://www.linkedin.com/mynetwork/invite-connect/connections/'
SEARCH_URL = 'https://www.linkedin.com/jobs/search/?f_TP=1%2C2&f_TPR=r604800&geoId=101620260&keywords=bgp&location=Israel&sortBy=DD&redirect=false&position=1&pageNum=0'
APL_LINK = 'https://www.linkedin.com/jobs/tracker/applied/'


html = client.get(SEARCH_URL).content
soup = BeautifulSoup(html, "html.parser")
search_result = []
srch_date = {}

#link, date, company, location, position
# date
for JobPostings in soup.find_all('time', attrs={'class' : ['job-result-card__listdate', 'job-result-card__listdate--new']}):
    srch_date['date'] = JobPostings.text
    search_result.append(srch_date)
    srch_date = {}
# company
i = 0
for JobPostings in soup.find_all('a',class_="result-card__subtitle-link job-result-card__subtitle-link"):
    search_result[i]['company'] = JobPostings.text
    i += 1
# location
i = 0
for JobPostings in soup.find_all('span', attrs={'class' : 'job-result-card__location'}):
    search_result[i]['location'] = JobPostings.text.replace(", Tel Aviv, Israel", "").replace("Central, Israel","Central").replace("Israel", "")
    i += 1
# position
i = 0
for JobPostings in soup.find_all('span', attrs={'class' : 'screen-reader-text'}):
    search_result[i]['position'] = JobPostings.text
    i += 1
#link, date, company, location, position
for j in range(len(search_result)):
    a = search_result[j]['date']
    b = search_result[j]['company']
    c = search_result[j]['location']
    d = search_result[j]['position'].replace("Radware","Radware      ")
    company_n = b.upper() + " " + c
    print(b[0:14:1], c, d[0:14:1], a[0:14:1], sep='\t|')