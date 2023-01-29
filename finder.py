import sys
import requests
import json

def get_new_token():

    auth_server_url = "https://api.petfinder.com/v2/oauth2/token"
    client_id = 'ID'
    client_secret = 'SECRET'

    token_req_payload = {'grant_type': 'client_credentials'}

    token_response = requests.post(auth_server_url,
    data=token_req_payload, verify=False, allow_redirects=False,
    auth=(client_id, client_secret))
                
    if token_response.status_code !=200:
        print("Failed to obtain token from the OAuth 2.0 server", file=sys.stderr)
        sys.exit(1)

    tokens = json.loads(token_response.text)
    return tokens['access_token']

    ## 
    ## 	obtain a token before calling the API for the first time
    ##
    
def find(location="98391", distance="50", size="small,medium,large,xlarge"):
    token = get_new_token()

    test_api_url = "https://api.petfinder.com/v2/animals?limit=10&type=dog" + "&" + location + "&" + distance + "&" + size
    api_call_headers = {'Authorization': 'Bearer ' + token}
    response = requests.get(test_api_url, headers=api_call_headers).json()
    results = []
    for a in response["animals"]:
        if a["photos"]:
            dog = {"name": a["name"], "url": a["url"], "photo": a["photos"][0]["full"]}
            results.append(dog)
    return results
            

#?location=98391&sort=distance&location=98391&limit=50&type=dog