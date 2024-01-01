# Mintgarden API to call on NFT owner's XCH_addresses
from time import sleep
import requests
import time

# Pull in NFT's database
# Collection to pull data from:
# Chamster Founders Series  = "col1hn3a9j6pgxtel9nl7duxatc0hk2w5e27leze3r34h46qptnyesms04rcac"
# Chamster Golfers Series = "col12zrl5dh4qwahqwf30d7n33fsun6jhp4rvlqaujqvewjp02uvx63st8v8fu"


# Get and setting the NFT's ID and name:
next_list = []
nft_metadata = []

i = 1
while (
    i < 7
):  # need to imrpove code so it can automatically stop when the last page is reached
    print(f"page {i}")
    if i == 1:
        url = "https://api.mintgarden.io/collections/col12zrl5dh4qwahqwf30d7n33fsun6jhp4rvlqaujqvewjp02uvx63st8v8fu/nfts?page=>"
    else:
        for next in next_list:
            url = f"https://api.mintgarden.io/collections/col12zrl5dh4qwahqwf30d7n33fsun6jhp4rvlqaujqvewjp02uvx63st8v8fu/nfts?page={next}"

    page_request = requests.get(url)
    database = page_request.json()
    next_address = database["next"]
    next_list.append(next_address)
    items = database["items"]

    for item in items:
        nftId = item["encoded_id"]
        nftName = item["name"]
        index = nftName.find("#")
        if index != -1:  # If '#' is found in the string
            number_after_hash = nftName[index + 1 :]  # Extract the number after '#'
            file_name = number_after_hash
        else:
            print("No '#' found in the string.")

        print(nftId, nftName, file_name)
        results = {
            "nftId": nftId,
            "nftName": nftName,
            "file_name": file_name,
        }
        nft_metadata.append(results)
    i += 1
    time.sleep(page_request.elapsed.total_seconds())
print(f"A total of {len(nft_metadata)} nfts has been collected")


# Getting the NFT's Image and Json file:

for item in nft_metadata:
    nftId = item["nftId"]
    fileName = item["file_name"]
    url = f"https://api.mintgarden.io/nfts/{nftId}"
    page_request = requests.get(url)
    database = page_request.json()
    img_uri = database["data"]["data_uris"][0]
    json_uri = img_uri.replace(".png", ".json")
    print(f"{img_uri} is being retrieved...")
    print(f"{json_uri} is being retrieved...")

    # Save the image
    with open(f"images/{fileName}.png", "wb") as img_file:
        img_response = requests.get(img_uri)
        img_file.write(img_response.content)
        print("Image saved")

    # Save the metadata
    with open(f"metadata/{fileName}.json", "wb") as metadata_file:
        metadata_response = requests.get(json_uri)
        metadata_file.write(metadata_response.content)
        print("Metadata saved")