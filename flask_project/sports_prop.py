import requests
from bs4 import BeautifulSoup

def player_props(sport):
    url = f"https://www.pine-sports.com/stats/props/{sport}/"
    site = requests.get(url)
    #print("\nAnaylzing data from:\n", url , '\n--------------------------------------------------------------')
    soup = BeautifulSoup(site.text,'html.parser')
    results = soup.find("div",id="props")
    table_elements = results.find("table")

    head = table_elements.find("thead")
    head_contents=head.find("tr").find_all("th")
    head_list =[]
    for x in head_contents[:-1]:
        head_list.append(x.text)

    body = table_elements.find("tbody")
    body_contents = body.find_all("tr")
    over_list = []
    under_list = []
    for x in body_contents:
        contents = x.find_all("td")
        dict = {}
        i = 0
        for x in contents[:-1]:
            dict[head_list[i]] = x.text
            i+= 1
        
        if int(dict['Over Count']) >= 8 and int(dict['Over ML']) >= -150:
            if float(dict['Projection']) > float(dict['Mean']):
                over_list.append(dict)
        elif int(dict['Under Count']) >= 9 and int(dict['Under ML']) >= -150:
            if float(dict['Projection']) < float(dict['Mean']):
                under_list.append(dict)
        else:
            pass
        
    sorted_over_list = sorted(over_list, key=lambda x: x['Over ML'], reverse = True)
    sorted_under_list = sorted(under_list, key=lambda x: x['Under ML'], reverse = True)
    return sorted_over_list , sorted_under_list