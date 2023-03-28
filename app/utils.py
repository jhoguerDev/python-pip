def get_population(country_dict):
  population_dict = {
    '1970': int(country_dict['1970 Population']),
    '1980': int(country_dict['1980 Population']),
    '1990': int(country_dict['1990 Population']),
    '2000': int(country_dict['2000 Population']),
    '2010': int(country_dict['2010 Population']),
    '2015': int(country_dict['2015 Population']),
    '2020': int(country_dict['2020 Population']),
    '2022': int(country_dict['2022 Population']),
  }
  labels = population_dict.keys()
  values = population_dict.values()
  return labels, values
def map_label_and_values_world(item):
  return item.keys()
  
def get_world_population_percentage_data(world_population_percentage_dict):
  print(type(world_population_percentage_dict))
  labels = [label.keys() for label in world_population_percentage_dict]
  #labels = list(map(map_label_and_values_world, world_population_percentage_dict))
  values = list(map(lambda item: item.values(), world_population_percentage_dict))
  #labels = world_population_percentage_dict[0].keys()
  #values = world_population_percentage_dict[0].values()
  return labels, values
  
def map_data(item):
  #labels = item['Country/Territory']
  #values = item['World Population Percentage']
  return {item['Country/Territory']: item['World Population Percentage']}
  #return labels, values

def get_world_population_percentage(data):
  result = list(map(map_data, data))
  return result
  

def population_by_country(data, country):
  result = list(filter(lambda item: item['Country/Territory'] == country, data))
  return result