# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day',
         'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen',
         'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix',
         'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September',
          'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August',
          'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September',
          'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980,
         1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185,
                       160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'],
                  ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'],
                  ['The Bahamas', 'Northeastern United States'],
                  ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'],
                  ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'],
                  ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'],
                  ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'],
                  ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'],
                  ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'],
                  ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'],
                  ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'],
                  ['The Caribbean', 'United States East coast'],
                  ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'],
                  ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'],
                  ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'],
                  ['Central America', 'Yucatn Peninsula', 'South Florida'],
                  ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'],
                  ['The Caribbean', 'Venezuela', 'United States Gulf Coast'],
                  ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'],
                  ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'],
                  ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'],
                  ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'],
                  ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'],
                  ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic',
                   'Turks and Caicos Islands'],
                  ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M',
           '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B',
           '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B',
           '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90, 4000, 16, 3103, 179, 184, 408, 682, 5, 1023, 43, 319, 688, 259, 37, 11, 2068, 269, 318, 107, 65, 19325,
          51, 124, 17, 1836, 125, 87, 45, 133, 603, 138, 3057, 74]

# 2
# Update Recorded Damages
conversion = {"M": 1000000, "B": 1000000000}


def convert_damages(list_of_damages):
    converted_list = []
    for damage in list_of_damages:
        if damage[-1:] == "B":
            converted_list.append(float(damage[:-1]) * conversion["B"])
        elif damage[-1:] == "M":
            converted_list.append(float(damage[:-1]) * conversion["M"])
        else:
            converted_list.append('Damages not recorded')
    return converted_list


# test function by updating damages
hurricane_damage_list = (convert_damages(damages))
print("================Hurricane Damage List====================")
print(hurricane_damage_list)

# 3
# take away
hurricanes = {}


def construct_hurricanes_dict(names, months, years, max_sustained_winds, areas_affected, hurricane_damage_list, deaths):
    for i in range(len(names)):
        hurricanes[names[i]] = {
            'Name': names[i],
            'Month': months[i],
            'Year': years[i],
            'Max Sustained Wind': max_sustained_winds[i],
            'Areas Affected': areas_affected[i],
            'Hurricane_damage': hurricane_damage_list[i],
            'Deaths': deaths[i]}
    return hurricanes


# this is our table
print("==============Hurricanes Dictionary======================")
print(
    construct_hurricanes_dict(names, months, years, max_sustained_winds, areas_affected, hurricane_damage_list, deaths))

print("====================================")
print(hurricanes["Cuba I"])


# 4 using our table from above, create function to return hurricanes by year
def hurricanes_by_year(year):
    hurricane_by_year = []
    for name in hurricanes:
        if hurricanes[name]['Year'] == year:
            hurricane_by_year.append(hurricanes[name])
    return hurricane_by_year


print("=================Hurricanes By Year===================")
print(hurricanes_by_year(1932))

# 5
hurricanes_by_area_dict = {}


def hurricanes_by_area(dict):
    for name in dict:
        for area in dict[name]['Areas Affected']:
            if area in hurricanes_by_area_dict:
                hurricanes_by_area_dict[area] += 1
            else:
                hurricanes_by_area_dict[area] = 1
    return hurricanes_by_area_dict


print("=================Hurricanes by Areas===================")
print(hurricanes_by_area(hurricanes))

# 6
max_hurricanes_dict = {}


def max_hurricanes(dict):
    max_key = max(hurricanes_by_area_dict, key=hurricanes_by_area_dict.get)
    for value in hurricanes_by_area_dict:
        if value == max_key:
            return max_key, hurricanes_by_area_dict[max_key]


print("==================Max Hurricanes==================")
print(max_hurricanes(hurricanes_by_area_dict))


# 7
def max_deaths(dict):
    max_death = 0
    hurricane_name = ''
    for name in dict:
        if dict[name]['Deaths'] > max_death:
            max_death = dict[name]['Deaths']
            hurricane_name = name
    return hurricane_name, max_death


print("=================Max Deaths===================")
print(max_deaths(hurricanes))

# 8
hurricane_mortality = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}


def mortality_by_rating(dict):
    mortality_scale = {0: 0,
                       1: 100,
                       2: 500,
                       3: 1000,
                       4: 10000}
    for name in dict:
        deaths = dict[name]['Deaths']
        if deaths == mortality_scale[0]:
            hurricane_mortality[0] = name
        elif mortality_scale[0] < deaths <= mortality_scale[1]:
            hurricane_mortality[1].append(name)
        elif mortality_scale[1] < deaths <= mortality_scale[2]:
            hurricane_mortality[2].append(name)
        elif mortality_scale[2] < deaths <= mortality_scale[3]:
            hurricane_mortality[3].append(name)
        elif mortality_scale[3] < deaths <= mortality_scale[4]:
            hurricane_mortality[4].append(name)
        else:
            hurricane_mortality[5].append(name)
    return hurricane_mortality


print("================Mortality By Rating====================")
print(mortality_by_rating(hurricanes))


# print(hurricanes['Cuba I']['Hurricane_damage'])

# 9
def greatest_damage(dict):
    max_damage = 0
    hurricane_name = ''
    for name in dict:
        if dict[name]['Hurricane_damage'] == 'Damages not recorded':
            continue
        if dict[name]['Hurricane_damage'] > max_damage:
            max_damage = dict[name]['Hurricane_damage']
            hurricane_name = name
    return hurricane_name, max_damage


print("================Greatest Damage====================")
print(greatest_damage(hurricanes))

# 10
hurricanes_damage = {0: [], 1: [], 2: [], 3: [], 4: []}


def hurricanes_by_damage(dict):
    damage_scale = {0: 0,
                    1: 100000000,
                    2: 1000000000,
                    3: 10000000000,
                    4: 50000000000}

    for name in dict:
        damage = dict[name]['Hurricane_damage']

        if damage == 'Damages not recorded':
            continue
        if damage == damage_scale[0]:
            hurricanes_damage[0] = name
        elif damage_scale[0] < damage <= damage_scale[1]:
            hurricanes_damage[1].append(name)
        elif damage_scale[1] < damage <= damage_scale[2]:
            hurricanes_damage[2].append(name)
        elif damage_scale[2] < damage <= damage_scale[3]:
            hurricanes_damage[3].append(name)
        else:
            hurricanes_damage[4].append(name)
    return hurricanes_damage


print("================Damage By Rating====================")
print(hurricanes_by_damage(hurricanes))

# 2
# Create a Table
# wtf?

# 3
# Organizing by Year

# create a new dictionary of hurricanes with year and key


# 4
# Counting Damaged Areas

# create dictionary of areas to store the number of hurricanes involved in


# 5
# Calculating Maximum Hurricane Count

# find most frequently affected area and the number of hurricanes involved in


# 6
# Calculating the Deadliest Hurricane

# find highest mortality hurricane and the number of deaths

# 7
# Rating Hurricanes by Mortality


# categorize hurricanes in new dictionary with mortality severity as key


# 8 Calculating Hurricane Maximum Damage

# find highest damage inducing hurricane and its total cost


# 9
# Rating Hurricanes by Damage
# damage_scale = {0: 0,
#                 1: 100000000,
#                 2: 1000000000,
#                 3: 10000000000,
#                 4: 50000000000}

# categorize hurricanes in new dictionary with damage severity as key
