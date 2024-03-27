import sender_stand_request

def test_find_order_by_track_success():
    track = sender_stand_request.get_new_order_track()
    responce = sender_stand_request.find_ord(track)

    assert responce.status_code == 200

#Семашко Владимир, 14 когорта, финальный проект, инженер по тестированию плюс