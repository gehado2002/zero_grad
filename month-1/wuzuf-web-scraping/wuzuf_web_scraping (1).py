import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def scrap():
    def web_scraping(job_name, num_pages):
        all_titles = []
        all_links = []
        all_companies = []
        all_specs = []
        all_occupations = []

        for num_page in range(num_pages):
            url = f'https://wuzzuf.net/search/jobs/?a=hpb&q={job_name.replace(" ","%20")}&start={num_page}'

            try:
                response = requests.get(url, timeout=10)
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                print(f"Error fetching page {num_page+1} for '{job_name}': {e}")
                continue

            soup = BeautifulSoup(response.content, 'lxml')

            titles = [title.text.strip() for title in soup.find_all("h2", {"class":"css-m604qf"})]
            all_titles.extend(titles)

            links = [link.a["href"] for link in soup.find_all("div", {"class":"css-pkv5jc"}) if link.a and "href" in link.a.attrs]
            all_links.extend(links)

            occupations = [occupation.text.strip() for occupation in soup.find_all("div", {"class":"css-1lh32fc"})]
            all_occupations.extend(occupations)

            companies = [company.text.replace(' -','').strip() for company in soup.find_all("a", {"class":"css-17s97q8"})]
            all_companies.extend(companies)

            specs = [spec.text.strip() for spec in soup.find_all("div", {"class":"css-y4udm8"})]
            all_specs.extend(specs)

            print(f"Scraping page {num_page+1} for '{job_name}'...")
            time.sleep(1)  # تأخير بسيط لتجنب الحظر

        return all_titles, all_links, all_companies, all_specs, all_occupations

    for job_name in ["data analysis", "data science", "business intelligence"]:
        titles, links, companies, specs, occupations = web_scraping(job_name, 5)

        dic = {
            'titles': titles,
            'links': links,
            'companies': companies,
            'specs': specs,
            'occupations': occupations
        }

        df = pd.DataFrame.from_dict(dic, orient='index').transpose()
        df.to_csv(f'{job_name}_jobs_in_egypt.csv', index=False)
        print(f"🛤️ {job_name} jobs scraped successfully\n")

    print("😀 Done")
    return df

if __name__ == "__main__":
    scrap()
