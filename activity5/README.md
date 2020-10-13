# CMPSC 201 Activity 5

## Updating `progator` Docker image

First, please pull the newest [progator](https://hub.docker.com/repository/docker/janyljumadinova/progator) image by running the following command:

`docker pull janyljumadinova/progator`

You can check that you have the `progator` image by running the following command and verifying that you see `progator` in the list of your Docker images:

`docker image list`

Then, run the docker container and mount your "activity5" directory as a volume by replacing `your-path/local/working/directory` in the following command with the path to your "activity5" directory:

`docker run -d -p 80:80 -v /your-path/local/working/directory/:/root/environment janyljumadinova/progator`

You can check that you have correctly started the Docker container:

`docker container list`

## Running COBOL programs

Now open your [localhost](http://localhost) to access Ubuntu 20.04 running with VSCode, navigate to the `root` directory, open the terminal, and navigate to the `environment` directory. Here you should see `example.cbl` program.

To compile this COBOL program, run the following command:

`cobc -x -free -o example example.cbl`

Then, to run it, you can run the following command:

`./example`

## Stopping the `progator` container

When you are finished working with `progator` do not forget to stop `progator` container by getting the container ID from the command you ran in your terminal:

`docker container list`

and then stopping the container by running the following command (replacing `container-ID` with the actual `progator` container ID in your terminal:

`docker container stop container-ID`

 
