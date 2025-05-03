import requests

url = 'https://epg.pw/api/epg.xml?channel_id=403626'

response = requests.get(url)
if response.status_code == 200:
    with open("epg.xml", "wb") as f:
        f.write(response.content)
    print("EPG updated successfully.")
else:
    print(f"Failed to download EPG. Status code: {response.status_code}")
