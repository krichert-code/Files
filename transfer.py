import csv
import sqlite3
from users import Users

class Record(object):
    def isValid(self):
        return not self.error

    def getTitle(self):
        return self.title

    def getValue(self):
        return self.value

    def getID(self):
        return self.operationId

    def getDate(self):
        return self.date

    def getAcountNumber(self):
        return self.accountNumber

    def getUserName(self):
        return self.userName

    def __prepareAccountNumber(self, number, charactersToRemove):
        for character in charactersToRemove:
            number = number.replace(character, '')
        return number

    def __prepareTitle(self, recordLine, start, end):
        title = ""
        idx = 0
        for text in recordLine:
            if (idx>=start and idx <=end):
                title = title + text
            idx = idx + 1
        return title


    def __init__(self, recordLine):
        try:
            self.error = False
            self.userName = recordLine[11]
            self.date = recordLine[15]
            self.value = float(recordLine[16].replace(',', '.'))
            self.operationId = recordLine[18]
            self.accountNumber = self.__prepareAccountNumber(recordLine[5], [' ', '-'])
            self.title = self.__prepareTitle(recordLine, 1,4)
        except IndexError:
            self.error = True


class Transfer(object):

    def loadFile(self, fileName):
        with open(fileName, 'r', newline='', encoding='ISO-8859-1') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    for column in row:
                        self.header.append(column)
                    line_count += 1
                else:
                    data = []
                    for column in row:
                        data.append(column)
                    record = Record(data)
                    if record.isValid():
                        self.data.append(record)
                    line_count += 1

    def storeInDB(self, progressBar):
        users = Users()
        conn = sqlite3.connect('file.db')
        c = conn.cursor()

        progressBar.initialize(len(self.data))

        for record in self.data:
            found, userId = users.findUserIdByAccount(record.getAcountNumber())

            if found:
                commit = True
                params = (record.getID(), record.getDate(), record.getValue(), record.getTitle(), userId,)
                try:
                    c.execute("INSERT INTO transactions (transactionId, day, value, title, userId) VALUES (?, ?, ?, ?, ?)",
                                params)
                except sqlite3.IntegrityError as err:
                    commit = False

                # Save (commit) the changes
                if commit:
                    conn.commit()
            progressBar.makeStep()

        conn.close()

    def __iter__(self):
        self.idx = 0
        return self

    def __next__(self):
        if self.idx < len(self.data):
            obj = self.data[self.idx]
            self.idx = self.idx + 1
            return obj
        raise StopIteration

    def __init__(self):
        self.header = []
        self.data = []

        pass
