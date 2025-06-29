import json

class Carrier:
  def __init__(self):
    print('Hello Morining')

  def newPackage(order, params):
    data = {}
    shipment = {}
    consignorAddress = {}
    consigneeAddress = {}
    product = {}

    data['Apikey'] = params['api_key']
    data['Command'] = 'OrderShipment'
    data['Shipment'] = shipment
    data['Products'] = [product]
    shipment['LabelFormat'] = params['label_format']
    shipment['ShipperReference'] = 'Reference_' + order['order_id']
    shipment['ConsignorAddress'] = consignorAddress
    shipment['ConsigneeAddress'] = consigneeAddress
    consignorAddress['Name'] = order['sender_fullname']
    consignorAddress['Company'] = order['sender_company']
    consignorAddress['AddressLine1'] = order['sender_address']
    consignorAddress['City'] = order['sender_city']
    consignorAddress['Zip'] = order['sender_postalcode']
    consignorAddress['Phone'] = order['sender_phone']
    consigneeAddress['Name'] = order['delivery_fullname']
    consigneeAddress['Company'] = order['delivery_company']
    consigneeAddress['AddressLine1'] = order['delivery_address']
    consigneeAddress['City'] = order['delivery_city']
    consigneeAddress['Zip'] = order['delivery_postalcode']
    consigneeAddress['Phone'] = order['delivery_phone']
    product['Description'] = 'Black Top'
    product['Quantity'] = '1'
    product['Value'] = '20'