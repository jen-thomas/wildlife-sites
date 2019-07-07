#!/bin/bash

if [ "$1" = "" ]
then
        echo "Please provide directory to save the backup" >&2
	exit
fi

DESTINATION_FILE="$1/wildlife-sites-$(date +%Y%m%d-%H%M%S).sql"

docker exec -i wildlife_sites_mysql_1 sh -c 'mysqldump --databases wildlife_sites_db -u wildlife_user -h 127.0.0.1 -pwildlife_sites_password' > "$DESTINATION_FILE"

echo "Backup done: $DESTINATION_FILE"
