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
    items = ["a", "b", "c", "d", "e", "f"]
    result = Any.subsetOf(min=1, max=4, items=items)
    print(result) # ['d', 'e', 'b']
