import requests
import csv

def main(file):
    with open(file, 'r') as csvfile:
        readCSV = csv.reader(csvfile)

        Errors = []

        for raw in readCSV:
            url = raw[0]
            #print(url)
            try:
                url_serach = "https://grocery.walmart.com/v3/api/products?strategy=search&storeId=2119&query=avocado&count=60&page=1&offset=0"
                response_search = requests.get(url_serach)
                response_search_str = response_search.json()
                products = []
                product_size = len(response_search_str['products'])
                #print(product_size)
                for i in range(0, product_size):
                    #print(i)
                    if(response_search_str['products'][i]['basic']['isOutOfStock'] == False):
                        products.append(response_search_str['products'][i]['USItemId'])
                for product in products:
                    #print(product)
                    try:
                        # IRO Item ID Grocery Call
                        url_iro = 'http://iro-site-facing.prod-site-facing.iro.services.prod.walmart.com/item-read-service/productOffers?rgs=PRODUCT_CONTENT,OFFER_PRODUCT,OFFER_PRICE,OFFER_INVENTORY,ESTIMATED_SHIP_PRICE,VARIANT_SUMMARY'
                        req_payload_iro = "{\"productContexts\": [{\"productId\": {\"USItemId\": \"" + product + "\"}}],\"storeFrontIds\": [{\"USStoreId\": 2110}]}"
                        headers_iro = {'WM_SVC.VERSION': '2.0.0',
                                       'WM_SVC.ENV': 'stg0',
                                       'WM_QOS.CORRELATION_ID': '18006880586',
                                       'WM_SVC.NAME': 'item-read-service',
                                       'WM_CONSUMER.ID': 'b97936bb-84b8-474d-8888-29cda10d6655',
                                       'Content-Type': 'application/json',
                                       'WM_VERTICAL_ID': '2'}
                        response_iro = requests.request("POST", url_iro, data=req_payload_iro, headers=headers_iro)
                        response_iro_str = response_iro.json()

                        if (response_iro_str['status'] == 'OK'):
                            #print(response_iro_str['payload'][0]['offerWrappers'][0]['storeFronts'][0]['canAddToCart'])
                            if (response_iro_str['payload'][0]['offerWrappers'][0]['storeFronts'][0]['canAddToCart'] == True):
                                #print(product+" Mismatching - Search Page (OOS-FALSE) & IRO (OOS-TRUE)")
                                Errors.append(product+" Mismatching - Search Page (OOS-FALSE) & IRO (OOS-TRUE)")
                        else:
                            Errors.append(product + " IRO is Status is " + response_iro_str['status'] + " Error Code: " +
                                          response_iro_str['payload'][0]['entityErrors'][0]['code'])
                    except Exception as e:
                        Errors.append(product + " " + e)
            except Exception as e:
                Errors.append(product + " " + e)

    with open('test1Res1Search.csv', 'w') as csv_wr:
        thewriter = csv.writer(csv_wr)
        for e in Errors:
            thewriter.writerow([e])

if __name__ == '__main__':
    main('search_url.csv')