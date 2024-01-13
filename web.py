import requests
from bs4 import BeautifulSoup
import csv


url="https://www.bikewale.com/yamaha-bikes/"
yamaha=requests.get(url)

soup=BeautifulSoup(yamaha.content,'html.parser')


#gathering images

# images=soup.findAll('div',class_="o-brXWGL")
# list_of_tags=[]
# for i in images:
#     img_tag = i.find('img')
#     if img_tag is not None and 'src' in img_tag.attrs:
#         j = img_tag['src']
#         list_of_tags.append(j)
# print(list_of_tags)




#text

# finding_txt = soup.findAll('div', class_="o-brXWGL")
# list_of_texts = []

# for i in finding_txt:
#     link = i.find('a')
#     if link is not None:
#         link_text = link.get_text()  #we can use strip=True as argument to get_text method if needed
#         list_of_texts.append(link_text)

# print(list_of_texts)


#storing data using csv
 
finding_links = soup.find_all('div', class_="o-brXWGL")

# Extract the links
list_of_links = []
for div_element in finding_links:
    link = div_element.find('a')
    if link is not None and 'href' in link.attrs:
        link_href = link['href']
        list_of_links.append(link_href)

# Write the data to a CSV file
csv_filename = 'data.csv'
with open(csv_filename, 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)

    # file heading 
    csv_writer.writerow(['All Links'])

    # Write each link as a row
    for link in list_of_links:
         csv_writer.writerow([link,soup.prettify()])
       
       
print(f'Data written to {csv_filename}')
        
