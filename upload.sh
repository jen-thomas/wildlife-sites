#!/bin/bash

curl -s http://localhost:8000/species/list/ | ssh $USER@pina.cat "cat > /var/www/carles.pina.cat/wildlife/index.html"
