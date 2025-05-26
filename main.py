import requests

with open("key.txt", "r") as file:
    access_token = file.readline()

user_id = "293049398"

response = requests.get(
    "https://api.vk.com/method/friends.get",
    params={
        "user_id": user_id,
        "access_token": access_token,
        "v": "5.199",
        "fields": "first_name,last_name"
    }
)

if response.status_code == 200:
    data = response.json()
    if "response" in data:
        friends = data["response"]["items"]
        count = data["response"]["count"]
        print(f"Список друзей пользователя (всего: {count}):")
        counter = 0
        for friend in friends:
            counter += 1
            print(
                f"{counter}. {friend['first_name']} {friend['last_name']} ( id = {friend['id']} )")
    else:
        print("Ошибка с данными")
else:
    print("Ошибка соединения с API")
