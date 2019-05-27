# Sistemaganaderia
Es un sistema basico para inscripcion de animales, tiene lo basico, guardar animal, consultas por ID, y tambien listar todos los animales registrados, utilizando flask como framework.

It is a basic system for animal registration, it has the basics, save animals, queries by ID, and also list all registered animals, using flask as a framework.

## Requirements

* Python 3.6
* Virtualenv
* Flask 1.0.2 


## Install
```bash
git clone https://github.com/WilliBobadilla/Sistemaganaderia.git

cd Sistemaganaderia

python3 -m venv env

source env/bin/activate

pip install -r requirements.txt

```
##Running the server 
###For linux 
```bash
export FLASK_APP=app.py 

```
###For Windows
```bash
set FLASK_APP=app.py

```
### Run locally on your computer
```bash

flask run

```
### Run locally on your network
```bash

flask run --host=your_computer_ip

```
