from Menu import Menu
from Clients import Clients
from IOStrategy import CliIOStrategy
from DBStrategy import fileDBStrategy


def main():
    ioStrategy = CliIOStrategy()
    dbStrategy = fileDBStrategy()
    c = Clients(ioStrategy, dbStrategy)
    m = Menu(c, ioStrategy)
    m.run()

if __name__ == '__main__':
	main()


