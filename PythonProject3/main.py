
file_name = "new_file.txt"
line_count =0
with open(file_name, 'r') as file:
    for line in file:
        line_count += 1

print(f"Total number of lines in '{file_name}': {line_count}")

