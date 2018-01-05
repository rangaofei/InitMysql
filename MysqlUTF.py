

mysqld = "[mysqld]"
client = "[client]"
mysql = "[mysql]"
server_charset = "character-set-server=utf8"
client_charset = "default-character-set=utf8"


def findMysqld(file_object, data):
    if data.find(mysqld) < 0:
        file_object.write('\n')
        file_object.write(mysqld)
        file_object.write('\n')
        file_object.writelines(server_charset)
    else:
        print("you have already write server_char_set")


def correct():
    file_object = open('/etc/mysql/mysql.conf.d/mysqld.cnf', 'r+')
    try:
        all_text = file_object.read()
        findMysqld(file_object, all_text)
    finally:
        file_object.close()


correct()
