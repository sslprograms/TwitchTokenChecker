import requests, threading, time

upt = open('input\\upt.txt', 'r').read().splitlines()
tokens = open('input\\tokens.txt', 'r').read().splitlines()

if len(upt) > len(tokens) :
    tokens = upt
else:
    tokens = tokens

def checkToken(token):
    with requests.session() as session:
        session.headers['Authorization'] = f'Bearer {token}'

        validCheck = session.get(
            'https://id.twitch.tv/oauth2/validate'
        )


        if validCheck.status_code == 200:
            print(f'> Token Valid | {token}')
            open('output\\validTokens.txt', 'a').write(f'{token}\n')
        else:
            print(f'> Token Invalid | {token}')


for x in tokens:
    try:
        x = x.split(':')[2]
    except:
        x = x 
    threading.Thread(target=checkToken, args=(x,)).start()
    time.sleep(0.005)

input()