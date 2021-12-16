DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Hector',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]


def run ():
    #List comprehensions
    all_python_devs = [worker["name"] for worker in DATA if worker["language"]=="python"]
    all_Platzi_workers = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]
    
    #Lambdas
    #-Filter
    adults = list(filter(lambda worker: worker["age"] > 18, DATA))
    #-Map
    adults = list(map(lambda worker: worker["name"], adults))
    #---add to dictionary with map to summary dictionarys "|"
    old_people = list(map(lambda worker: worker | {"old" : worker["age"] >70}, DATA))
    

    #CHALLENGE
    #all_python_devs filter and map
    all_python_devss = list(filter(lambda worker: worker["language"] == "python", DATA))
    all_python_devss = list(map(lambda worker: worker["name"], all_python_devss))
    #all_Platzi_workers filter and map
    all_Platzi_workerss = list(filter(lambda worker: worker["organization"] == "Platzi", DATA))
    all_Platzi_workerss = list(map(lambda worker: worker["name"], all_Platzi_workerss))
    #list adults with comprehensions
    adultss = [worker["name"] for worker in DATA if worker["age"] > 18]
    #list old people with comprehensions
    old_peoplee = [{**worker, **{'old': worker['age'] > 70}} for worker in DATA]

    #Prints
    print("Workers with Python")
    for worker in all_python_devs:
        print(worker)
    print(" ")
    print("Workers in Platzi")
    for worker in all_Platzi_workers:
        print(worker)
    print(" ")
    print("Workers that are adults")
    for worker in adults:
        print(worker)
    print(" ")
    print("Workers that are olds")
    for worker in old_people:
        print(worker)

    #PRINTS CHALLENGE
    print("---------------------------")
    print("CHALLENGE")
    print("Workers with Python (filter and map)")
    for worker in all_python_devss:
        print(worker)
    print(" ")
    print("Workers in Platzi (filter and map)")
    for worker in all_Platzi_workerss:
        print(worker)
    print(" ")
    print("Workers that are adults (Comprehensions)")
    for worker in adultss:
        print(worker)
    print(" ")
    print("Workers that are olds (Comprehensions)")
    for worker in old_peoplee:
        print(worker)


if __name__ == "__main__":
    run()