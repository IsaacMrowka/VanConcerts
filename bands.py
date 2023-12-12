import requests
import json
import shutil
import os
import datetime

#scraping portion

url = "https://seatgeek.ca/api/events?page=1&listing_count.gte=1&lat=49.278149780386&lon=-123.115234375&range=23mi&sort=datetime_local.asc&taxonomies.id=2000000&client_id=MTY2MnwxMzgzMzIwMTU4"

payload = {}
headers = {
  'authority': 'seatgeek.ca',
  'accept': 'application/json, text/plain, */*',
  'accept-language': 'en-US,en;q=0.9',
  'cookie': 'sg_l=en-CA; sg_c=CAD; sixpack_client_id=0da4ba6c-4ad2-47cc-b705-65292a6c9d4f; sg_uuid=789342d2-284d-51d4-e5cc-65b6953aa70a; sg_session=535fb637136a57b716ee0f6989ad8345; SeatGeekEntrance=category=entrance:affiliate:225%3Baid=225%3Bpid=%3Brid=%3Bgid=%3Bquery=%3Bdt=%3Bap=%3BadId=; SeatGeekAffiliate=%5B225%2Cnull%2C900716022%2Cnull%2Cnull%5D; SeatGeekTimer=1702260990; datadome=vsHbmlSbvkrz~WadLcR9A2tptD3N~SiynNttRaHIMZ2IXPZoCYo5ytVVoM45T76bLVauEgbMmE_3MfXNPoHNxdNSZKmN1zEyJ4483jtTQHumVF1B9aD1L8FfnG0fZx8~; datadome=ojcEJBfAK_7fh11EQTc22xllK~zkSLio0OHL6m8EPDgY6fF1hwdAeGmCN34~P0646_S1~NEJg3Q_qYyZBVgKgR5AUWYoY5KGzQSs4VCBoMZKIcIkIIwnDCTiOiaqbrmK',
  'if-none-match': 'W/"5b4de6348a18a8347f20cdd06d210c210238342f"',
  'referer': 'https://seatgeek.ca/cities/vancouver/concerts',
  'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'sixpack-client-id': '0da4ba6c-4ad2-47cc-b705-65292a6c9d4f',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
  'x-sg-currency-code': 'CAD',
  'x-sg-locale': 'en-CA',
  'x-sg-sift-session-id': '0da4ba6c-4ad2-47cc-b705-65292a6c9d4f'
}

response = requests.request("GET", url, headers=headers, data=payload)

jsondata = json.loads(response.text)

#text file portion

# Set the source and destination paths

desired_working_dir = "C:/Users/imrow/Documents/CODE/VisualStudioCode/VanConcerts/"
os.chdir(desired_working_dir)
print("Current Working Directory:", os.getcwd())

source_path = "C:/Users/imrow/Documents/CODE/VisualStudioCode/VanConcerts/BandsPlaying.txt"
destination_path = "C:/Users/imrow/Desktop/BandsPlaying.txt"

f = open("BandsPlaying.txt", "w")
print(datetime.date.today(), file=f)

for band in jsondata['events']:
    artist = band['performers'][0]['name']
    time = band['datetime_utc']
    place = band['venue']['name_v2']
    print(artist, ", Time: ", time,", Place: ", place, file=f )

f.close()
shutil.move(source_path, destination_path)
