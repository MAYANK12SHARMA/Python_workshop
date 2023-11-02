# wap a python program to sort a given dictonary by key

color_dict = {
    "red": "#ff0001",
    "green": "#ff0202",
    "black": "#ff0451",
    "white": "#ff451278"
}

dict = sorted(color_dict)
print(dict)

# without sort function
color_dict = {
    "red": "#ff0001",
    "green": "#ff0202",
    "black": "#ff0451",
    "white": "#ff451278"
}

# Custom sorting function
def sort_dict(input_dict):
    sorted_dict = {}
    keys = list(input_dict.keys())
    keys.sort()  # Sorting the keys alphabetically
    for key in keys:
        sorted_dict[key] = input_dict[key]
    return sorted_dict

sorted_color_dict = sort_dict(color_dict)

# Output the sorted dictionary
print("Sorted Dictionary by Key:")
print(sorted_color_dict)





















# # Sorting the dictionary by keys in ascending order
# sorted_color_dict = dict(sorted(color_dict.items(), key=lambda item: item[0]))

# print("Original Dictionary:", color_dict)
# print("Sorted Dictionary by Keys:", sorted_color_dict)
