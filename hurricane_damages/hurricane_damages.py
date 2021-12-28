# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages


conversion = {"M": 1000000,
              "B": 1000000000}

def damages_to_float():
  float_damages = []
  length = len(damages)
  i = 0
  while i < length:
    if not damages[i]:
      float_damages.append('Damages not recorded')
    else:
      if damages[i][-1] == 'M' or damages[i][-1] == 'B':
        float_num = float(damages[i][:-1])
        char = conversion[damages[i][-1]]
        if float_num > 0:
          float_damages.append(float_num * char)
        else:
          float_damages.append('Damages not recorded')
      else:
        float_damages.append('Damages not recorded')
    i += 1
  return float_damages

# test function by updating damages

# damages.extend(["","000","0M","5M", "0.7B"])
float_damages_list = damages_to_float()
#print(damages_to_float())


# 2 
# Create a Table

hurricane_records = list(zip(names,months,years,max_sustained_winds,areas_affected,float_damages_list,deaths))
#print(hurricane_records)

# Create and view the hurricanes dictionary

hurricane_dict = {}
for record in hurricane_records:
  values = {}
  keys = ["Name","Month","Year","Max Sustained Wind","Areas Affected","Damages","Deaths"]
  index = 0
  for data in record:
    values.update({keys[index]:data})
    index += 1
  hurricane_dict.update({record[0]:values})
#print(hurricane_dict)


# 3
# Organizing by Year

year_hurricane_dict = {}
for hurricane, value in hurricane_dict.items():
  year_hurricane_dict.update({value["Year"]:[]})
# print(year_hurricane_dict)
# create a new dictionary of hurricanes with year and key
for year in year_hurricane_dict:
  for hurricane, value in hurricane_dict.items():
    if year == value["Year"]:
      year_hurricane_dict[year].append(value)
#print(year_hurricane_dict[1932])


# 4
# Counting Damaged Areas
def how_often_affected_areas():
  affected_areas_dict = {}
  areas_list = []
  for value in hurricane_dict.values():
    for area in value["Areas Affected"]:
      areas_list.append(area)
  for area in areas_list:
    count = areas_list.count(area)
    affected_areas_dict.update({area:count})
    i = 0
    while i < count:
      areas_list.remove(area)
      i += 1
  return affected_areas_dict

# create dictionary of areas to store the number of hurricanes involved in

count_affected_areas = how_often_affected_areas()
#print(count_affected_areas)

# 5 
# Calculating Maximum Hurricane Count

# find most frequently affected area and the number of hurricanes involved in

def max_hurricane_count():
  max_value = -1
  most_affected_places = []
  for area,count in count_affected_areas.items():
    if count > max_value:
      max_value = count
      most_affected_places.append(area)
  max_place = most_affected_places[-1]
  print("The most affected area was {area}, with {max} hurricanes.".format(area=max_place,max=max_value))
#max_hurricane_count()


# 6
# Calculating the Deadliest Hurricane
def deadliest_hurricane():
  max_mortality = -1
  possible_hurricanes = []
  for record in hurricane_dict.values():
    name = record["Name"]
    deaths = record["Deaths"]
    if deaths > max_mortality:
      max_mortality = deaths
      possible_hurricanes.append(name)
  print("The deadliest hurricane was {hurricane} with {X} deaths.".format(hurricane=possible_hurricanes[-1],X=max_mortality))

# find highest mortality hurricane and the number of deaths

#deadliest_hurricane()


# 7
# Rating Hurricanes by Mortality

mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}
                   
mortality_hurricane_dict = {}
def rate_mortality():
  for key in mortality_scale:
    mortality_hurricane_dict.update({key:[]})
  for key,value in hurricane_dict.items():
    deaths = value["Deaths"]
    rated = False
    for rating, rating_values in mortality_scale.items():
      if rated == False:
        if rating == 4:
          mortality_hurricane_dict[4].append({key:value})
          rated = True
        elif deaths < mortality_scale[rating + 1] and deaths > rating_values:
          mortality_hurricane_dict[rating].append({key:value})
          rated = True


# categorize hurricanes in new dictionary with mortality severity as key

rate_mortality()
# for element in mortality_hurricane_dict:
#  print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
#  print(element, mortality_hurricane_dict[element])


# 8 Calculating Hurricane Maximum Damage

def hurricane_max_damage():
  max_damage = -1
  possible_hurricanes = []
  for name, value in hurricane_dict.items():
    number = value["Damages"]
    if type(number) == float:
      if max_damage < number:
        max_damage = number
        possible_hurricanes.append(name)
  print("The most destructive hurricane was {hurricane}, with a cost of {X} $".format(hurricane=possible_hurricanes[-1],X=max_damage))


# find highest damage inducing hurricane and its total cost
# hurricane_max_damage()


# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}

                   
damages_hurricane_dict = {}
def rate_damages():
  for key in damage_scale:
    damages_hurricane_dict.update({key:[]})
  for key,value in hurricane_dict.items():
    if not value["Damages"] == "Damages not recorded":
      damages = value["Damages"]
      rated = False
      for rating, rating_values in damage_scale.items():
        if rated == False:
          if rating == 4:
            damages_hurricane_dict[4].append({key:value})
            rated = True
          elif damages < damage_scale[rating + 1] and damages > rating_values:
            damages_hurricane_dict[rating].append({key:value})
            rated = True

rate_damages() 
#for element in mortality_hurricane_dict:
 # print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
 # print(element, damages_hurricane_dict[element])
 #print(damages_hurricane_dict)
# categorize hurricanes in new dictionary with damage severity as key
