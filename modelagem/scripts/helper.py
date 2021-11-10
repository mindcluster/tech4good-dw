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

    for i in range(1, 150):
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

    for i in range(1, 1000):
        fact_production = {
            "date_id": random.randint(1, 365),
            "item_id": random.randint(1, 19),
            "producer_id": random.randint(1, 149),
            "location_id": random.randint(1, 1940),
            "qtd_product": random.randint(1, 100),
            "excess": random.randint(0, 1)
        }
        fact_productions.append(fact_production)

    return fact_productions
