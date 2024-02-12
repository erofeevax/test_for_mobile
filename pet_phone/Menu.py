class Menu:

    def __init__(self, c, io):
        self.clients = c
        self.values = ["Create client", "Show clients", "Dump to file", "Load from file",
                       "Clear clients", "Edit client", "Exit"]
        self.actions = [self.clients.createClient, self.clients.showClients,
                        self.clients.dump, self.clients.load, self.clients.clear, self.clients.editClient]
        self.io = io

    def run(self):
        try:
            while True:
                self.io.output("*----------------------*")
                for i, item in enumerate(self.values):
                    self.io.output("{0:1}. {1}".format(i, item))
                self.io.output("*----------------------*")

                action = input()  # используем input() напрямую

                if action.isdigit():
                    action = int(action)
                    if action > len(self.actions) or action < 0:
                        self.io.output("Invalid action")
                        continue
                    if action == len(self.actions):
                        return
                    self.actions[action]()
                else:
                    self.io.output("Invalid input. Enter a number.")

        except Exception as e:
            self.io.output("Invalid input or operation: " + str(e))
            return
