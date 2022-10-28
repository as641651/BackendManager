# BackendManager
Manage processes executions and synchronise data between cluster and a local node. 

In order to run the code, use one of the following methods:

## 1) Manual Installation

### Requirements:

1. numpy
2. pandas
2. matplotlib


Clone this directory and execute the following command inside the directory

```bash
pip install .
```

## 2) Use Docker

### Requirements:

1. Docker

Clone this directory and execute the following command inside the directory

Build image:

```bash
docker build -t [IMAGE_NAME] .
```
Map the ports for jupyter notebook and the current working directory to the container, and Run the image

Linux version
```bash
 docker run -it -p [port of container]:[port of the notebook] -v ${1:-$PWD}:/home/user [image_name:version]
```
Windows version 
```bash
 docker run -it -p 0.0.0.0:[port of container]:[port of notebook] -v [the directory where image files are stored]:/home/user [image_name:version]
```
example:

 port of container = 8005 , port of notebook = 8888 , image directory = /c/Users/Projects/BackendManager, image name = manager

```bash
docker run -it -p 0.0.0.0:8005:8888 -v /c/Users/Projects/BackendManager:/home/user manager
```


Run Jupyter notebook inside the container. 
```bash
jupyter notebook --ip 0.0.0.0 --no-browser --allow-root
```
for windows OS write the following command in the browser: localhost:[port of container]

incase the above line did not work in windows then write the following command in the browser: [ip of the machine]:[port of container]

The IP of your machine is printed when opening Docker toolbox Quickstart command line(in case of using docker toolbox).

## Usage

Refer the ```.ipynb``` files [here](/examples/simulated)
