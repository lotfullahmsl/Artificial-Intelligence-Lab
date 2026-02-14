main_text = input("Enter the main string: ")
search_pattern = input("Enter the substring to search: ")

occurrence_count = 0
position = 0

while position <= len(main_text) - len(search_pattern):
    if main_text[position:position + len(search_pattern)] == search_pattern:
        occurrence_count += 1
        position += 1
    else:
        position += 1

print(occurrence_count)
