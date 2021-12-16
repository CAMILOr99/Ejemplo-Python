def run():
    my_list = [1,"Hello", True, 4.5]
    my_dict = {"firstname":"Camilo",
                "Lastname":"Rodriguez"}
#list of dictionarys
    super_list = [
        {"firstname":"Camilo","Lastname":"Rodriguez"},
        {"firstname":"Miguel","Lastname":"Torres"},
        {"firstname":"Pepe","Lastname":"Rodelo"},
        {"firstname":"Susana","Lastname":"Martinez"},
        {"firstname":"Jose","Lastname":"Garcia"},
    ]
#Dictionary of lists
    super_dict = {
        "natural_nums":[1, 2, 3, 4, 5],
        "integer_nums":[-1, -2, 0, 1, 2],
        "floating_nums": [1.1, 4.5, 6.43]
    }

    for key,value in super_dict.items():
        print(key, "-" , value)

    for item in super_list:
        print(item["firstname"], "-" , item["Lastname"])


if __name__ == "__main__":
    run()
