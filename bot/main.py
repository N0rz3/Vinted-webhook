from pyVinted import Vinted # API-wrapper by aime-risson
import time
import utils
import os
import requests
import json

WEBHOOK = "YOUR_WEBHOOK"

os.system("title Vinted Scraping $_$ By N0RZE")

banner = """
            /$$             /$$                     /$$
           |__/            | $$                    | $$
 /$$    /$$ /$$ /$$$$$$$  /$$$$$$    /$$$$$$   /$$$$$$$
|  $$  /$$/| $$| $$__  $$|_  $$_/   /$$__  $$ /$$__  $$
 \  $$/$$/ | $$| $$  \ $$  | $$    | $$$$$$$$| $$  | $$
  \  $$$/  | $$| $$  | $$  | $$ /$$| $$_____/| $$  | $$
   \  $/   | $$| $$  | $$  |  $$$$/|  $$$$$$$|  $$$$$$$
    \_/    |__/|__/  |__/   \___/   \_______/ \_______/

             🤑 Vinted Bot v0.0.1 
                  Credits: norze

""".replace("$", utils.Light_Purple + "$" + utils.Reset).replace("_", utils.Light_Red + "_" + utils.Reset).replace("|", utils.Light_Red + "|" + utils.Reset).replace("/", utils.Light_Red + "/" + utils.Reset).replace("\\", utils.Light_Red + "\\" + utils.Reset)
print(banner)

input("Press enter to start scraping vinted ads ...\n")

last_item_id = ""
sent_items = []

allowed_brands = ["nike", "adidas", "ralph lauren", "puma"] # list of brands you want
allowed_country_code = "fr" # your country
allowed_price = "20" # your max price

while True:
    try:
            
        time.sleep(3)    
        vinted = Vinted()
        items = vinted.items.search(f"https://www.vinted.fr/vetement?order=newest_first&price_to={allowed_price}&currency=EUR&country_code={allowed_country_code}", 10, 1)
       

        for item in items:
            if item.brand_title.lower() in allowed_brands:
                if item.id not in sent_items: 
                    sent_items.append(item.id)  

                    title = item.title
                    if title != "":
                        title = title
                    else:
                        title = "Not found"

                    screen = item.photo
                    if screen != "":
                        screen = screen
                    else:
                        screen = "Not found"
                    
                    brand = item.brand_title
                    if brand != "":
                        brand = brand
                    else:
                        brand = "Not found"

                    price = item.price
                    if price != "":
                        price = price
                    else:
                        price = "Not found"

                    url = item.url
                    if url != "":
                        url = url
                    else:
                        url = "Not found"

                    currency = item.currency
                    if currency != "":
                        currency = currency
                    else:
                        currency = "Not found"
                    
                    create = item.created_at_ts
                    if create != "":
                        create = create
                    else:
                        create = "Not found"


                    if currency == "EUR":
                        price = f"{price}€"
                    else:
                        price = price

                    data = {
                        "embeds": [
                            {
                                "title": "Vinted Bot",
                                "description": f"Bot vinted v1",
                                "color": 3447003,
                                "thumbnail": {
                                    "url": "https://www.presse-citron.net/app/uploads/2020/06/vinted-logo.jpg"
                                },
                                "image": {
                                    "url": screen
                                },
                                "fields": [
                                    {
                                        "name": f"{title} : {url}",
                                        "value": f"⌛ **Published **: `{create}`\n🔖 **Brand **: `{brand}`\n💰 **Price **: `{price}`\n"
                                    }
                                ],
                                "footer": {
                                    "icon_url": "https://i.pinimg.com/originals/3c/c6/e7/3cc6e7226c2ab03619a012c9bcf12c17.gif",
                                    "text": "Dev By N0RZE"
                                }
                            }
                        ]
                    }

                    headers = {
                        "Content-Type": "application/json"
                    }

                    response = requests.post(WEBHOOK, data=json.dumps(data), headers=headers)

                    if response.status_code == 204:
                        print('[+] Embed sent successfully.')
                    else:
                        print('[-] Failed to send embed. Status code:', response.status_code)



                else:
                    print(f"[{utils.Blue}INFO{utils.Blue}{utils.Reset}] Already shown")


    except:
        print(f"[{utils.Blue}INFO{utils.Blue}{utils.Reset}] Failed")
