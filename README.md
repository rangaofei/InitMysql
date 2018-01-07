
# 解决ubuntu下mysql中文乱码的问题
1. 使用wget或者curl均可
```
wget https://raw.githubusercontent.com/rgf456/InitMysql/master/MysqlUTF.py
```
2. 下载完成后执行
```shell
sudo python3 MysqlUTF.py
```
程序首先判断是否是ubuntu系统，假如不是则输出
```
Your system is $your sys$,current not support!!!
```
程序运行时会提示先将你的原`path/to/mysqld.conf`备份为`path/to/mysqld.conf.bak.bak`

3. 然后写入文件中
```shell
debian:sudo service mysql restart
centOS:sudo service mysqld restart
```
