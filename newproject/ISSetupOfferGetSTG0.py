import requests
from pprint import pprint

def main():
    offer_id = 'BAAEAB182019451DB796FE9089336596'
    respose = requests.get('http://itemstoresetup.stg0.itemstore.catdev.prod.walmart.com/itemstore-item-setup-app/services/offer/'+offer_id)
    response_str = respose.json()

    #pprint(response_str) # - pretty print

    print(response_str['status'])
    assert(response_str['status'] == 'OK')
    print(response_str['payload']['offerPurchaseType']['purchaseOption'])
    assert(response_str['payload']['offerPurchaseType']['purchaseOption'] == 'BUY')
    print(response_str['payload']['offerPurchaseType']['conditionType'])
    assert(response_str['payload']['offerPurchaseType']['conditionType'] == 'NEW')

if __name__ == '__main__':
    main()