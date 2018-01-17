import requests
import csv

def main():
    Errors = []
    with open('actual1.csv', 'r') as csvfile:
        readCSV = csv.reader(csvfile)
        product_ids = []
        for raw in readCSV:
            pr_id = raw[1]
            st_id = raw[0]
            try:
                #Item page
                #product_id = '13893738'
                url_ip = 'https://grocery.walmart.com/v3/api/products/'+pr_id+'?itemFields=all&storeId='+st_id
                response_ip = requests.get(url_ip)
                response_ip_str = response_ip.json()
                #print(response_ip_str)
                print(response_ip_str['basic']['isOutOfStock'])
                try:
                    if(response_ip_str['basic']['isOutOfStock'] is None):
                        Errors.append(pr_id +" "+st_id+ " " + "Item page Fail to get respective product isOutOfStock is not available!") #not able to handle it
                    else:
                        if(response_ip_str['basic']['isOutOfStock'] == True):
                            try:
                                #IRO Item ID Grocery Call
                                url_iro = 'http://iro-site-facing.prod-site-facing.iro.services.prod.walmart.com/item-read-service/productOffers?rgs=PRODUCT_CONTENT,OFFER_PRODUCT,OFFER_PRICE,OFFER_INVENTORY,ESTIMATED_SHIP_PRICE,VARIANT_SUMMARY'
                                req_payload_iro = "{\"productContexts\": [{\"productId\": {\"USItemId\": \""+pr_id+"\"}}],\"storeFrontIds\": [{\"USStoreId\": "+st_id+"}]}"
                                headers_iro = {'WM_SVC.VERSION': '2.0.0',
                                       'WM_SVC.ENV': 'stg0',
                                       'WM_QOS.CORRELATION_ID': '18006880586',
                                       'WM_SVC.NAME': 'item-read-service',
                                       'WM_CONSUMER.ID': 'b97936bb-84b8-474d-8888-29cda10d6655',
                                       'Content-Type': 'application/json',
                                       'WM_VERTICAL_ID': '2'}
                                response_iro = requests.request("POST", url_iro, data=req_payload_iro, headers=headers_iro)
                                response_iro_str = response_iro.json()

                                if(response_iro_str['status'] == 'OK'):
                                    print(response_iro_str['payload'][0]['offerWrappers'][0]['storeFronts'][0]['canAddToCart'])
                                    if(response_iro_str['payload'][0]['offerWrappers'][0]['storeFronts'][0]['canAddToCart'] == False):
                                        print("Item Page (IP-OOS-FALSE) & IRO Mismatching (IRO-OOS-TRUE)"+pr_id)
                                        Errors.append(pr_id+" "+st_id+" Item Page (IP-OOS-FALSE) & IRO Mismatching (IRO-OOS-TRUE)")
                                else:
                                    Errors.append(pr_id+" "+st_id + " IRO is Status is "+response_iro_str['status']+" Error Code: "+response_iro_str['payload'][0]['entityErrors'][0]['code'])
                            except Exception as e:
                                Errors.append(pr_id+" "+st_id+" "+str(e))
                except Exception as e2:
                    Errors.append(pr_id + " " + st_id + " " + str(e2))
            except Exception as e1:
                Errors.append(pr_id+" "+st_id+" "+str(e1))

    with open('actual1Res1.csv', 'w') as csv_wr:
        thewriter = csv.writer(csv_wr)
        for e in Errors:
            thewriter.writerow([e])

if __name__ == '__main__':
    main()