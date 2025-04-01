import matplotlib.pyplot as plt
import numpy as np

# For facility reasons, the datas from `js/index.js` are copied here to generate the charts

happiness_by_region = {
  'Southern Asia': 4.7938,
  'Central and Eastern Europe': 5.566733333333333,
  'Middle East and Northern Africa': 5.237,
  'Latin America and Caribbean': 5.942549999999999,
  'Australia and New Zealand': 7.2675,
  'Western Europe': 6.8984,
  'Sub-Saharan Africa': 4.34619512195122,
  'Southeastern Asia': 5.202166666666667,
  'North America': 7.085,
  'Eastern Asia': 5.688833333333332
}

top10_countries_by_gdp = [
    {
        'Country': 'Qatar',
        'Region': 'Middle East and Northern Africa',
        'Rank 2019': '29',
        'Score 2019': '6.374',
        'GDP 2019': '1.684',
        'Family 2019': '1.313',
        'Life Expectancy 2019': '0.871',
        'Freedom 2019': '0.555',
        'Trust 2019': '0.167',
        'Generosity 2019': '0.22'
    },
    {
        'Country': 'Luxembourg',
        'Region': 'Western Europe',
        'Rank 2019': '14',
        'Score 2019': '7.09',
        'GDP 2019': '1.609',
        'Family 2019': '1.479',
        'Life Expectancy 2019': '1.012',
        'Freedom 2019': '0.526',
        'Trust 2019': '0.316',
        'Generosity 2019': '0.194'
    },
    {
        'Country': 'Singapore',
        'Region': 'Southern Asia',
        'Rank 2019': '34',
        'Score 2019': '6.262',
        'GDP 2019': '1.572',
        'Family 2019': '1.463',
        'Life Expectancy 2019': '1.141',
        'Freedom 2019': '0.556',
        'Trust 2019': '0.453',
        'Generosity 2019': '0.271'
    },
    {
        'Country': 'United Arab Emirates',
        'Region': 'Middle East and Northern Africa',
        'Rank 2019': '21',
        'Score 2019': '6.825',
        'GDP 2019': '1.503',
        'Family 2019': '1.31',
        'Life Expectancy 2019': '0.825',
        'Freedom 2019': '0.598',
        'Trust 2019': '0.182',
        'Generosity 2019': '0.262'
    },
    {
        'Country': 'Kuwait',
        'Region': 'Middle East and Northern Africa',
        'Rank 2019': '51',
        'Score 2019': '6.021',
        'GDP 2019': '1.5',
        'Family 2019': '1.319',
        'Life Expectancy 2019': '0.808',
        'Freedom 2019': '0.493',
        'Trust 2019': '0.097',
        'Generosity 2019': '0.142'
    },
    {
        'Country': 'Ireland',
        'Region': 'Western Europe',
        'Rank 2019': '16',
        'Score 2019': '7.021',
        'GDP 2019': '1.499',
        'Family 2019': '1.553',
        'Life Expectancy 2019': '0.999',
        'Freedom 2019': '0.516',
        'Trust 2019': '0.31',
        'Generosity 2019': '0.298'
    },
    {
        'Country': 'Norway',
        'Region': 'Western Europe',
        'Rank 2019': '3',
        'Score 2019': '7.554',
        'GDP 2019': '1.488',
        'Family 2019': '1.582',
        'Life Expectancy 2019': '1.028',
        'Freedom 2019': '0.603',
        'Trust 2019': '0.341',
        'Generosity 2019': '0.271'
    },
    {
        'Country': 'Switzerland',
        'Region': 'Western Europe',
        'Rank 2019': '6',
        'Score 2019': '7.48',
        'GDP 2019': '1.452',
        'Family 2019': '1.526',
        'Life Expectancy 2019': '1.052',
        'Freedom 2019': '0.572',
        'Trust 2019': '0.343',
        'Generosity 2019': '0.263'
    },
    {
        'Country': 'Hong Kong',
        'Region': 'Eastern Asia',
        'Rank 2019': '76',
        'Score 2019': '5.43',
        'GDP 2019': '1.438',
        'Family 2019': '1.277',
        'Life Expectancy 2019': '1.122',
        'Freedom 2019': '0.44',
        'Trust 2019': '0.287',
        'Generosity 2019': '0.258'
    },
    {
        'Country': 'United States',
        'Region': 'North America',
        'Rank 2019': '19',
        'Score 2019': '6.892',
        'GDP 2019': '1.433',
        'Family 2019': '1.457',
        'Life Expectancy 2019': '0.874',
        'Freedom 2019': '0.454',
        'Trust 2019': '0.128',
        'Generosity 2019': '0.28'
    }
]

