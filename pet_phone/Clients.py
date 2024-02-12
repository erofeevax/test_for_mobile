from Client import Client


class Clients:

    def __init__(self, ioStrategy,dbStrategy):
        self.clientsList = list()
        self.io = ioStrategy
        self.db = dbStrategy
        self.data = "clients.data"
        self.maxId = 0

    def add(self, client):
        self.clientsList.append(client)
        self.io.output("Successful operation.\n")
    
    def createClient(self):
        c = Client(self.io, self.maxId)
        self.add(c)
        self.maxId += 1

    def showClients(self):
        for i, item in enumerate(self.clientsList):
            self.io.output(f"----------\nClient №:{i}")
            item.show()

    def editClient(self):
        clientId = int(self.io.input("Choose client's id: "))
        for i in self.clientsList:
            if i.id == clientId:
                i.edit()
                break

    def dump(self):
        self.db.dump(self.data, self.clientsList)

    def load(self):
        self.clientsList = self.db.load(self.data)

    def clear(self):
        self.clientsList.clear()
