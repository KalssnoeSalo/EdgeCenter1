import json
import requests

urlQueue = 'https://api.gcdn.co/vp/api/tasks.json' #ссылка для POST запроса постановки видео в очередь на обработку
apiToken = "APIkey 1404$38b1d4666a8e3c3a0c2459c146e8be1397e7452233edcb2db77a6136715272f4e569722667fc8a4da254f4c2c3cdf7f298f1e1a584c6b0284578f86d533e0979"
headers = {'Authorization': apiToken} #Заголовки для авторизации через API

jsonCode = {"task":
            {"url": "https://s-ed1.cloud.gcore.lu/9208-mediaplatform78268/videos/9fSB0JwbFCbDsh9d.mp4", #ссылка на видео для обработки
            "type": "cv",
            "keyframes_only": "1",
            "stop_objects": "FACE_F"
            }
        } #JSON код с параметрами обработки видео

response = requests.post(urlQueue, headers=headers, json=jsonCode) #POST запрос для постановки видео в очередь на обработку
print(response.json()) #Вывод ответа POST апроса на постановку видео в очередь на обработку

data = json.loads(response.text) #Преобразование JSON кода в словарь для получения id
idQueue = str(data['id'])
print(idQueue)

urlStatus = 'https://api.gcdn.co/vp/api/tasks/' + idQueue + '.json' #ссылка для получения статуса обработки видео

response2 = requests.get(urlStatus, headers=headers) #GET запрос для полученя статуса обработки видео
data = json.loads(response2.text) #Преобразование JSON кода в словарь для получения статуса обработки видео
status = data['status']

while status == 'new' or status == 'processing' or status == 'starting': #цикл ожидания окончания обработки видео посылающий GET звпрос пока обработка не закончится
    response2 = requests.get(urlStatus, headers=headers) #GET запрос для полученя статуса обработки видео
    print(status) #вывод статуса обработки видео на данный момент
    data = json.loads(response2.text)
    print(response2.json()) #вывод результата обработки видео
    status = data['status'] #изменение переменной содержащей статус на текущий статус
    print(status) #вывод статусаа в консоль

print(response2.json()) #вывод результата обработки видео

