import datetime
import platform
import os

from subprocess import Popen, PIPE

mysqld = "[mysqld]"
client = "[client]"
mysql = "[mysql]"
server_charset = "character-set-server=utf8"
client_charset = "default-character-set=utf8"


def print_message(msg):
    time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print('[%s]:%s' % (time, msg))


def backup_file(file_object, data):
    print_message('back up your file to %s.bak_bak...' % file_object)
    f = open(file_object.name + '.bak_bak', 'w')
    name = f.name
    f.writelines(data)
    f.flush()
    f.close()
    print_message('back up your file success,you can open find it : %s' % name)


def find_mysqld(file_object, data):
    if data.find(mysqld) < 0:
        backup_file(file_object, data)
        print_message("prepare write into file...")
        file_object.write(data)
        file_object.write('\n')
        file_object.write(mysqld)
        file_object.write('\n')
        file_object.writelines(server_charset)
        file_object.flush()
        print_message("write file success...")
    elif data.find(server_charset) < 0:
        backup_file(file_object, data)
        print_message("prepare write into file...")
        file_object.seek(0, 0)
        str = data.replace(mysqld, mysqld + '\n' + server_charset)
        file_object.writelines(str)
        file_object.flush()
        print_message("write file success...")
    else:
        print_message("you have already write server_char_set...")


def correct():
    f = open('/etc/mysql/mysql.conf.d/mysqld.cnf', 'r+')
    try:
        all_text = f.read()
        find_mysqld(f, all_text)
    finally:
        f.close()


def show_mysql_info():
    print_message(Popen("which mysql", stdout=PIPE, shell=True).stdout.read())


def judge_platform():
    sys = platform.uname().system.lower()
    if sys.find("ubuntu") < 0:
        show_mysql_info()
        print_message('Your system is %s,current not support!!!' % sys)
    else:
        print_message('Your system is %s ,supported!!!' % sys)
        correct()


judge_platform()
