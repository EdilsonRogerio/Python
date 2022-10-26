travel_list = [
    {
        "Country": "France",
        "Cities Visited": ["Paris", "Lille", "Dijon"],
    },
    {
        "Country": "Germany",
        "Cities Visited": ["Berlin", "Hamburg", "Stuttgart"],
    },
]

def add_new_country(country_visited, times_visited, cities_visited):
    add_country = {}
    add_country["Country"] = country_visited
    add_country["Cities Visited"] = cities_visited
    add_country["Times Visited"] = times_visited

    travel_list.append(add_country)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_list)