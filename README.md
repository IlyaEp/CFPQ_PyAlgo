[![CircleCI](https://circleci.com/gh/JetBrains-Research/CFPQ_PyAlgo/tree/master.svg?style=svg)](https://circleci.com/gh/JetBrains-Research/CFPQ_PyAlgo/tree/master)

# CFPQ_PyAlgo
The CFPQ_PyAlgo is a repository for developing, testing and benchmarking algorithms that solve Formal-Language-Constrained Path Problems, such as Context-Free Path Queries and Regular Path Queries. All algorithms are based on the [GraphBLAS](http://graphblas.org/index.php?title=Graph_BLAS_Forum) framework that allows you to represent graphs as matrices and work with them in terms of linear algebra. For convenience, all the code is written in Python using [pygraphblas](https://github.com/michelp/pygraphblas), which is Python wrapper around GraphBLAS API.

# Installation
First of all you need to clone repository with its submodules:

```bash
git clone --recurse-submodules https://github.com/simpletonDL/CFPQ_PyAlgo.git 
git submodule init
git submodule update
```
Then the easiest way to get started is to use Docker. An alternative, which is more correct, is to install everything directly.

## Using Docker
The first way to start is to use Docker:

```bash
# build docker image
docker build --tag <some_tag> .

# run docker container
docker run --rm -it -v ${PWD}:/CFPQ_PyAlgo <some_tag> bash
```
After it you can develop everything locally and run tests and benchmarks inside the container. Also you can use PyCharm and [configure an interpreter using Docker]( https://www.jetbrains.com/help/pycharm/using-docker-as-a-remote-interpreter.html).

## Direct install
The correct way is to install everything into your local python interpreter or virtual environment.

First of all you need to install [pygraphblas](https://github.com/michelp/pygraphblas) package. There is currently no pip package, so you need to install it manually. There is an [installation script for ubuntu](https://github.com/michelp/pygraphblas/blob/master/install-ubuntu.sh). If you make into troubles during installation, [this issue](https://github.com/michelp/pygraphblas/issues/61) can relieve your sufferings.

Secondly you need to install cfpq_data_devtools package and other requirements:

```bash
cd deps/CFPQ_Data
pip3 install -r requirements.txt
python3 setup.py install --user

cd ../../
pip3 install -r requirements.txt
```
To check if the installation was successful you can run simple tests
```bash
python3 -m pytest test -v -m "CI"
```
# Project structure
The global project structure is the following:

```
.
├── deps
│   └── CFPQ_Data - repository with graphs and grammars suites
├── src
│   ├── algo - directory where all algorithm implementations are locating
│   ├── grammar - directory for all grammar formats representation and its loading  
│   ├── graph - directory for all graph formats representation and its loading
│   └── utils - directory for other useful classes and methods
└── test
    ├── some_algo_tests - directory for testing some algorithm 
    ├── another_algo_tests - directory for testing another algorithm
    └── suites - directory for test data and its wrappers
```
