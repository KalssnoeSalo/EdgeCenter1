import json
import requests
import tus
from tus import upload
from tusclient.uploader import Uploader

createVideo_url = "https://api.gcdn.co/vp/api/videos" #Ссылка для POST запроса для создания слота для загрузки видео
apiToken = "APIkey 1404$38b1d4666a8e3c3a0c2459c146e8be1397e7452233edcb2db77a6136715272f4e569722667fc8a4da254f4c2c3cdf7f298f1e1a584c6b0284578f86d533e0979"
apiKey = "1404$38b1d4666a8e3c3a0c2459c146e8be1397e7452233edcb2db77a6136715272f4e569722667fc8a4da254f4c2c3cdf7f298f1e1a584c6b0284578f86d533e0979"

headers = {'Authorization': apiToken} #Заголовки для авторизации через API
jsonCode = {
"video": {
"name": "Video",
"description": "Video1",
"origin_url": "",
"screenshot_id": 0,
"ad_id": 2,
"projection": "regular",
"client_user_id": 10,
"stream_id": 1
}
}#JSON од для POST запроса

res = requests.post(createVideo_url, json=jsonCode, headers=headers) #Записываение ответа от POST запроса для создания слота для заливки видео в переменную res

data = json.loads(res.text) #преобразование JSON кода в словарь для удобного получения данных по заголовкам

print(res.json()) #Вывод результата POST запроса в виде JSON кода

videoId = data['id'] #Получение значения id видео из JSON ответа
videoUrl = ('https://api.gcdn.co/vp/api/videos/' + str(videoId)+"/upload") #создание url
clientId = data['client_id']

res2 = requests.get(videoUrl, headers=headers) #GET запрос для получения URL и токена видео
videoToken = json.loads(res2.text)['token'] #получение значения токаена из ответа GET запроса
videoUploadUrl = 'https://vp-uploader-dt.gcdn.co/upload' #ссылка для загрузки видео

print(videoId)
print(videoUrl)
print(videoUploadUrl)
print(videoToken)
print(clientId)
print(res2.json())

#ЧАСТЬ С ЗАГРУЗКОЙ ВИДЕО ЧЕРЕЗ TUS
metadata = {'filename': 'Nya! milk so good!.mp4', 'client_id': str(clientId), 'video_id': str(videoId), 'token': str(videoToken)}

FILE_PATH = 'Nya! milk so good!.mp4' #путь к файлу, который нужно загрузить
TUS_ENDPOINT = videoUploadUrl #ссылка для загрузки видео
headers2 = {'Authorization': videoToken} #заголовки для авторизации с использование ранее полученного токена видео
CHUNK_SIZE = 256000 #указание размера чанка загрузки

with open(FILE_PATH, 'rb') as file:
    tus.upload(tus_endpoint=TUS_ENDPOINT, file_obj=file, headers=headers2, chunk_size=CHUNK_SIZE, metadata=metadata) #загрузка файла через метод upload с ранее задаными нами параметрами