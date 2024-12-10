import requests
import json
import hashlib
import random
import time

try:
    while True:
        print("\n---------> MegaRun Hack by Raviya <---------")
        choice = input("\n-> Press 'Y' to Start the Game or 'N' to Exit: ").strip().upper()

        if choice == 'Y':
                
            # Read the access_token from the file
            with open("game_auth.json", "r") as json_file:
                data = json.load(json_file)  # Load the JSON data from the file
                game_access_JWT = data.get("game_access_JWT")  # Get the access_token
                User_Agent = data.get("User_Agent")

            # Use the access_token in your code
            if not game_access_JWT:
                print("\n--> Access token not found.")
                exit()

            game_url = "https://dshl99o7otw46.cloudfront.net/api/game/v1/game-session/9482808f-72c3-43a5-96c4-38c3d3a7673e"

            game_payload = json.dumps({
            "current_level_uuid": "3ae643db-5410-4f04-a89b-e8b9539a62d6",
            "current_item_uuid": "1ad5304f-d000-41ac-bd8b-6169c1dde21b",
            "current_character_uuid": "aa2fb3c0-a3fd-4e78-b925-4b0ba9f08ab9"
            })
            game_headers = {
            'Authorization': f'Bearer {game_access_JWT}',
            'Origin': 'https://dshl99o7otw46.cloudfront.net',
            'User-Agent': f'{User_Agent}',
            'Content-Type': 'application/json',
            'Accept': '*/*',
            'Referer': 'https://dshl99o7otw46.cloudfront.net/games/9482808f-72c3-43a5-96c4-38c3d3a7673e/build/v19/index.html?platform=pwa&version=200',
            'Accept-Language': 'en-US,en;q=0.9',
            'x-requested-with': 'lk.wow.superman',
            'Accept-Encoding': 'gzip, deflate, br',
            'Host': 'dshl99o7otw46.cloudfront.net',
            'Content-Length': str(len(game_payload)),
            'Connection': 'keep-alive'
            }

            game_response = requests.request("POST", game_url, headers=game_headers, data=game_payload)
            game_data = game_response.json()

            # Extract token (use the previous response processing)
            game_token = game_data.get("data", {}).get("token")

            if not game_token:
                print("--> Failed to retieve game token !")
                print(game_response.text)
                exit()
            
            # Extract initial state
            initial_state = game_data.get("data", {}).get("initial_state")

            # Generating the idempotency key
            def gen_key(initial_state):
                p = 153451
                q = 846544
                z = 575896
                
                # Calculate the key
                key = (p ^ initial_state) + (q ^ (z >> 4)) + (1 ^ q) + initial_state
                
                # Return the MD5 hash of the calculated key
                return hashlib.md5(str(key).encode()).hexdigest()

            # Generate the key
            key = gen_key(initial_state)

            results_url = "https://dshl99o7otw46.cloudfront.net/api/game/v1/profile/data"

            results_headers = {
            'User-Agent': f'{User_Agent}',
            'Accept-Encoding': 'gzip, deflate, br',
            'authorization': f'Bearer {game_access_JWT}',
            'x-requested-with': 'lk.wow.superman',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://dshl99o7otw46.cloudfront.net/games/9482808f-72c3-43a5-96c4-38c3d3a7673e/build/v19/index.html?platform=pwa&version=200',
            'accept-language': 'en-US,en;q=0.9',
            'Connection': 'keep-alive',
            'Host': 'dshl99o7otw46.cloudfront.net',
            'accept': '*/*',
            'Content-Length': '0'
            }

            results_response = requests.request("GET", results_url, headers=results_headers)
            results_data = results_response.json()

            daily_box = results_data.get("data", {}).get("daily_winning_chances", 0)
            used_box = results_data.get("data", {}).get("consumed_chances", 0)
            total_won = results_data.get("data", {}).get("won_data", 0)
            remain_won = results_data.get("data", {}).get("remaining_data", 0)
            
            print("\n----> Game is starting !\n")

            print("-> Daily Chances ", daily_box)
            print("-> Used Chances  ", used_box)
            print(f"-> Total WON Data {total_won} MB")
            print(f"-> Remain to WIN  {remain_won} MB\n")

            def show_progress_bar(duration):
                total_steps = 25  # Length of the progress bar
                step_duration = duration / total_steps
                
                print(f"Waiting ({int(duration)} sec) [", end="", flush=True)
                for i in range(total_steps + 1):
                    percentage = int((i / total_steps) * 100)
                    print("#", end="", flush=True)
                    time.sleep(step_duration)
                print(f"] {percentage}% Done!\n")    

            # Random time delay between 18 and 26 seconds
            time_delay = random.uniform(16, 26)

            # Show progress bar
            show_progress_bar(time_delay)

            print("\n----> Game is started !\n")

            # Initialize the starting score
            current_score = 0

            for i in range(1, 101):  # 1 to 100 for better tracking
                # Increment score randomly by 5, 10, or 20
                increment = random.choice([5, 10, 20])
                current_score += increment

                gift_url = f"https://dshl99o7otw46.cloudfront.net/api/game/v1/game-session/random-gift/{game_token}/1"
                
                # Create the payload
                gift_payload = json.dumps({
                    "score": current_score
                })
                
                # Define headers
                gift_headers = {
                    'Authorization': f'Bearer {game_access_JWT}',
                    'Origin': 'https://dshl99o7otw46.cloudfront.net',
                    'User-Agent': f'{User_Agent}',
                    'idempotency-key': f'{key}',
                    'Content-Type': 'application/json',
                    'Accept': '*/*',
                    'Referer': 'https://dshl99o7otw46.cloudfront.net/games/9482808f-72c3-43a5-96c4-38c3d3a7673e/build/v19/index.html?platform=pwa&version=200',
                    'Accept-Language': 'en-US,en;q=0.9',
                    'x-requested-with': 'lk.wow.superman',
                    'Content-Length': str(len(gift_payload)),
                    'Host': 'dshl99o7otw46.cloudfront.net',
                    'Accept-Encoding': 'gzip, deflate, br',
                    'Connection': 'keep-alive'
                }

                # Send the POST request
                gift_response = requests.post(gift_url, headers=gift_headers, data=gift_payload)
                gift_data = gift_response.json()

                print("\n---------> MegaRun Hack by Raviya <---------")
                print(f"\nBox {i} Score = {current_score}\n")
                
                # Extract 'amount' value
                amount = gift_data.get("data", {}).get("amount", 0)

                # Print message based on 'winner' value
                if amount != 0:
                    print(f"-> Congragulation! you have WON {amount} MB")

                    results_url = "https://dshl99o7otw46.cloudfront.net/api/game/v1/profile/data"

                    results_headers = {
                    'User-Agent': f'{User_Agent}',
                    'Accept-Encoding': 'gzip, deflate, br',
                    'authorization': f'Bearer {game_access_JWT}',
                    'x-requested-with': 'lk.wow.superman',
                    'sec-fetch-site': 'same-origin',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-dest': 'empty',
                    'referer': 'https://dshl99o7otw46.cloudfront.net/games/9482808f-72c3-43a5-96c4-38c3d3a7673e/build/v19/index.html?platform=pwa&version=200',
                    'accept-language': 'en-US,en;q=0.9',
                    'Connection': 'keep-alive',
                    'Host': 'dshl99o7otw46.cloudfront.net',
                    'accept': '*/*',
                    'Content-Length': '0'
                    }

                    results_response = requests.request("GET", results_url, headers=results_headers)
                    results_data = results_response.json()

                    daily_box = results_data.get("data", {}).get("daily_winning_chances", 0)
                    used_box = results_data.get("data", {}).get("consumed_chances", 0)
                    total_won = results_data.get("data", {}).get("won_data", 0)
                    remain_won = results_data.get("data", {}).get("remaining_data", 0)

                else:
                    print("-> Try again!, good luck for next round")
                
                print("---> Daily Chances ", daily_box)
                print("---> Used Chances  ", used_box)
                print(f"-> Total WON Data   {total_won} MB\n")

                # Random time delay between 18 and 26 seconds
                time_delay = random.uniform(16, 26)

                # Show progress bar
                show_progress_bar(time_delay)
            break

        elif choice == 'N':
            print("\n-> Exiting, Thanks for using MegaRun Hack by Raviya !")
            break

        else:
            print("Invalid input. Please press 'Y' or 'N'.\n")

except KeyboardInterrupt:
    print("\nThanks for using MegaRun Hack by Raviya !")