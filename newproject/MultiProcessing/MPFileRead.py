import multiprocessing as mp
import csv
import requests

def main(pr_id):
    with open('test1Res1.csv', 'w') as csv_wr:
        thewriter = csv.writer(csv_wr)
        try:
            #Item page
            #product_id = '13893738'
            url_ip = 'https://grocery.walmart.com/v3/api/products/'+pr_id+'?itemFields=all&storeId=2110'
            response_ip = requests.get(url_ip)
            response_ip_str = response_ip.json()
            #print(response_ip_str)
            print(response_ip_str['basic']['isOutOfStock'])

            if(response_ip_str['basic']['isOutOfStock'] is None):
                thewriter.writerow([pr_id + " " + "Item page Fail to get respective product isOutOfStock is not available!"]) #not able to handle it
            else:
                if(response_ip_str['basic']['isOutOfStock'] == True):
                    try:
                        #IRO Item ID Grocery Call
                        url_iro = 'http://iro-site-facing.prod-site-facing.iro.services.prod.walmart.com/item-read-service/productOffers?rgs=PRODUCT_CONTENT,OFFER_PRODUCT,OFFER_PRICE,OFFER_INVENTORY,ESTIMATED_SHIP_PRICE,VARIANT_SUMMARY'
                        req_payload_iro = "{\"productContexts\": [{\"productId\": {\"USItemId\": \""+pr_id+"\"}}],\"storeFrontIds\": [{\"USStoreId\": 2110}]}"
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
                                thewriter.writerow([pr_id+" Item Page (IP-OOS-FALSE) & IRO Mismatching (IRO-OOS-TRUE)"])
                        else:
                            thewriter.writerow([pr_id + " IRO is Status is "+response_iro_str['status']+" Error Code: "+response_iro_str['payload'][0]['entityErrors'][0]['code']])
                    except Exception as e:
                        thewriter.writerow([pr_id + " " + e])
        except Exception as e1:
            thewriter.writerow([pr_id+" "+e1])

def process_wrapper(lineByte):
    with open("test2.txt") as f:
        f.seek(lineByte)
        line = f.readline()
        main(line)

#init objects
pool = mp.Pool(5)
jobs = []

#create jobs
with open("test2.txt") as f:
    nextLineByte = f.tell()
    for line in f:
        jobs.append( pool.apply_async(process_wrapper,(nextLineByte)) )
        #nextLineByte = f.tell()

#wait for all jobs to finish
for job in jobs:
    job.get()

#clean up
pool.close()