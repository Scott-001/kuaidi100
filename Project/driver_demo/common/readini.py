import configparser


def readIni(path, section, option):
    conf = configparser.ConfigParser()
    conf.read(path, encoding='utf-8')
    res = conf.get(section, option)
    return res


if __name__ == '__main__':
    print(readIni(r'../config/config.ini', 'URL', 'url'))
