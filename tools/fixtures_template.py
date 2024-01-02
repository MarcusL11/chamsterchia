import requests
import time
import json

i = 1
id_list = []
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
            result = {
                "encoded_id": encoded_id,
            }
        else:
            print("Error in retrieving encoded_id")
        
        id_list.append(result)
        print(encoded_id)
        
    i += 1
    time.sleep(page_request.elapsed.total_seconds())

print(f"A total of {len(id_list)} nfts has been collected")

for item in id_list:
    count = 1
    url = f"https://api.mintgarden.io/nfts/{encoded_id}"
    page_request = requests.get(url)
    database = page_request.json()
    
    # Extracting necessary data
    metadata = database["data"]["metadata_json"]
    attributes = metadata["attributes"]
    img_uri = database["data"]["data_uris"][0]
    events = database["events"]
    
    # Chamster Model
    chamster_pk = database["id"]
    encoded_id = database["encoded_id"]
    name = metadata["name"]

    if "Legendary" in name:
        chaster_type = "Legendary"
    else:
        chamster_type = "Normal"
    
    # Dictionary to store attributes
    attributes_dict = {attribute["trait_type"]: attribute["value"] for attribute in attributes}
    
    # Assign values based on trait_type
    chamster_attributes = {
        "Background": "background", "Fur": "fur", "Shirt": "shirt", "Pants": "pants",
        "Head": "head", "Eyes": "eyes", "Club": "club", "Power": "power", "Putting": "putting",
        "Accuracy": "accuracy", "Recovery": "recovery", "Luck": "luck", "Specialty": "specialty",
        "TSI": "tsi"
    }

    chamster_data = {attribute_key: attributes_dict.get(trait_type, None) for trait_type, attribute_key in chamster_attributes.items()}

    chamster_model = {
        "model": "chamsterapp.Chamster",
        "pk": chamster_pk,
        "fields": {
            "encoded_id": encoded_id,
            "name": name,
            "type": chamster_type,
            "background": chamster_data.get("background"),
            "fur": chamster_data.get("fur"),
            "shirt": chamster_data.get("shirt"),
            "pants": chamster_data.get("pants"),
            "head": chamster_data.get("head"),
            "eyes": chamster_data.get("eyes"),
            "club": chamster_data.get("club"),
            "power": chamster_data.get("power"),
            "putting": chamster_data.get("putting"),
            "accuracy": chamster_data.get("accuracy"),
            "recovery": chamster_data.get("recovery"),
            "luck": chamster_data.get("luck"),
            "specialty": chamster_data.get("specialty"),
            "tsi": chamster_data.get("tsi"),
        }
    },    
    
    count += 1
    print("count: ", count)
    
    # Save the NFT image to static folder
    with open("../chamsterapp/fixtures/updated_test.json", "w") as json_file:
        json.dump(chamster_model, json_file, indent=4)  # 'indent' is optional for pretty formatting

    # ChamsertOwner Model
    # owner_address_id = database["owner_address"]["id"]
    # owner_address_encoded_id = database["owner_address"]["encoded_id"]
    # owner_id = database["owner"]["id"]
    # owner_encoded_id = database["owner"]["encoded_id"]
    # owner_username = database["owner"]["owner_username"]
    # owner_name = database["owner"]["owner_name"]
    # owner_avatar_uri = database["owner"]["owner_avatar_uri"]       

    # Transaction Model 
    # for event in events:
        # xch_price = database["xch_price"]
        # event_index = event["event_index"]
        # event_type = event["event_type"]
        # event_timestamp = event["timestamp"]
        # event_xch_price = event["xch_price"]
        # event_address_id = event["address"]["id"]
        # event_address_encoded_id = event["address"]["encoded_id"]
        # event_verification_state = event["owner"]["verification_state"]
        # event_owner_id = event["owner"]["id"]
        # event_owner_encoded_id = event["owner"]["encoded_id"]
        # event_previous_address_id = event["previous_address"]["id"]
        # event_previous_address_encoded_id = event["previous_address"]["encoded_id"]
        # event_previous_owner = event["previous_owner"]
        # event_previous_owner_id = event["previous_owner"]["id"]
    
    # Save the NFT image to static folder
    # with open(f"../theme/static/chamsterapp/img/nft/test/{encoded_id}.png", "wb") as img_file:
    #     img_response = requests.get(img_uri)
    #     img_file.write(img_response.content)
    #     print("Image saved")
    
    # Save Owner Avatar image to static folder
    # with open(f"..theme/static/chamsterapp/img/avatar/{owner_id}.png", "wb") as img_file:
    #     img_response = requests.get(owner_avatar_uri)
    #     img_file.write(img_response.content)
    #     print("Image saved")
    

    # chamster_owner_model = {
    #     "model": "chamsterapp.ChamsterOwner",
    #     "pk": chamster_owner_id,
    #     "fields": {
    #         "transaction_id": transaction_id,
    #         "chamster_id": chamster_pk,
    #         "owner_address_id": owner_address_id,
    #         "owner_address_encoded_id": owner_address_encoded_id,
    #         "owner_id": owner_id,
    #         "owner_encoded_id": owner_encoded_id,
    #         "owner_username": owner_username,
    #         "owner_name": owner_name,
    #         "owner_avatar_uri": owner_avatar_uri,
    #     }
    # },
    # transaction_model = {
    #     "model": "chamsterapp.Transaction",
    #     "pk": transaction_id,
    #     "fields": {
    #         "chamster_id": chamster_pk,
    #         "xch_price": xch_price,
    #         "event_index": event_index,
    #         "event_type": event_type,
    #         "event_timestamp": event_timestamp,
    #         "event_xch_price": event_xch_price,
    #         "event_address_id": event_address_id,
    #         "event_address_encoded_id": event_address_encoded_id,
    #         "event_verification_state": event_verification_state,
    #         "event_owner_id": event_owner_id,
    #         "event_owner_encoded_id": event_owner_encoded_id,
    #         "event_previous_address_id": event_previous_address_id,
    #         "event_previous_address_encoded_id": event_previous_address_encoded_id,
    #         "event_previous_owner": event_previous_owner,
    #         "event_previous_owner_id": event_previous_owner_id,
    #     }
    # },



        

        
    # Create the Chmaster model fixutre file and save to fixutres folder
        
    # Create the Owner model fixture file and save to fixutres folder
        
    # Create the Transaction model fixture file and save to fixutres folder 
        
    # Create the Assets model fixutre file and save to fixutres folder
