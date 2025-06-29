from carrier import *
import random

order = {
    'order_id': str(random.randint(1000, 10000)),
    'sender_company': 'MMCompany',
    'sender_fullname': 'Jan Kowalski',
    'sender_address': 'Kopernika 1234',
    'sender_city': 'Poznan',
    'sender_postalcode': '61208',
    'sender_email': '',
    'sender_phone': '666666666',
    'delivery_company': 'Spring GDS',
    'delivery_fullname': 'Maud Driant',
    'delivery_address': 'Strada Foisorului, Nr. 16, Bl. F11C, Sc. 1, Ap. 10',
    'delivery_city': 'Bucuresti, Sector 3',
    'delivery_postalcode': '031179',
    'delivery_country': 'RO',
    'delivery_email': 'john@doe.com',
    'delivery_phone': '555555555',
}

params = {
    'api_key': 'ed1e2e1567b781d6',
    'label_format': 'PDF',
    'service': 'EXPR',
}

print(order)

carrier = Carrier();