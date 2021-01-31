import sqlite3
from users import Users
from datetime import datetime, timedelta
from dateutil.relativedelta import *


class Payments(object):

    def __createEmptyPaymentsArray(self, monthCount):
        data = []
        for i in range(monthCount, -1, -1):
            data.append(0)
        return data

    def __setValue(self, array, value, paymentDate):
        idx = 0
        for date in self.__headers:
            if date == paymentDate:
                array[idx] = value
                break
            idx = idx + 1

    def getPaymentsMonths(self):
        return self.__headers

    def getPamentsByUserAndDate(self, userId, date):
        result = []
        conn = sqlite3.connect('file.db')
        c = conn.cursor()
        param = (userId, date,)
        for row in c.execute("SELECT title, value FROM transactions WHERE userId = ? AND strftime('%m-%Y', "
                             "transactions.day ) = ?", param):
            result.append((row[0], row[1]))

        c.close()
        return result

    def getPaymentsForLastMonths(self, monthCount):
        records = {}

        for i in range(monthCount, -1, -1):
            self.__headers.append((datetime.today() + relativedelta(months=-i)).strftime("%m-%Y"))

        conn = sqlite3.connect('file.db')
        c = conn.cursor()

        param = ((datetime.today() + relativedelta(months=-monthCount)).strftime("%Y-%m-01"),)
        LastUserId = -1
        for row in c.execute("SELECT users.userId, users.name, SUM(transactions.value), strftime('%m-%Y', "
                             "transactions.day ) as 'month-year'  FROM users, transactions WHERE (users.userId = "
                             "transactions.userId AND transactions.day >= ?)  GROUP BY users.userId, "
                             "strftime('%m-%Y', transactions.day ) ORDER BY users.name", param):
            if LastUserId != row[0]:
                item = self.__createEmptyPaymentsArray(monthCount)
                records[(row[0], row[1])] = item
                LastUserId = row[0]

            self.__setValue(item, row[2], row[3])

        c.close()
        for user in self.__users:
            if (user.id, user.name) not in records:
                item = self.__createEmptyPaymentsArray(monthCount)
                records[(user.id, user.name)] = item

        return records

    def __init__(self):
        self.__headers = []
        self.__users = Users()


