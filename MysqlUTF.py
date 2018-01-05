mysqld = "[mysqld]"
client = "[client]"
mysql = "[mysql]"
server_charset = "character-set-server=utf8"
client_charset = "default-character-set=utf8"


def backup_file(file_object, data):
    print('back up your file to %s.bak_bak...' % file_object)
    f = open(file_object.name + '.bak_bak', 'w')
    name = f.name
    f.writelines(data)
    f.flush()
    f.close()
    print('back up your file success,you can open find it : %s' % name)


def findMysqld(file_object, data):
    if data.find(mysqld) < 0:
        backup_file(file_object, data)
        print("prepare write into file...")
        file_object.write(data)
        file_object.write('\n')
        file_object.write(mysqld)
        file_object.write('\n')
        file_object.writelines(server_charset)
        file_object.flush()
        print("write file success...")
    elif data.find(server_charset) < 0:
        backup_file(file_object,data)
        print("prepare write into file...")
        file_object.seek(0,0)
        str = data.replace(mysqld, mysqld + '\n' + server_charset)
        file_object.writelines(str)
        file_object.flush()
        print("write file success...")
    else:
        print("you have already write server_char_set...")


def correct():
    f = open('/etc/mysql/mysql.conf.d/mysqld.cnf', 'r+')
    try:
        all_text = f.read()
        findMysqld(f, all_text)
    finally:
        f.close()


correct()
