from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from generar_base import Taller
import json
import requests

engine = create_engine('sqlite:///basetaller.db')

Session = sessionmaker(bind=engine)
session = Session()

archivo = requests.get(
    'https://pkgstore.datahub.io/core/country-codes/country-codes_json/data/616b1fb83cbfd4eb6d9e7d52924bb00a/country'
    '-codes_json.json')

datos_json = archivo.json()

for d in datos_json:
    print(d)
    print(len(d.keys()))
    t = Taller(nombrePais=d['CLDR display name'], capital=d['Capital'], contienente=d['Continent'], dial=d['Dial'],
               geonameId=d['Geoname ID'], itu=d['ITU'], languages=d['Languages'], isIndependent=d['is_independent'])
    session.add(t)

session.commit()
