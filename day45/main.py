
# Rich Whiffen - 12/15/2022
#
# Udemy 100 Days of Code: The complete Python Pro Bootcamp for 2022
# Day 45 - using BeautifulSoup to scrape websites.
#
# picking this back up in April (yikes) - didn't change much just
# reviewing this lesson to jump into the next.

from bs4 import BeautifulSoup

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

print("title html")
print(soup.title)
print("title string")
print(soup.title.string)


print(soup.prettify())


print(soup.p)

all_a_tags = soup.find_all(name="a")

print(all_a_tags)

print ("loop through the href tags")
for tag in all_a_tags:
    print(tag.get("href"))


heading = soup.find(name="h1", id="name")
print(heading)

#print the value of a variable - need to review what the _ is for in class_
section_heading = soup.find(name="h3", class_="heading")
print(section_heading.get("class"))