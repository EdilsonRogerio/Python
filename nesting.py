# Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
    "Brazil": "Brasilia",
}

# Nesting a List in a dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
    "Brazil": ["São Paulo", "Ceará", "Rio De Janerio"],
}

# Nesting a dictionary in a dictionary
travel = {
    "France": {
        "Cities Visited": ["Paris", "Lille", "Dijon"],
        "Total Visits": 46
    },
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
    "Brazil": ["São Paulo", "Ceará", "Rio De Janerio"],
}

# print(travel["France"])

# Nesting a dictionary in a list
travel_list = [
    {
        "Country": "France",
        "Cities Visited": ["Paris", "Lille", "Dijon"],
    },
    {
        "Country": "Germany",
        "Cities Visited": ["Berlin", "Hamburg", "Stuttgart"],
    }
]

print(travel_list[0][0])
