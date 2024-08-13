class Utils:
    @staticmethod
    def enumerated(array):
        print(len(array))
        list_enumerated = []
        for index in range(len(array) - 1):
            list_enumerated.append((index, array[index]))
        return list_enumerated
