import time
import os
from discord_webhook import DiscordWebhook, DiscordEmbed
from pyVinted import Vinted
import utils

WEBHOOK_URL = "YOUR_WEBHOOK"

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

                🤑 Vinted Bot v1
                    By Norze

""".replace("$", utils.PURPLE + "$" + utils.WHITE).replace("_", utils.RED + "_" + utils.WHITE).replace("|", utils.RED + "|" + utils.WHITE).replace("/", utils.RED + "/" + utils.WHITE).replace("\\", utils.RED + "\\" + utils.WHITE)
print(banner)

last_item_id = ""
sent_items = []

allowed_brands = ["nike", "adidas", "ralph lauren", "puma"] # list of brands you want
allowed_country_code = "fr" # your country
allowed_price = 200 # your max price

while True:
    try:
        time.sleep(3)    
        vinted = Vinted()
        items = vinted.items.search(f"https://www.vinted.fr/vetement?order=newest_first&price_to={allowed_price}&currency=EUR&country_code={allowed_country_code}", 10, 1)
       
        for item in items:
            if item.brand_title.lower() in allowed_brands:
                if item.id not in sent_items: 
                    sent_items.append(item.id)  

                    titler = item.title if item.title else "Not found"
                    screen = item.photo if item.photo else "Not found"
                    brand = item.brand_title if item.brand_title else "Not found"
                    price = f"{item.price}€" if item.price else "Not found"
                    url = item.url if item.url else "Not found"
                    create = item.created_at_ts.strftime("%Y-%m-%d %H:%M:%S") if item.created_at_ts else "Not found"

                    webhook = DiscordWebhook(url=WEBHOOK_URL)
                    embed = DiscordEmbed(title="", description=f"**[{titler}]({url})**", color=3447003)
                    embed.add_embed_field(name="", value="", inline=False)
                    embed.set_thumbnail(url="https://c0.lestechnophiles.com/www.numerama.com/wp-content/uploads/2016/02/simpsons.gif?resize=500,432&key=f4555826")
                    embed.set_image(url=screen)
                    embed.add_embed_field(name="⌛ Publication", value=create, inline=True)
                    embed.add_embed_field(name="🔖 Marque", value=brand, inline=True)
                    embed.add_embed_field(name="💰 Prix", value=price, inline=True)

                    embed.set_footer(text="Bot Vinted by Norze")
                    webhook.add_embed(embed)
                    response = webhook.execute()

                    if response.status_code == 200:
                        print('[+] Embed sent successfully.')
                    else:
                        print('[-] Failed to send embed. Status code:', response.status_code)

                else:
                    print("[INFO] Already shown")

    except Exception as e:
        print("[INFO] Failed:", str(e))