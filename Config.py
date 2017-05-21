import os
import pickle


class Config:
    fileName = "config.txt"
    data = {}

    def __init__(self):
        self.load()

    def load(self):
        if not os.path.exists(self.fileName):
            with open(self.fileName, 'wb') as f:
                newData = {}
                newData["threadNum"] = 4
                newData["direction"] = 0
                newData["depth"] = 3
                newData["width"] = 20
                newData["number"] = 200
                newData["time"] = 300
                newData["Id"]=True
                newData["name"]=True
                newData["verified"]=True
                newData["description"]=True
                newData["gender"]=True
                newData["fans"]=True
                newData["follow"]=True
                pickle.dump(newData, f)
        with open(self.fileName, 'rb') as f:
            self.data = pickle.load(f)

    def commit(self):
        with open(self.fileName, 'wb') as f:
            pickle.dump(self.data, f)

    def setConfig(self, newData):
        self.data = newData;
        self.commit()

    def getConfig(self):
        return self.data;

    def addUser(self, name, passwd):
        if self.users.get(name):
            return False
        self.users[name] = passwd
        self.commit()
        return True

    def checkUser(self, name, passwd):
        return self.users.get(name) == passwd
