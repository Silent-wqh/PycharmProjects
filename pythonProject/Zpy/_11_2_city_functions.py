# def city_country(city, country, population):
#     return(f'{city.title()}, {country.title()} - population {population}')


def city_country(city, country, population=''):
    if population == '':
        return (f'{city.title()}, {country.title()}')
    else:
        return(f'{city.title()}, {country.title()} - population {population}')

