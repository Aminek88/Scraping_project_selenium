# processor.py

import pandas as pd

def stock_data(liste):
    rows = []

    for items in liste:
        info = items['info'].split('\n')
        des = items['Equipement'].split('\n')
        row = {
            'URL' : items['url'],
            'Title': items['Title'],
            'Localisation': items['Localisation'],
            'Price': items['Price'],
            'Chambre': items['Bedroom'],
            'Salle de bain': items['Bathroom'],
            'Type': None,
            'Secteur': None,
            'Salons': None,
            'Surface habitable': None,
            'Âge du bien': None,
            'Étage': None,
            'Frais de syndic': None,
            'Ascenseur': 'non',
            'Balcon': 'non',
            'Chauffage': 'non',
            'Climatisation': 'non',
            'Concierge': 'non',
            'Cuisine equipee': 'non',
            'Duplex': 'non',
            'Meuble': 'non',
            'Parking': 'non',
            'Securite': 'non',
            'Terrasse': 'non',
        }

        info_dict = {}
        for i in range(0, len(info), 2):
            if i + 1 < len(info):
                info_dict[info[i]] = info[i + 1]

        row['Type'] = info_dict.get('Type')
        row['Secteur'] = info_dict.get('Secteur')
        row['Salons'] = info_dict.get('Salons')
        row['Surface habitable'] = info_dict.get('Surface habitable')
        row['Âge du bien'] = info_dict.get('Âge du bien')
        row['Étage'] = info_dict.get('Étage')
        row['Frais de syndic'] = info_dict.get('Frais de syndic / mois')

        for equip in ['Ascenseur', 'Balcon', 'Chauffage', 'Climatisation', 'Concierge', 'Cuisine equipee', 'Duplex', 'Meuble', 'Parking', 'Securite', 'Terrasse']:
            row[equip] = 'oui' if equip in des else 'non'

        rows.append(row)

    df = pd.DataFrame(rows)
    df.to_csv('classified_data2.csv', index=False)
    return df
