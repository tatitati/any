from datetime import datetime
import random

from main import Any


def test_positiveNumber():
    def createData():
        return {
            "age": Any.positiveNumber(),
            "name": Any.word()
        }


    result = Any.listOf(
        min=3,
        max=7,
        factoryFunction=createData
    )
    print(result)
    # [
    #     {'age': 7323, 'name': 'vecalmzbdcvdwuqk'},
    #     {'age': 9705, 'name': 'bdqqpgtpgbfbci'},
    #     {'age': 9656, 'name': 'ojizqxl'}
    # ]


def test_subsetOf():
    result = Any.subsetOf(min=1, max=4, items=["a", "b", "c", "d", "e", "f"])
    print(result) # ['d', 'e', 'b']

def test_dateTimeBefore():
    result = Any.dateTimeBefore(datetime(2015, 12, 25, 10, 30, 45))
    print(result) # 1994-10-22 10:30:45