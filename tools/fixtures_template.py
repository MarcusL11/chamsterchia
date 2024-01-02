import requests
import time

i = 1
nft_metadata = []
next_address = "start"

while next_address is not None: 
    print(f"page {i}")

    if i == 1:
        url = "https://api.mintgarden.io/collections/col12zrl5dh4qwahqwf30d7n33fsun6jhp4rvlqaujqvewjp02uvx63st8v8fu/nfts?page=>"
    else:
        url = f"https://api.mintgarden.io/collections/col12zrl5dh4qwahqwf30d7n33fsun6jhp4rvlqaujqvewjp02uvx63st8v8fu/nfts?page={next_address}"

    page_request = requests.get(url)
    database = page_request.json()

    # Check if items list is empty; if so, break the loop
    items = database.get("items", [])
    if not items:
        break

    next_address = database["next"]

    for item in items:
        encoded_id = item["encoded_id"]
        if encoded_id:
            print(encoded_id)
            nft_metadata.append(encoded_id)
        else:
            print("No data")
    i += 1
    time.sleep(page_request.elapsed.total_seconds())

print(f"A total of {len(nft_metadata)} nfts has been collected")


        
        # name = items["name"]
        # collection_id = items["collection_id"]
        # collection_name = items["collection_name"]
        # xch_price = items["xch_price"] # offer price
        # owner_address_encoded_id = items["owner_address_encoded_id"]
        # owner_encoded_id = items["owner_encoded_id"]
        # owner_id = items["owner_id"] # Onwer's DID
        # owner_avatar_uri = items["owner_avatar_uri"] # Owner's avatar
        # owner_name = items["owner_name"] # Owner's name

        # Database = {
        #     "model": "chamsterapp.Chamster",
        #     "pk": "f5250a20fca3bba2adf8a3aea0c155d44065ec741842d70db2057a25f0a58658",
        #     "fields": {
        #         "encoded_id": "nft175js5g8u5wa69t0c5wh2ps2463qxtmr5rppdwrdjq4aztu99sevqpzp3qc",
        #         "owner_address": "xch1mkgxz8nzmfctq39uuyupghpqyl44nlszcse7ull76xm8mu7y7jzqy5ruy7",
        #         "data_uri": "https://nftstorage.link/ipfs/bafybeiglb6r7yuiacxi3s2cyik67d2vh24b6ubg4um3ujmqsmd6ofrglum/182.png",
        #         "thumbnail_uri": "https://assets.mainnet.mintgarden.io/thumbnails/214337bfa45d97ae9866446914564ca1c987820466f5b146c8a7751bd24539b7_512.webp",
        #         "preview_uri": "https://assets.mainnet.mintgarden.io/thumbnails/214337bfa45d97ae9866446914564ca1c987820466f5b146c8a7751bd24539b7.webp",
        #         "name": "Chamster Golfer #182",
        #         "background": "Farm Field",
        #         "fur": "Brown Fur",
        #         "shirt": "Pink Shirt",
        #         "pants": "White Pants",
        #         "head": "Nothing",
        #         "eyes": "Normal Eyes",
        #         "club": "Iron",
        #         "power": 4,
        #         "putting": 3,
        #         "accuracy": 5,
        #         "recovery": 1,
        #         "luck": 7,
        #         "specialty": "None",
        #         "tsi": 20
        #     }
        # }