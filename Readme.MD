restart docker
docker build . -t app1image
docker build . -t app2image

start dockerc-compose
sudo docker-compose up

term3
localhost/app2/api -вызов метода из 2 приложения 
localhost:5555/api/app2 - вызов метода из 2 приложения первым
