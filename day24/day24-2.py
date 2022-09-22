# Rich Whiffen - 9/22/2022
#
# Udemy 100 Days of Code: The complete Python Pro Bootcamp for 2022
# Day 24 - mail merge challenge - read and write files
#
# other files in this day are from the pre-packaged lessons (snake with high score)
#

DEBUG=True
REPLACE_STRING = "[name]"

with open("./input/names/invited_names.txt", "r") as merge_file:
    merge_list = merge_file.readlines()

with open("./input/letters/starting_letter.txt", "r") as letter_file:
    letter = letter_file.read()


for name in merge_list:
    if DEBUG:
        print(f"{name}")
    snipped_name = name.strip()
    merged_letter = letter.replace(REPLACE_STRING, snipped_name)
    if DEBUG:
        print(f"{merged_letter}")
    filename = "./output/readytosend/" + snipped_name + ".txt"
    if DEBUG:
        print(f"{filename}")
    with open( filename, "w")  as new_letter:
        new_letter.write(f"{merged_letter}")
