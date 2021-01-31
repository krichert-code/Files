import sqlite3
from collections import namedtuple
UserStruct = namedtuple("UserStruct", "name email id bankAccounts delete new modified")

class User(object):
    def __init__(self, name, email, id):
        self.name = name
        self.email = email
        self.id = id
        self.bankAccounts = []
        self.delete = False
        self.new = False
        self.modified = False

class Users(object):

    def __getUserData(self):
        self.users = []
        conn = sqlite3.connect('file.db')
        c = conn.cursor()
        r = conn.cursor()
        for row in c.execute('SELECT * FROM users'):
            obj = User(row[2], row[1], row[0])
            for bankAccountRow in r.execute('SELECT number FROM accounts WHERE userId=?', (row[0],)):
                obj.bankAccounts.append(bankAccountRow[0])
            self.users.append(obj)
        conn.close()

    def addBankAccount(self, userId, bankAccount=""):
        for item in self.users:
            if (userId == item.id):
                item.modified = True
                item.bankAccounts.append(bankAccount)
                break

    def delBankAccount(self, userId, accountId):
        for item in self.users:
            if userId == item.id:
                item.modified = True
                item.bankAccounts.pop(accountId)
                break

    def updateUserData(self, userId, name, email):
        for item in self.users:
            if item.id == userId:
                item.modified = True
                item.name = name
                item.email = email
                break

    def updateUserBankAccount(self, userId, bankAccountId, number):
        for item in self.users:
            if item.id == userId:
                item.modified = True
                item.bankAccounts[bankAccountId] = number
                break

    def addNewUser(self, name="", email=""):
        obj = User(name, email, self.__newUserId)
        currentUserId = self.__newUserId
        obj.new = True
        self.__newUserId = self.__newUserId - 1
        self.users.insert(0, obj)
        return currentUserId

    def delUser(self, id):
        removeObjectFromList = False
        for item in self.users:
            obj = item
            if (item.id == id):
                obj = item
                if item.new:
                    removeObjectFromList = True
                item.delete = True
                break
        if removeObjectFromList:
            self.users.remove(obj)

    def getUsersCount(self):
        return len(self.users)

    def storeUsedData(self, progressBar):
        conn = sqlite3.connect('file.db')
        c = conn.cursor()
        progressBar.initialize(len(self.users))

        for item in self.users:
            progressBar.makeStep()
            if item.new:
                params = (item.email, item.name, )
                c.execute("INSERT INTO users (email, name) VALUES (?, ?)", params)
                userId = c.lastrowid
                for account in item.bankAccounts:
                    params = (account, userId,)
                    c.execute("INSERT INTO accounts (number, userId) VALUES (?, ?)", params)
                # Save (commit) the changes
                conn.commit()
                continue

            if item.delete:
                params = (item.id, )
                c.execute("DELETE FROM users WHERE userId = ?", params)
                c.execute("DELETE FROM accounts WHERE userId = ?", params)
                c.execute("DELETE FROM transactions WHERE userId = ?", params)
                # Save (commit) the changes
                conn.commit()
                continue

            if item.modified:
                params = (item.name, item.email, item.id,)
                paramDelete = (item.id,)
                c.execute("UPDATE users SET name = ?, email = ? WHERE userId = ?", params)
                c.execute("DELETE FROM accounts WHERE userId = ?", paramDelete)
                for number in item.bankAccounts:
                    paramsInsert = (number, item.id,)
                    c.execute("INSERT INTO accounts (number, userId) VALUES (?, ?)", paramsInsert)
                # Save (commit) the changes
                conn.commit()
                continue

        conn.close()

    def __prepareAccountNumber(self, number, charactersToRemove):
        for character in charactersToRemove:
            number = number.replace(character, '')
        return number

    def findUserIdByAccount(self, accountNumber):
        found = False
        userId = -1
        for user in self.users:
            for number in user.bankAccounts:
                if self.__prepareAccountNumber(number,['-', ' ']) == accountNumber:
                    found = True
                    userId = user.id
                    return found, userId
        return found, userId

    def __iter__(self):
        self.idx = 0
        return self

    def __next__(self):
        if self.idx < len(self.users):
            obj = self.users[self.idx]
            self.idx = self.idx + 1
            return obj
        raise StopIteration

    def __init__(self):
        self.__newUserId = -1
        self.__getUserData()
