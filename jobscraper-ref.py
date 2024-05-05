import requests
from bs4 import BeautifulSoup


def scrap_page(url):
    response = requests.get(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
        },
    )

    soup = BeautifulSoup(response.text, "html.parser")
    jobs = soup.find("table", id="jobsboard").find_all(
        "td", class_="company position company_and_position"
    )

    all_jobs = []

    for job in jobs:
        title_element = job.find("h2", itemprop="title")
        if title_element:
            title = title_element.text.strip()
        else:
            title = "Title not found"

        company_element = job.find("h3", itemprop="name")
        if company_element:
            company = company_element.text.strip()
        else:
            company = "Company not found"

        location_element = job.find("div", class_="location")
        if location_element:
            location = location_element.text.strip()
        else:
            location = "Location not found"

        salary_element = job.find("div", class_="location tooltip")
        if salary_element:
            salary_info = salary_element.text.strip()
        else:
            salary_info = "Salary information not found"

        job_url_element = job.find("a", class_="preventLink")
        if job_url_element:
            job_url = "https://remoteok.com" + job_url_element.get("href")
        else:
            job_url = "URL not found"

        print("Job Title:", title)
        print("Company Name:", company)
        print("Location:", location)
        print("Salary Information:", salary_info)
        print("Job URL:", job_url)
        print()

        job_data = {
            "title": title,
            "company": company,
            "location": location,
            "url": job_url,
        }
        all_jobs.append(job_data)

    return all_jobs


def main():
    keywords = ["flutter", "ios", "python"]

    for keyword in keywords:
        scrap_page(f"https://remoteok.com/remote-{keyword}-jobs")


main()
