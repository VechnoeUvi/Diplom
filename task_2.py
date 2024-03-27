#Семашко Владимир, 14 когорта, финальный проект, инженер по тестированию плюс
import requests

SERVICE_URL = "https://3190a209-cf3d-4fef-a15f-381f2b774c47.serverhub.praktikum-services.ru"

NEW_ORDER = "/api/v1/orders"
ORDER_TRACK = "/api/v1/orders/track?t="

header = {
    "Content-Type": "application/json"
}

ord_body = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": [
        "BLACK"
    ]
}
#создание заказа
def get_new_order_track():
    return requests.post(SERVICE_URL + NEW_ORDER, json=ord_body, headers=header).json()["track"]

def find_ord(track):
    return requests.get(SERVICE_URL + ORDER_TRACK + str(track))

def test_find_order_by_track_success():
    track = get_new_order_track()
    responce = find_ord(track)

    if responce.status_code == 200:
        print("status code - 200")

#Семашко Владимир, 14 когорта, финальный проект, инженер по тестированию плюс