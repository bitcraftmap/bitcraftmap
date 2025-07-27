import requests
import json
import math
import time

sleep = 1
limit = 100
all_claims = []
current_page = 1
claims_url = 'https://bitjita.com/api/claims'
user_agent = {'User-agent': 'Manserk For bitcraftmap.com'}

# Step one : load the current json


# Todo : 
# Transform the data to use the entityid as json key
# For each entityid, get building data

# Get info 
# bank ? 
# Waystone ? 
# Market ?
# number of NPC ?