import requests
from bs4 import BeautifulSoup

url = "https://www.belastingdienst.nl/wps/wcm/connect/bldcontenten/belastingdienst/individuals/tax-regulations/tax_treaties/list-of-eu-countries/list-of-eu-countries#:~:text=The%20countries%20of%20the%20European%20Union%20%28EU%29%20are%3A,Czech%20Republic%207%20Denmark%208%20Estonia%20Weitere%20Elemente"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
blog_titles = soup.findAll(attrs={"class":"content_main"})

for title in blog_titles:
    print(title.text)

#text co chceme je jen v ul toho divu, tedy musíme najít jen způsob, jak vytisknout jen tuhle část. 
