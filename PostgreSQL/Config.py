from configparser import ConfigParser
import os

def config(ruta="PostgreSQL", filename='database.ini', section='postgresql'):
    
    filename = os.path.join(ruta, filename)
    if not os.path.isfile(filename):
        print(os.getcwd())
        raise Exception('File {0} not found'.format(filename))

    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db
