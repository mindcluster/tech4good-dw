from helper import *
from database import Database

db = Database()


def create_database():
    database_data_mart = open("./datamart/data-mart.sql", 'r')
    database_sql = database_data_mart.read()
    database_data_mart.close()
    db.execute(database_sql)


def populate_date(date):
    day = date.day
    month = date.month
    year = date.year

    sql = f"INSERT INTO `DATE` (`DATE`, `DAY`, `MONTH`, `YEAR`) VALUES ('{date}', {day}, {month}, {year});"
    db.insert(sql)


def populate_location(location):
    sql = f'INSERT `LOCATION` (`CITY`, `UF`, `LOCATION`) VALUES ("{location["city"]}", "{location["uf"]}", "{location["location"]}");'
    db.insert(sql)


def populate_producer(producer):
    sql = f"INSERT INTO `PRODUCER` (`NAME`, `AGE`) VALUES ('{producer['name']}', '{producer['age']}');"
    db.insert(sql)


def populate_item(item):
    sql = f"INSERT INTO `ITEM` (`NAME`) VALUES ('{item['name']}');"
    db.insert(sql)


def populate_factproduction(factproduction):
    sql = f"INSERT `FACTPRODUCTION` (`DATE_ID`, `ITEM_ID`, `PRODUCER_ID`, `LOCATION_ID`, `QTD_PRODUCT`, `EXCESS`) VALUES ({factproduction['date_id']}, {factproduction['item_id']}, {factproduction['producer_id']}, {factproduction['location_id']}, {factproduction['qtd_product']}, {factproduction['excess']});"
    db.insert(sql)


def main():
    # create_database()

    all_dates_in_a_year = get_all_dates_in_a_year(2021)
    for date in all_dates_in_a_year:
        populate_date(date)

    locations = get_locations()
    for location in locations:
        populate_location(location)

    producers = get_producers()
    for producer in producers:
        populate_producer(producer)

    items = get_items()
    for item in items:
        populate_item(item)

    fact_productions = get_fact_productions()
    for fact_production in fact_productions:
        populate_factproduction(fact_production)

    db.close()


if __name__ == '__main__':
    main()
