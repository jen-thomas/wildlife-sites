#!/bin/bash -x

if [ "$1" = "" ]
then
        echo "Please provide file to restore backup from" >&2
	exit
fi

SQL_FILE="$1"

docker exec -it wildlife_sites_mysql_1 mysql -u wildlife_user -h 127.0.0.1 -pwildlife_sites_password -e "drop database wildlife_sites_db;"

cat "$SQL_FILE" | docker exec -i wildlife_sites_mysql_1 mysql -u wildlife_user -h 127.0.0.1 -pwildlife_sites_password