bottom10_countries_by_gdp = [
    {
        'Country': 'Somalia',
        'Region': 'Sub-Saharan Africa',
        'Rank 2019': '112',
        'Score 2019': '4.668',
        'GDP 2019': '0',
        'Family 2019': '0.698',
        'Life Expectancy 2019': '0.268',
        'Freedom 2019': '0.559',
        'Trust 2019': '0.27',
        'Generosity 2019': '0.243'
    },
    {
        'Country': 'Central African Republic',
        'Region': 'Sub-Saharan Africa',
        'Rank 2019': '155',
        'Score 2019': '3.083',
        'GDP 2019': '0.026',
        'Family 2019': '0',
        'Life Expectancy 2019': '0.105',
        'Freedom 2019': '0.225',
        'Trust 2019': '0.035',
        'Generosity 2019': '0.235'
    },
    {
        'Country': 'Burundi',
        'Region': 'Sub-Saharan Africa',
        'Rank 2019': '145',
        'Score 2019': '3.775',
        'GDP 2019': '0.046',
        'Family 2019': '0.447',
        'Life Expectancy 2019': '0.38',
        'Freedom 2019': '0.22',
        'Trust 2019': '0.18',
        'Generosity 2019': '0.176'
    },
    {
        'Country': 'Liberia',
        'Region': 'Sub-Saharan Africa',
        'Rank 2019': '141',
        'Score 2019': '3.975',
        'GDP 2019': '0.073',
        'Family 2019': '0.922',
        'Life Expectancy 2019': '0.443',
        'Freedom 2019': '0.37',
        'Trust 2019': '0.033',
        'Generosity 2019': '0.233'
    },
    {
        'Country': 'Congo (Kinshasa)',
        'Region': 'Sub-Saharan Africa',
        'Rank 2019': '127',
        'Score 2019': '4.418',
        'GDP 2019': '0.094',
        'Family 2019': '1.125',
        'Life Expectancy 2019': '0.357',
        'Freedom 2019': '0.269',
        'Trust 2019': '0.053',
        'Generosity 2019': '0.212'
    },
    {
        'Country': 'Niger',
        'Region': 'Sub-Saharan Africa',
        'Rank 2019': '114',
        'Score 2019': '4.628',
        'GDP 2019': '0.138',
        'Family 2019': '0.774',
        'Life Expectancy 2019': '0.366',
        'Freedom 2019': '0.318',
        'Trust 2019': '0.102',
        'Generosity 2019': '0.188'
    },
    {
        'Country': 'Malawi',
        'Region': 'Sub-Saharan Africa',
        'Rank 2019': '150',
        'Score 2019': '3.41',
        'GDP 2019': '0.191',
        'Family 2019': '0.56',
        'Life Expectancy 2019': '0.495',
        'Freedom 2019': '0.443',
        'Trust 2019': '0.089',
        'Generosity 2019': '0.218'
    },
    {
        'Country': 'Mozambique',
        'Region': 'Sub-Saharan Africa',
        'Rank 2019': '123',
        'Score 2019': '4.466',
        'GDP 2019': '0.204',
        'Family 2019': '0.986',
        'Life Expectancy 2019': '0.39',
        'Freedom 2019': '0.494',
        'Trust 2019': '0.138',
        'Generosity 2019': '0.197'
    },
    {
        'Country': 'Sierra Leone',
        'Region': 'Sub-Saharan Africa',
        'Rank 2019': '129',
        'Score 2019': '4.374',
        'GDP 2019': '0.268',
        'Family 2019': '0.841',
        'Life Expectancy 2019': '0.242',
        'Freedom 2019': '0.309',
        'Trust 2019': '0.045',
        'Generosity 2019': '0.252'
    },
    {
        'Country': 'Madagascar',
        'Region': 'Sub-Saharan Africa',
        'Rank 2019': '143',
        'Score 2019': '3.933',
        'GDP 2019': '0.274',
        'Family 2019': '0.916',
        'Life Expectancy 2019': '0.555',
        'Freedom 2019': '0.148',
        'Trust 2019': '0.041',
        'Generosity 2019': '0.169'
    }
]

regions = list(happiness_by_region.keys()) # Getting only the regions names, using the keys of the dictionary
happiness_scores = list(happiness_by_region.values()) # Getting the happiness scores, using the values of the dictionary

fig, ax = plt.subplots()
plt.figure(1)
ax.bar(regions, happiness_scores)

ax.set_ylabel('Happiness Score')
ax.set_title('Happiness by region')
fig.canvas.manager.set_window_title('Happiness by region')

fig, ax = plt.subplots()
plt.figure(2)
countries = [country['Country'] for country in top10_countries_by_gdp] # Getting the countries names
gdp = [np.float64(country['GDP 2019']) for country in top10_countries_by_gdp] # Getting the GDP values as float
ax.bar(countries, gdp)

ax.set_ylabel('GDP')
ax.set_title('Top 10 GDP by country')
fig.canvas.manager.set_window_title('Top 10 GDP by country')

fig, ax = plt.subplots()
plt.figure(3)
countries = [country['Country'] for country in bottom10_countries_by_gdp]
gdp = [np.float64(country['GDP 2019']) for country in bottom10_countries_by_gdp]
ax.bar(countries, gdp)

ax.set_ylabel('GDP')
ax.set_title('Bottom 10 GDP by country')
fig.canvas.manager.set_window_title('Bottom 10 GDP by country')
plt.show()