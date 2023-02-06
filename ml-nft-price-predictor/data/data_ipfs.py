import pandas as pd
import requests

base_url = "https://ipfs.io/ipfs/QmeSjSinHpPnmXmspMjwiXyN6zS4E9zccariGR3jxcaWtq/"

# Initialize empty dataframe to store token data
df = pd.DataFrame(columns=["token_id", "TRAITS_COUNT", "EARRING", "BACKGROUND", "FUR", "EYES", "MOUTH", "HAT", "CLOTHES"])

# Iterate through 1 to 10000 and retrieve data for each URL
for i in range(1, 10001):
    try:
        url = base_url + str(i)
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            attributes = data['attributes']
            # Store the number of traits
            df.loc[i-1, "TRAITS_COUNT"] = len(attributes)
            # Store the values of each trait_type in its corresponding column
            for attribute in attributes:
                trait_type = attribute['trait_type'].upper()
                value = attribute['value']
                column_name = trait_type
                df.loc[i-1, column_name] = value
            df.loc[i-1, "token_id"] = i
            print(f"Stored data for token number: {i}")
        else:
            print(f"Failed to retrieve data from URL: {url}")
    except Exception as ex:
        print (url)
        print (ex)

df.to_csv("NFT_traits.csv", index=False)