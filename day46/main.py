
# Rich Whiffen - 4/16/2023
#
# Udemy 100 Days of Code: The complete Python Pro Bootcamp for 2022
# Day 46 - using BeautifulSoup to scrape websites - spotify playless edition


from bs4 import BeautifulSoup
import requests
base_url = "https://www.billboard.com/charts/hot-100/" 

# found a class comment with this idea of functions - like it better
def get_http_page():
    date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
    response = requests.get(base_url + date)
    response.raise_for_status()
    html_doc = response.text 
    return html_doc

def get_songs_list(page):
    soup = BeautifulSoup(page, 'html.parser')
    songs_table = soup.find("div", "chart-results")
    songs = songs_table.find_all("h3", class_="a-no-trucate", id="title-of-a-story")
    songs_list = [song.text.strip() for song in songs] #just getting song names for now, should really do name + artist
    return songs_list

billboard_page = get_http_page()
song_names = get_songs_list(billboard_page)
print(song_names)