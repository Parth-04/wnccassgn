import pandas as pd
from bs4 import BeautifulSoup
import requests
from tabulate import tabulate
import html


html_text = requests.get('https://itc.gymkhana.iitb.ac.in/wncc/soc/').text
soup = BeautifulSoup(html_text,'lxml')
project = soup.find_all('div', class_ = 'col-lg-4')

data = []

for i in range(len(project)):
    item = project[i]
    if (i == 54):
        project_name = '\"The Watchdogs\" -Solving a murder mystery using Computer Vision and Data Science'
    else:
        project_name = item.find('p', class_ = 'lead').text
    print("Project: ",project_name)

    project_link = 'https://itc.gymkhana.iitb.ac.in'+item.a['href']

    proj_text = requests.get(project_link).text
    proj_soup = BeautifulSoup(proj_text,'lxml')

    mentor_list = proj_soup.find('h4', class_ = 'display3').find_next_sibling('ul').find_all('li')
    print("Mentor(s):")
    mentors = ''
    for j in mentor_list:
        print('*'+j.text)
        mentors += j.text + ', '
    

    mentee = proj_soup.find('h4', class_ = 'display3').find_next_sibling('ul').find_next_sibling('ul').find('li').text
    print("Number of Mentees:",mentee)
    
    tent_table = proj_soup.find('div', class_ = 'd-flex').find('h4', class_ = 'display3').find_next_sibling('table')
    headers = [th.get_text(strip=True) for th in tent_table.find_all('th')]
    rows = tent_table.find_all('tr')
    table_data = []
    for row in rows:
        cells = row.find_all('td')
        row_data = [cell.get_text(strip=True) for cell in cells]
        table_data.append(row_data)
    print(tabulate(table_data, headers=headers, tablefmt='grid'))

    print("Project Description: ",project_link)
    print()



    row_var = [project_name, mentors, mentee, project_link]
    row_dict = {'Project Name':row_var[0], 'Mentor List':row_var[1], 'Number of Mentees':row_var[2], 'More Information':row_var[3]}
    data.append(row_dict)

df = pd.DataFrame(data)
pd.set_option('display.max_columns', None)
df = df.dropna(how='all')
df = df.drop_duplicates()
df.to_csv('data.csv', index=False)
df.to_excel('data.xlsx', index=False)
print(df)

    
