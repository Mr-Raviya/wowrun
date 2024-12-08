import requests
import random
import json
import os

try:
    print("---------- MegaRun Hack by Raviya ----------")
    print("\nScript Started !\n")

    file_path = "main_auth.json"

    if not os.path.exists(file_path):
        # File does not exist
        print(f"File '{file_path}' does not exist.")

        # Prompt the user for authCode
        auth_code = input("-> Enter the authCode: ")

        def generate_code(length):
            # Generate a random hexadecimal code of the specified length
            return ''.join(random.choices('0123456789abcdef', k=length))

        # Generate a single code of either 15 or 16 characters
        length = random.choice([15, 16])  # Randomly choose between 15 or 16 characters
        generated_Did = generate_code(length)

        print("--> Device id generated !")

        def generate_android_user_agent():
            android_versions = ['12', '11', '10', '9', '8', '13', '6', '7', '5', '14']  # List of Android versions
            device_models = [
                "GKWS6", "vivo 1904", "Pixel 6", "Galaxy S21", "OnePlus 8", "Redmi Note 10", "Moto G9", "Realme 7", "Pilex 5", "Pixel 7", "Pixel 8", "Galaxy S22", "Galaxy S24", "Galaxy S22 Ultra"
            ]  # Example device models
            build_numbers = [
                "W528JS", "PPR1.180610.011", "RQ3A.210905.001", "SP1A.210812.015", "TP1A.221005.002"
            ]  # Example build numbers
            chrome_versions = [
                "95.0.4638.74", "94.0.4606.71", "93.0.4577.82", "92.0.4515.131", "91.0.4472.120"
            ]  # Chrome versions

            android_version = random.choice(android_versions)
            device_model = random.choice(device_models)
            build_number = random.choice(build_numbers)
            chrome_version = random.choice(chrome_versions)

            user_agent = (
                f"Mozilla/5.0 (Linux; Android {android_version}; {device_model} Build/{build_number}; wv) "
                f"AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{chrome_version} Mobile Safari/537.36"
            )

            return user_agent

        User_Agent = generate_android_user_agent()
        print("--> User Agent generated !")
        
        # Authenticate and get the access token
        auth_url = "https://api.wow.lk/superapp-user-profile-service/user/authenticate"
        auth_payload = json.dumps({
            "authCode": auth_code,
            "platform": "MOBILE",
            "grantType": "auth",
            "integrityToken": "",
            "mobileOS": "android"
        })
        auth_headers = {
            'Host': 'api.wow.lk',
            'Accept': 'application/json, text/plain, */*',
            'Authorization': 'Bearer undefined',
            'Accept-Language': 'en',
            'X-Device-Id': f'{generated_Did}',
            'Content-Type': 'application/json',
            'Content-Length': str(len(auth_payload)),
            'Accept-Encoding': 'gzip, deflate, br',
            'User-Agent': 'okhttp/4.9.2',
            'Connection': 'keep-alive'
        }

        auth_response = requests.post(auth_url, headers=auth_headers, data=auth_payload)
        auth_data = auth_response.json()

        # Extract the accessToken
        main_access_JWT = auth_data.get("data", {}).get("accessToken")
        main_refresh_JWT = auth_data.get("data", {}).get("refreshCode")
        mobile_no = auth_data['data']['msisdn']

        if not main_access_JWT:
            print("--> Failed to auth !")
            print(auth_response.text)
            exit()

        with open("main_auth.json", "w") as json_file:
            json.dump({"main_access_JWT": main_access_JWT, "main_refresh_JWT": main_refresh_JWT, "generated_Did": generated_Did, "mobile_no": mobile_no, "User_Agent": User_Agent}, json_file, indent=4)  # Save to JSON file

        print("--> Your mobile number:", mobile_no)
        print("--> Auth Tokens & Keys saved to 'main_auth.json'")

        # Use the access token in the second request
        app_url = "https://api.wow.lk/superapp-mini-app-authentication-service/application/authentication"
        app_payload = json.dumps({
            "appId": "MEGA_GAMES",
            "msisdn": f"{mobile_no}",
            "deviceId": f"{generated_Did}"
        })
        app_headers = {
            'Accept': 'application/json, text/plain, */*',
            'Authorization': f'Bearer {main_access_JWT}',
            'Accept-Language': 'en',
            'x-device-id': f'{generated_Did}',
            'Content-Type': 'application/json',
            'Content-Length': str(len(app_payload)),
            'User-Agent': 'okhttp/4.9.1',
            'Connection': 'keep-alive',
            'Host': 'api.wow.lk',
            'Accept-Encoding': 'gzip, deflate, br'
        }

        app_response = requests.post(app_url, headers=app_headers, data=app_payload)
        app_data = app_response.json()

        # Extract token (use the previous response processing)
        print("--> Requesting game access token !")
        print("--> Response code:", app_response.status_code)

        token = app_data.get("data", {}).get("token")

        if not token:
            print("--> Failed to retrieve token !")
            print(app_response.text)
            exit()

        # Prepare the URL and headers
        token_url = f"https://dshl99o7otw46.cloudfront.net/api/user/v1/access-token/{token}"
        token_headers = {
            'User-Agent': f'{User_Agent}',
            'Accept': '*/*',
            'Referer': f'https://dshl99o7otw46.cloudfront.net/landingpage/v16/index.html?token={token}',
            'Accept-Language': 'en-US,en;q=0.9',
            'x-requested-with': 'lk.wow.superman',
            'Accept-Encoding': 'gzip, deflate, br',
            'Host': 'dshl99o7otw46.cloudfront.net',
            'Content-Length': '0',
            'Connection': 'keep-alive'
        }

        # Send the GET request
        token_response = requests.get(token_url, headers=token_headers)
        token_data = token_response.json()

        game_access_JWT = token_data.get('data', {}).get('access_token')  # Extract the access_token

        with open("game_auth.json", "w") as json_file:
            json.dump({"game_access_JWT": game_access_JWT, "User_Agent": User_Agent}, json_file, indent=4)  # Save to JSON file

        print("--> Game Tokens saved to 'game_auth.json'")

    # Check if the file exists
    else:
        status_code = 0
        while status_code != 201: 
        
            # File exists, read the tokens
            with open(file_path, "r") as json_file:
                auth_data = json.load(json_file)
                main_access_JWT = auth_data.get("main_access_JWT")
                main_refresh_JWT = auth_data.get("main_refresh_JWT")
                generated_Did = auth_data.get("generated_Did")
                mobile_no = auth_data.get("mobile_no")
                User_Agent = auth_data.get("User_Agent")
            
            # Check if tokens are available
            if main_access_JWT and main_refresh_JWT:

                # Use the access token in the second request
                app_url = "https://api.wow.lk/superapp-mini-app-authentication-service/application/authentication"
                app_payload = json.dumps({
                    "appId": "MEGA_GAMES",
                    "msisdn": f"{mobile_no}",
                    "deviceId": f"{generated_Did}"
                })
                app_headers = {
                    'Accept': 'application/json, text/plain, */*',
                    'Authorization': f'Bearer {main_access_JWT}',
                    'Accept-Language': 'en',
                    'x-device-id': f'{generated_Did}',
                    'Content-Type': 'application/json',
                    'Content-Length': str(len(app_payload)),
                    'User-Agent': 'okhttp/4.9.1',
                    'Connection': 'keep-alive',
                    'Host': 'api.wow.lk',
                    'Accept-Encoding': 'gzip, deflate, br'
                }

                app_response = requests.post(app_url, headers=app_headers, data=app_payload)
                status_code = app_response.status_code

                if app_response.status_code != 201:
                    print("--> Response code:", app_response.status_code)
                    print("--> Auth refreshing !")
            
                    refresh_url = "https://api.wow.lk/superapp-user-profile-service/user/authenticate"

                    refresh_payload = json.dumps({
                    "refreshCode": f"{main_refresh_JWT}",
                    "platform": "MOBILE",
                    "grantType": "refresh",
                    "msisdn": f"{mobile_no}",
                    "integrityToken": "",
                    "mobileOS": "android"
                    })
                    refresh_headers = {
                    'Accept': 'application/json, text/plain, */*',
                    'Authorization': 'Bearer undefined',
                    'Accept-Language': 'en',
                    'x-device-id': f'{generated_Did}',
                    'Content-Type': 'application/json',
                    'User-Agent': 'okhttp/4.9.2',
                    'Host': 'api.wow.lk',
                    'Content-Length': str(len(app_payload)),
                    'Connection': 'keep-alive',
                    'Accept-Encoding': 'gzip, deflate, br'
                    }

                    refresh_response = requests.request("POST", refresh_url, headers=refresh_headers, data=refresh_payload)
                    refresh_data = refresh_response.json()

                    # Extract the accessToken
                    main_access_JWT = refresh_data["data"]["data"]["accessToken"]
                    main_refresh_JWT = refresh_data["data"]["data"]["refreshCode"]

                    if not main_access_JWT:
                        print("--> Failed to refresh !")
                        print(refresh_response.text)
                        exit()

                    with open("main_auth.json", "w") as json_file:
                        json.dump({"main_access_JWT": main_access_JWT, "main_refresh_JWT": main_refresh_JWT, "generated_Did": generated_Did, "mobile_no": mobile_no, "User_Agent": User_Agent}, json_file, indent=4)  # Save to JSON file

                    print("--> Auth Tokens refreshed to 'main_auth.json'")
                        
        app_data = app_response.json()

        print("--> Requesting game access token !")
        print("--> Response code:", app_response.status_code)

        # Extract token (use the previous response processing)
        token = app_data.get("data", {}).get("token")

        if not token:
            print("--> Failed to retrieve token !")
            print(app_response.text)
            exit()

        # Prepare the URL and headers
        token_url = f"https://dshl99o7otw46.cloudfront.net/api/user/v1/access-token/{token}"
        token_headers = {
            'User-Agent': f'{User_Agent}',
            'Accept': '*/*',
            'Referer': f'https://dshl99o7otw46.cloudfront.net/landingpage/v16/index.html?token={token}',
            'Accept-Language': 'en-US,en;q=0.9',
            'x-requested-with': 'lk.wow.superman',
            'Accept-Encoding': 'gzip, deflate, br',
            'Host': 'dshl99o7otw46.cloudfront.net',
            'Content-Length': '0',
            'Connection': 'keep-alive'
            }

        # Send the GET request
        token_response = requests.get(token_url, headers=token_headers)
        token_data = token_response.json()

        game_access_JWT = token_data.get('data', {}).get('access_token')  # Extract the access_token

        with open("game_auth.json", "w") as json_file:
            json.dump({"game_access_JWT": game_access_JWT, "User_Agent": User_Agent}, json_file, indent=4)  # Save to JSON file

        print("--> Game Tokens saved to 'game_auth.json'")

except KeyboardInterrupt:
    print("\nThanks for using MegaRun Hack by Raviya.")
