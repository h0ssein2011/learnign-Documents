#!/bin/bash
curl http://api.citybik.es/v2/networks/citi-bike-nyc > city_bike.json

jq -r '.network.stations[] | [.name,  .last_updated ] | @csv' city_bike.json > city_bike.csv
rm city_bike.json
 