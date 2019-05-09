from enum import Enum
import re

class ImageQueryField(Enum):
    NAME = 1
    DATE = 2
    TAG = 3


class ImageQueryOperator(Enum):
    CONTAINS = 1
    EQUALS = 2
    GREATER_THAN = 3
    LOWER_THAN = 4
    BETWEEN = 5


class ImageGrouping(Enum):
    DATE = 1
    TAG = 2


class ImageQueryCondition:
    def __init__(self, field: ImageQueryField, operator: ImageQueryOperator, operand1: str, operand2: str):
        self.__field = field
        self.__operator = operator
        self.__operand1 = operand1
        self.__operand2 = operand2

    def getField(self) -> ImageQueryField:
        return self.__field

    def getOperator(self) -> ImageQueryOperator:
        return self.__operator

    def getOperand1(self) -> str:
        return self.__operand1

    def getOperand2(self) -> str:
        return self.__operand2


class ImageQuery:
    def __init__(self):
        self.__conditions = None
        self.__imageGrouping = None

    def getConditions(self) -> List[ImageQueryCondition]:
        return self.__conditions

    def setConditions(self, conditions: List[ImageQueryCondition]):
        self.__conditions = conditions

    def getImageGrouping(self) -> ImageGrouping:
        return self.__imageGrouping

    def setImageGrouping(self, imageGrouping: ImageGrouping):
        self.__imageGrouping = imageGrouping

    def toImageQueryLanguage(self) -> str:
        query = ''

        for i in range(len(__conditions)):
            c = __conditions[i]

            query += c.getField().name + ' '

            if c.getOperator() == ImageQueryOperator.GREATER_THAN:
                query += '> '
            elif c.getOperator() == ImageQueryOperator.LOWER:
                query += '< '

            query += c.getOperand1()

            if c.getOperator() == ImageQueryOperator.BETWEEN:
                query += ' - ' + c.getOperand2()

            if i != len(__conditions):
                query += ', '

        return query

    def fromImageQueryLanguage(imageQueryString: str) -> ImageQuery:
        for conditionString in imageQueryString.split(','):
            conditionTokens = strip(re.sub(' +', ' ', conditionString)).split(' ')
            for i in range(len(conditionTokens)):
                t = conditionTokens[i]


    def toSQL(self) -> str:
        query = 'SELECT * FROM IMAGE WHERE '

        for condition in self.__conditions:
            pass
