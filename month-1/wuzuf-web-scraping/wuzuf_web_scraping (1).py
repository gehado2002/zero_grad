import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrap():
    def web_scraping(job_name,num_pages):

        all_titles=[]
        all_links=[]
        all_companies=[]
        all_specs=[]
        all_occupations=[]
        for num_page in range(num_pages):
            url=f'https://wuzzuf.net/search/jobs/?a=hpb&q={job_name.replace(" ","%20")}\
             %20jobs%20in%20egypt&start={num_page}'
            response=requests.get(url)

            soup=BeautifulSoup(response.content,'lxml')


            titles=soup.find_all("h2",{"class":"css-m604qf"})
            titles=[title.text for title in titles]
            all_titles.extend(titles)


            links=soup.find_all("div",{"class":"css-pkv5jc"})
            links = [link.a["href"] for link in links if link.a and "href" in link.a.attrs]
            all_links.extend(links)


            occupations=soup.find_all("div",{"class":"css-1lh32fc"})
            occupations=[occupation.text for occupation in occupations ]
            all_occupations.extend(occupations)

            companies=soup.find_all("a",{"class":"css-17s97q8"})
            companies=[company.text.replace(' -','') for company in companies]
            all_companies.extend(companies)


            specs=soup.find_all("div",{"class":"css-y4udm8"})
            specs=[spec.text for spec in specs]
            all_specs.extend(specs)
            print(f"Scraping data for '{job_name}'...")
        return all_titles, all_links, all_companies, all_specs, all_occupations

    for job_name in ["data analysis" , "data science" , "business intelligence"]:
            titles, links, companies, specs, occupations= web_scraping(job_name, 5)

            dic={}
            dic['titles']=titles
            dic['links']=links
            dic['companies']=companies
            dic['specs']=specs
            dic['occupations']=occupations

            df = pd.DataFrame.from_dict(dic, orient='index').transpose()
            df.to_csv(f'{job_name}_jobs_in_egypt.csv',index=False)
            print(f"🛤️{job_name} jobs scraped successfully\n")

    print("😀Done")
    return df

if __name__ == "__main__":
    scrap()
