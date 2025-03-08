import requests
from bs4 import BeautifulSoup

def scrape_jobs():
    url = "https://weworkremotely.com/categories/remote-programming-jobs"

    # Add detailed headers to mimic a real browser request
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://weworkremotely.com/"
    }

    response = requests.get(url, headers=headers)

    print(f"🌐 Requesting: {url}")  # Debugging
    print(f"🔄 Response Status Code: {response.status_code}")  # Print status code
    print(f"📝 First 500 chars of response: {response.text[:500]}")  # Print part of response content

    if response.status_code != 200:
        print("❌ Error: Failed to retrieve job listings.")
        return {"error": "Failed to retrieve job listings"}

    # Use lxml parser for XML data
    soup = BeautifulSoup(response.text, "xml")
    job_listings = []

    job_posts = soup.find_all("item")
    print(f"🔍 Found {len(job_posts)} job listings")  # Debugging output

    for job in job_posts:
        title_tag = job.find("title")
        link_tag = job.find("link")
        description_tag = job.find("description")

        if title_tag and link_tag:
            title = title_tag.text.strip()
            job_link = link_tag.text.strip()
            description = description_tag.text.strip() if description_tag else "No description available."

            job_listings.append({
                "title": title,
                "link": job_link,
                "description": description
            })

    print(f"✅ Returning {len(job_listings)} jobs")
    return job_listings
