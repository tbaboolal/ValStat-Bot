from seleniumbase import Driver
from bs4 import BeautifulSoup
import time


def valorant_stats(username):


    #Create Web Driver Instance using undetected chromedriver to bypass bot filters
    driver = Driver(uc=True)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})") 


    #Change username to live url for tracker.gg
    username = username.replace("#","%23")
    url = 'https://tracker.gg/valorant/profile/riot/'+username+'/overview'


    try:
        #open the webdriver and navigate to this address.
        driver.get(url)
        #Allow the page to load all dynamic content
        time.sleep(5)
        
        #Store the html code into html_text
        html_text = driver.page_source

        #Use BeautifulSoup to parse there the html code
        soup = BeautifulSoup(html_text, 'lxml')
    finally:

        #close webdriver
        driver.quit()           
    
    #Get act stats and profile url
    stats = soup.find_all('div', class_="numbers")
    profile = soup.find('img', class_="user-avatar__image")


    if len(stats) == 0:
        return False
    else:

        #Create file and write to it the player stats.
        with open ('player_stat.txt', 'w', encoding='utf-8') as f:

            #Write to file the current rank text
            f.write(soup.find('h2').text+"\n")

            #Write to file the users profile URL
            f.write(profile['src']+"\n")

            #Write all the act stats into the textfile
            for stat in stats:
                f.write(stat.find("span", class_ = "name").text+ "#"+stat.find("span", class_ = "value").text+"#")
            f.write("\n")
            
            
    
    

if __name__ == "__main__":
    valorant_stats()