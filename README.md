template project with
- docker
- pyhton
- django
- django restframework
- mariadb

mariadb en entornos linux
instalar pkg config 
$ sudo apt-get install python3-dev default-libmysqlclient-dev build-essential pkg-config  (ubuntu)
setear variables de entorno
$ export MYSQLCLIENT_CFLAGS=`pkg-config mysqlclient --cflags`
$ export MYSQLCLIENT_LDFLAGS=`pkg-config mysqlclient --libs`



