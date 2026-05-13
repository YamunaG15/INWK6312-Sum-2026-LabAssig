# INWK6312 Linux Lab

This repository contains the Docker files necessary to start an Ubuntu Container for the Linux Labs in the INWK6312 course


## Dependencies

This project requires the use of these tools:
* Docker / Docker Compose


## Running the Application
Run the following commands from a directory where this repository is located
### Build Image:
```shell
docker-compose -f linux-lab/docker-compose.yml build 
```
### Start services
```shell
docker-compose -f linux-lab/docker-compose.yml up -d
```
### Connect to a new terminal session
```shell
docker exec -it my-ubuntu bash
```
### Stop services
```shell
docker-compose -f linux-lab/docker-compose.yml down 
```
### Stop services and delete volumes
```shell
docker-compose -f linux-lab/docker-compose.yml down -v
```
