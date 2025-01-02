import requests

def get_followers_count(username):
    url = f"https://www.instagram.com/{username}/?__a=1"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['graphql']['user']['edge_followed_by']['count']
    else:
        return None

def list_followers_with_199_or_more_followers(target_username):
    url = f"https://www.instagram.com/{target_username}/?__a=1"
    response = requests.get(url)
    if response.status_code == 200:
        followers = response.json()['graphql']['user']['edge_followed_by']['edges']
        for follower in followers:
            follower_username = follower['node']['username']
            follower_count = get_followers_count(follower_username)
            if follower_count is not None and follower_count >= 199:
                print(follower_username)
    else:
        print("Kullanıcı bulunamadı")

if __name__ == "__main__":
    target_username = input("Hedef hesabın kullanıcı adını girin: ")
    list_followers_with_199_or_more_followers(target_username)
