cutoff_list = [
("Pilani", "CS", 327),
("Pilani", "Eco", 271),
("Pilani", "Chemical", 239),
("Goa", "CS", 315),
("Goa", "Eco", 260),
("Goa", "Chemical", 230),
("Hyderabad", "CS", 310),
("Hyderabad", "Eco", 255),
("Hyderabad", "Chemical", 225)
]

cutoff_dict = {}

for campus, branch, marks in cutoff_list:
    if campus not in cutoff_dict:
        cutoff_dict[campus] = {}
    cutoff_dict[campus][branch] = marks

print(cutoff_dict)