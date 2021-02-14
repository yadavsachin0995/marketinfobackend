# marketinfobackend

## Project setup

### Compiles and hot-reloads for development
```
python manage.py runserver
```

### Instructions to run

python manage.py runserver from the root directory exposes the application on port 8000, which is used by the frontend application for API calls. Alternatively, docker image for this app can be pulled from dockerhub and can be run on the local using below command:

docker pull yadavsachin0995/dockerized-market-info-backend (images not uploaded to docker-hub as of now, will update if my system stops timing out for no valid reason)
docker run -it -p 8000:8000 --rm --name dockerized-market-info-backend dockerized-market-info-backend


Hint - To run the container in detached mode, use -d.


### What's pending?

1. Test Cases - Unit Test cases have not been written for any file or util.
2. Exception Handling could be improvised.
3. Extract globally configurable variables from components and put the in a conf file.


### Is there a demo link available?

No. Since the locally built container images were not uploaded to remote, was unable to pull those images on ECS. Planned to have one instance each for frontend, backend and redis server - exposing the frontend app through a public IP. If my VPN stops behaving irrationally, might upload the docker images and complete the hosting. 

If docker is locally installed and a good internet bandwidth is available, images for frontend and backend (refer - https://github.com/yadavsachin0995/market-info-frontend) can be built using -
a. docker build -t dockerized-market-info-backend . (from the root folder of the backend project - https://github.com/yadavsachin0995/market-info-frontend)
b. docker build -t dockerized-market-info-app . (from the root folder of this project)


Some snapshots of the running app are attached below -

Landing page with no filter on Equity Name

![alt text](/snapshots/screen1.PNG)

Filter text entered inside textbox provides real-time filtering of results

![alt text](/snapshots/screen2.PNG)

If a user clicks download button on filtered results screen, only present records are downloaded in csv

![alt text](/snapshots/screen3.PNG)

Information of containers used to run the app along with port numbers

![alt text](/snapshots/screen4.PNG)

### What about Redis?

The redis container used for this project was fetched from the official repo of Redis on dockerhub. The same can be fetched and started using following commands-

a. docker pull redis
b. docker run --rm -p 6379:6379 redis
