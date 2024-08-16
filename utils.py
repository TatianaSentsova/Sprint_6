import random


class Utils:
    @staticmethod
    def enumerated(array):
        list_enumerated = []
        for index in range(len(array) - 1):
            list_enumerated.append((index, array[index]))
        return list_enumerated

    @staticmethod
    def generation_phone_number():
        ten_number = random.randint(0000000000, 9999999999)
        return f'+7{ten_number}'
