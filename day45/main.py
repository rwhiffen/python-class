
# Rich Whiffen - 12/15/2022
#
# Udemy 100 Days of Code: The complete Python Pro Bootcamp for 2022
# Day 45 - using BeautifulSoup to scrape websites.
#

from bs4 import BeautifulSoup

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

print(soup.title)
print(soup.title.string)


print(soup.prettify())


print(soup.p)

all_a_tags = soup.find_all(name="a")

print(all_a_tags)

for tag in all_a_tags:
    print(tag.get("href"))
