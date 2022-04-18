import requests

url = "https://api.gcdn.co/vp/api/videos" #ссылка GET апроса на получение списка видео
apiToken = "APIkey 1404$38b1d4666a8e3c3a0c2459c146e8be1397e7452233edcb2db77a6136715272f4e569722667fc8a4da254f4c2c3cdf7f298f1e1a584c6b0284578f86d533e0979"

headers = {'Authorization': apiToken} #Заголовок для авторизации через APIkey
response = requests.get(url, headers=headers) #GET запрос для получения списка видео

print(response.json()) #вывод списка видео в консоль
