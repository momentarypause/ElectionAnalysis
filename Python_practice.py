# counties = ["Arapahoe","Denver","Jefferson"]
# if "El Paso" in counties:
#     print("El Paso is in the list of counties")
# else:
#     print("El Paso is not in the list of counties")

# for county in counties:
#     print(county)



county_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
voting_data = [{"county": "Arapahoe", "registered_voters": 422829},
                {"county": "Denver", "registered_voters": 463353},
                {"county": "Jefferson", "registered_voters": 432438}]


# for county in counties_dict.keys():
#     print(county)

# for county in counties_dict:
#     print(counties_dict[county])


# for county, registered_voters in county_dict.items():
#     print(county +  "county has" +  str(registered_voters) +  "registered voters")
    
for county, voters in county_dict.items():
    print(f"{county} county has {voters:,} registered voters")