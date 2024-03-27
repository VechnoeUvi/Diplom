import configuration
import requests
import data

#создание заказа
def get_new_order_track():
    return requests.post(configuration.SERVICE_URL + configuration.NEW_ORDER, json=data.ord_body, headers=data.header).json()["track"]

def find_ord(track):
    return requests.get(configuration.SERVICE_URL + configuration.ORDER_TRACK + str(track))