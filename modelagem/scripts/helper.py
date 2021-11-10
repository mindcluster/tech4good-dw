import datetime
import json
import random
import requests
from faker import Faker


def randomdateinayear(year):
    start = datetime.date(year, 1, 1)
    end = datetime.date(year, 12, 31)
    return start + datetime.timedelta(seconds=random.randint(0, int((end - start).total_seconds())))


def get_all_dates_in_a_year(year):
    start = datetime.date(year, 1, 1)
    end = datetime.date(year, 12, 31)
    return [start + datetime.timedelta(days=i) for i in range((end - start).days + 1)]


def get_locations():
    locations = []
    list_files = ["sao-paulo", "rio-grande-do-sul", "minas-gerais", "acre"]

    for file in list_files:
        result = requests.get(
            f"https://raw.githubusercontent.com/diegoholiveira/br-estados-cidades/master/data/{file}.json")
        estado = json.loads(result.content)

        cidades = estado["cidades"]

        for cidade in cidades:
            location = {
                "city": estado["nome"],
                "uf": estado["sigla"],
                "location": cidade["nome"]
            }
            locations.append(location)

    return locations


def get_producers():
    producers = []
    fake = Faker()

    for i in range(1, 15):
        producer = {
            "name": fake.name(),
            "age": random.randint(18, 65),
        }
        producers.append(producer)

    return producers


def get_items():
    items = [
        {"name": "peixes"},
        {"name": "ovos de galinhas"},
        {"name": "frangos de corte"},
        {"name": "carboidratos"},
        {"name": "hortaliças "},
        {"name": "chás"},
        {"name": "temperos"},
        {"name": "frutíferas "},
        {"name": "madeireiras"},
        {"name": "composto"},
        {"name": "ovos de codorna"},
        {"name": "porquinhos da Índia"},
        {"name": "Aquaponia"},
        {"name": "larvas de moscas"},
        {"name": "ruminantes"},
        {"name": "suínos"},
        {"name": "biodigestor"},
        {"name": "sistema de tratamento de água potável"},
        {"name": "carvoaria artesanal"}
    ]

    return items


def get_fact_productions():
    fact_productions = []

    for producer_id in range(1, 15):
        location_id = random.randint(1, 1940)

        for item_id in range(1, 15):

            for date_id in range(1, 365):
                qtd_product = random.randint(1, 10)

                fact_production = {
                    "date_id": date_id,
                    "item_id": item_id,
                    "producer_id": producer_id,
                    "location_id": location_id,
                    "qtd_product": qtd_product,
                    "qtd_excess": qtd_product - 7 if qtd_product > 7 else 0
                }
                fact_productions.append(fact_production)

    return fact_productions
