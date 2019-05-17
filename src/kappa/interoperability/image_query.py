from datetime import datetime
import dateparser
from enum import Enum
import re
from typing import *

class ImageQueryField(Enum):
    NAME = 0
    DATE = 1
    TAGS = 2


class ImageQueryOperator(Enum):
    EQUALS = 0
    GREATER_THAN = 1
    LOWER_THAN = 2
    BETWEEN = 3
    CONTAINS = 0


class ImageGrouping(Enum):
    DATE = 0
    TAG = 1


class ImageQueryCondition:
    def __init__(self, field: ImageQueryField, operator: ImageQueryOperator, operand1: str, operand2: str):
        if field is not ImageQueryField.DATE and operator is not ImageQueryOperator.CONTAINS:
            raise ImageQueryError(-1)
        if not operand1.strip() or (field is ImageQueryField.DATE and ImageQuery.parseDate(operand1) is None):
            raise ImageQueryError(0)
        if operator is ImageQueryOperator.BETWEEN and (not operand2.strip() or ImageQuery.parseDate(operand2) is None):
            raise ImageQueryError(1)

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
        self.__conditions = []
        self.__imageGrouping = None

    def getConditions(self) -> List[ImageQueryCondition]:
        return self.__conditions

    def addCondition(self, condition: ImageQueryCondition):
        self.__conditions.append(condition)

    def clearConditions(self):
        self.__conditions.clear()

    def getImageGrouping(self) -> ImageGrouping:
        return self.__imageGrouping

    def setImageGrouping(self, imageGrouping: ImageGrouping):
        self.__imageGrouping = imageGrouping

    def toImageQueryLanguage(self) -> str:
        conditionStrings = []
        errorOperandIndices = []

        for i in range(len(self.__conditions)):
            c = self.__conditions[i]
            conditionString = c.getField().name.lower() + ' '

            if c.getOperator() is ImageQueryOperator.GREATER_THAN:
                conditionString += '> '
            elif c.getOperator() is ImageQueryOperator.LOWER_THAN:
                conditionString += '< '

            conditionString += c.getOperand1()

            if c.getOperator() is ImageQueryOperator.BETWEEN:
                conditionString += ' - ' + c.getOperand2()

            conditionStrings.append(conditionString)

        if errorOperandIndices:
            raise ImageQueryError(errorOperandIndices)
        return ', '.join(conditionStrings)

    def fromImageQueryLanguage(imageQueryString: str) -> 'ImageQuery':
        imageQuery = ImageQuery()

        if not imageQueryString:
            return imageQuery

        for conditionString in imageQueryString.split(','):
            conditionString = re.sub(' +', ' ', conditionString).strip()

            fieldStr, operatorChar, operand1, operand2 = None, None, None, None
            buffer = ''
            expectOperator = 0

            for i in range(len(conditionString)):
                c = conditionString[i]
                writeToBuffer = True
                expectOperator -= 1

                if c == ' ':
                    if fieldStr is None:
                        fieldStr = buffer
                        buffer = ''
                        expectOperator = 2
                elif c == '<' or c == '>':
                    if fieldStr is None or expectOperator > 0:
                        if fieldStr is None:
                            fieldStr = buffer
                        operatorChar = c
                        buffer = ''
                elif c == '-' and operatorChar is None:
                    operatorChar = '-'
                    operand1 = buffer.strip()
                    buffer =  ''
                else:
                    buffer += c

            if not fieldStr:
                raise ImageQueryError()

            if operand1 is None:
                operand1 = buffer.strip()
                operand2 = ''
            else:
                operand2 = buffer.strip()

            if fieldStr.upper() == 'NOM':
                field = ImageQueryField.NAME
            elif fieldStr.upper() == 'DATE':
                field = ImageQueryField.DATE
            elif fieldStr.upper() == 'TAGS':
                field = ImageQueryField.NAME
            else:
                raise ImageQueryError()

            if operatorChar == '<':
                operator = ImageQueryOperator.LOWER_THAN
            elif operatorChar == '>':
                operator = ImageQueryOperator.GREATER_THAN
            elif operatorChar == '-':
                operator = ImageQueryOperator.BETWEEN
            else:
                if field is ImageQueryField.DATE:
                    operator = ImageQueryOperator.EQUALS
                else:
                    operator = ImageQueryOperator.CONTAINS

            imageQuery.addCondition(ImageQueryCondition(field, operator, operand1, operand2))

        return imageQuery


    def toSQL(self) -> str:
        query = 'SELECT * FROM IMAGE WHERE '

        for condition in self.__conditions:
            pass

    def parseDate(date: str) -> datetime:
        return dateparser.parse(date, languages=['fr'])


class ImageQueryError(ValueError):
    def __init___(self, operandIndex: int = -1):
        super().__init__(self)

        self.__operandIndex = operandIndex

    def getOperandIndex(self) -> int:
        return self.operandIndex
