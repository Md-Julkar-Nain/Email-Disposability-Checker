import requests
email = input('Your Email: ')
url = f'https://api.mailcheck.ai/email/{email}'
res = requests.get(url)
data = res.json()

if res.status_code == 200:
    disposable = data.get('disposable')
    if not disposable:
        print("You are allowed to open account.")
    else:
        print("Invalid Email Address.")



