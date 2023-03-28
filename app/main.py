import utils
import read_csv
import charts
  
def run():
  data = read_csv.read_csv('data.csv')
  data = list(filter(lambda item: item['Continent'] == 'South America', data))

  counttries = list(map(lambda x: x['Country/Territory'], data))
  percentage = list(map(lambda x: x['World Population Percentage'], data))
  charts.generate_pie_chart(counttries, percentage)

  country = input('type Country => ')
  
  result = utils.population_by_country(data, country)


  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(result[0])
    charts.generate_bar_chart(country['Country/Territory'], labels, values)


if __name__ == '__main__':
  run()