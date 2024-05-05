import requests
from bs4 import BeautifulSoup

# keywords = ["flutter", "python", "golang"]
#
# r = requests.get(
#     f"https://remoteok.com/remote-{keywords}-jobs",
#     headers={
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
#     },
# )

# print(r.status_code)

## job scraping

url = "https://remoteok.com/remote-flutter-jobs"

print(f"Scrapping {url}...")
response = requests.get(
    url,
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    },
)
soup = BeautifulSoup(
    response.content,
    "html.parser",
)

job = (
    soup.find("table", id="jobsboard")
    .find("td", class_="company position company_and_position")
    .find_all("a")
)
print(job)
# .find("tbody")

# for job in jobs:
#     title = job.find("span", class_="title").text
#     company, position, region = job.find_all("span", class_="company")[:3]
#     try:
#         url = job.find("div", class_="tooltip--flag-logo").next_sibling["href"]
#     except:
#         url = None
#     if url == None:
#         job_data = {
#             "title": title,
#             "company": company.text,
#             "position": position.text,
#             "region": region.text,
#             "url": None,
#         }
#     else:
#         job_data = {
#             "title": title,
#             "company": company.text,
#             "position": position.text,
#             "region": region.text,
#             "url": f"https://weworkremotely.com{url}",
#         }
#     all_jobs.append(job_data)
