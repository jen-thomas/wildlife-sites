#!/bin/bash

docker-compose --project-name wildlife_sites -f docker-compose.yml down
docker-compose --project-name wildlife_sites -f docker-compose.yml up
