from helper import *
from database import Database

db = Database()


def create_database():
    database_data_mart = open("./datamart/data-mart.sql", 'r')
    database_sql = database_data_mart.read()
    database_data_mart.close()
    db.execute(database_sql)


def populate_date(all_dates_in_a_year):
    data = []

    for date in all_dates_in_a_year:
        day = date.day
        month = date.month
        year = date.year
        data.append((date, day, month, year))

    return data


def populate_location(locations):
    data = []

    for location in locations:
        data.append((location['city'], location['uf'], location['location']))

    return data


def populate_producer(producers):
    data = []

    for producer in producers:
        data.append((producer['name'], producer['age']))

    return data


def populate_item(items):
    data = []

    for item in items:
        data.append((item['name'],))

    return data


def populate_factproduction(fact_productions):
    data = []

    for fact_production in fact_productions:
        data.append((fact_production['date_id'], fact_production['item_id'], fact_production['producer_id'],
                     fact_production['location_id'], fact_production['qtd_product'], fact_production['qtd_excess']))

    return data


def main():
    # create_database()

    # Get all dates in a year
    all_dates_in_a_year = get_all_dates_in_a_year(2021)

    sql = "INSERT INTO `DATE` (`DATE`, `DAY`, `MONTH`, `YEAR`) VALUES (%s, %s, %s, %s);"
    data = populate_date(all_dates_in_a_year)

    db.insert(sql, data)

    # Get all locations
    locations = get_locations()

    sql = 'INSERT `LOCATION` (`CITY`, `UF`, `LOCATION`) VALUES (%s, %s, %s);'
    data = populate_location(locations)

    db.insert(sql, data)

    # Get all producers
    producers = get_producers()

    sql = "INSERT INTO `PRODUCER` (`NAME`, `AGE`) VALUES (%s, %s);"
    data = populate_producer(producers)

    db.insert(sql, data)

    # Get all items
    items = get_items()

    sql = "INSERT INTO `ITEM` (`NAME`) VALUES (%s);"
    data = populate_item(items)

    db.insert(sql, data)

    # Get all factproduction
    fact_productions = get_fact_productions()

    sql = "INSERT `FACTPRODUCTION` (`DATE_ID`, `ITEM_ID`, `PRODUCER_ID`, `LOCATION_ID`, `QTD_PRODUCT`, `QTD_EXCESS`) VALUES (%s, %s, %s, %s, %s, %s);"
    data = populate_factproduction(fact_productions)

    db.insert(sql, data)

    db.close()


if __name__ == '__main__':
    main()
