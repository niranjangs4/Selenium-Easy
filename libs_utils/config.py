import configparser


def readconfig(title, key):
    config = configparser.ConfigParser()
    config.read(r'H:\seleniumeasy\Config.cfg')
    return config.get(title, key)


if __name__ == "__main__":
    print(readconfig('WEB', 'Browser'))
