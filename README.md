
# 解决ubuntu下mysql中文乱码的问题
现在支持大部分linux设备，ubuntu/centos/osx均测试通过

有问题可以直接联系我

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
在osx和CentOS中会查询/etc/my.cnf文件，文件不存在则会自动创建，
文件存在则会先备份原有的文件为/etc/my.cnf.bak_bak,然后自动在原文件中写入数据

Ubunt则会自动查询`/etc/mysql/mysql.conf.d/mysqld.cnf`,先备份次文件，然后写入数据
3. 然后写入文件中
```shell
Ubunut: sudo service mysql restart
CentOS: sudo service mysqld restart
```
macos下可以自己重启mysql