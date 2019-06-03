# docker-compose-flask-postgres
Python application with Flask, Postgresql and Redis building in docker-compose.

# Start using
1. First, build the base images for services: web and database. It helps you to save much time in the future.

`docker build -t flask:latest .` \
`docker build -t postgres:base .`

You can choose any another names for your images, but be sure that you put them in docker-compose.yml 

2. Create external volume for postgres

`docker volume create db_data`

or other name you want, just change it in docker-compose.yml

3. Launch service

`docker-compose up --build -d`

3. Stop service

`docker-compose down --volume`

4. Remove external volume

`docker volume rm db_data`

# Request
For example from powershell with curl:
`curl
-X POST
-H 'Content-Type:application/json'
-d '{\"client_id"\: \"1\", \"date"\: \"2018-12-03 16:58:02\", \"amount"\: \"26000\", \"currency"\: \"USD\", \"country"\: \"USA\"}'
http://localhost:5000/validate`
