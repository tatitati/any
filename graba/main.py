import random
import string
from datetime import date, datetime, timedelta

class Any:

    @staticmethod
    def of(options: list):
        return random.choice(options)

    @staticmethod
    def listOf(min, max, factoryFunction):
        result = []
        amount = Any.positiveNumber(min, max)
        for i in range(0, amount):
            data = factoryFunction()
            result.append(data)

        return result

    @staticmethod
    def subsetOf(min, max, items):
        items_randomized = random.sample(items, len(items))
        if min == None:
            min=1
        if max == None or max > len(items):
            max=len(items)-1

        amount_to_get = Any.positiveNumber(min=min, max=max)
        return items_randomized[:amount_to_get]

    @staticmethod
    def positiveNumber(min: int = 0, max=9999) -> int:
        return random.randrange(min, max)

    @staticmethod
    def negativeNumber(min: int = -9999, max=0) -> int:
        return random.randrange(min, max)

    @staticmethod
    def anyNumber() -> int:
        return Any.of([Any.positiveNumber(), Any.negativeNumber()])

    @staticmethod
    def anyLetter() -> str:
        return Any.of(list(string.ascii_lowercase))

    @staticmethod
    def word(min = 1, max = 30) -> str:
        length = Any.positiveNumber(min, max)
        alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]

        return ''.join(random.choice(alphabet) for i in range(length))

    @staticmethod
    def sentence(min_words: int = 1, max_words: int = 5) -> str:
        amount_words = Any.positiveNumber(min=min_words, max=max_words)
        words=[]
        for i in range(amount_words):
            words.append(Any.word())

        return ' '.join(words)

    @staticmethod
    def bytes(min=1, max=30) -> bytes:
        word = Any.word(min, max)
        return word.encode('UTF-8')

    @staticmethod
    def url(min=1, max=4) -> str:
        length = Any.positiveNumber(min, max)
        words = []
        for i in range(length):
            words.append(Any.word())

        return "http://www/"+'.'.join(words)

    @staticmethod
    def bool() -> bool:
        return Any.of([True, False])

    @staticmethod
    def dateTimeInPast() -> datetime:
        now = datetime.now()
        return now - timedelta(days = Any.positiveNumber())

    @staticmethod
    def dateTimeInFuture() -> datetime:
        now = datetime.now()
        return now + timedelta(days=Any.positiveNumber())

    @staticmethod
    def dateTimeBefore(beforeDateTime: datetime) -> datetime:
        return beforeDateTime - timedelta(days=Any.positiveNumber())

    @staticmethod
    def dateTimeAfter(afterDateTime: datetime) -> datetime:
        return afterDateTime + timedelta(days=Any.positiveNumber())

    @staticmethod
    def dateTime() -> datetime:
        return Any.of([Any.dateTimeInPast(), Any.dateTimeInFuture()])

    @staticmethod
    def date() -> date:
        return Any.dateTime().date()