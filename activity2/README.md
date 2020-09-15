# CMPSC 201: Class Activity 2

## Introduction

This class activity invites individuals to explore the use of SLY for scanning and parsing.


## Docker 

Once you have Docker Desktop running on your machine, you can use Docker to run the given
Python program. These commands should be run from the `src` directory,
one level up from the directory containing the source code. 

### Building

To build a Docker image, run the following command:

`docker build -t sly .`

### Running

To run a program in a docker container, run the following command, where `example.py` 
is the name of the program.

*Mac/Linux:*

`docker run --rm -v $(pwd)/src:/root sly python3 example.py`

*Windows:*

`docker run --rm -v "%cd%/src":/root sly python3 example.py`


### Submission

Commit the modified `example.py` file to your class activities repository.