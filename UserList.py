import os,pickle
class UserList:
    fileName="userlist.txt"

    def __init__(self):
        self.load()

    def load(self):
        if not os.path.exists(self.fileName):
            with open(self.fileName,'wb') as f:
                pickle.dump(dict(),f)
        with open(self.fileName, 'rb') as f:
            self.users=pickle.load(f)

    def commit(self):
        with open(self.fileName, 'wb') as f:
            pickle.dump(self.users, f)

    def addUser(self,name,passwd):
        if self.users.get(name):
            return False
        self.users[name]=passwd
        self.commit()
        return True

    def checkUser(self,name,passwd):
        return self.users.get(name)==passwd