# 🧟‍♀️💻 Happy-Zombie-Hen 🐔

Hi, this is Karen again! Today, we're diving into an educational example on zombie computers—with a twist! We’re making a videogame, but this game also includes a client-server connection setup. This will be a playful introduction to how connections work in a controlled environment. Let’s dive in! 🚀

## What's Inside the Repo?
This repository has two main components:

-  setup.py — Our Happy Hen videogame! 🎮🐔
  
- controlador.py — A server socket to manage connections. 🖥️🔗

  
## 📋 Main Objective
The main goal is to create an .exe using Pygame so that our game can run as a standalone application. To do this, we’ll use cx_Freeze to turn our game into an executable file.

## Getting Started

Set Up the IP Address:


Before you begin, you’ll need to modify the IP address in the code. Make sure to enter the IP of the computer you want to use as the server in both the game (setup.py) and the server (controlador.py) files.

Install cx_Freeze:

This tool is what allows us to create an .exe file for our Pygame project.

```bash
pip install cx_Freeze
```
Build an example on cmd: 

```bash
python setup.py build
```
On Server device run (controlador.py) : 

```bash
python controlador.py 
```

🎉 Running the Game on client device 

After setting up, you can compile and run the game! It's a fun way to explore basic client-server interactions while watching a happy hen survive a zombie apocalypse! 🐔🧟‍♂️]

## EXAMPLES

## SETUP.EXE 

![image](https://github.com/user-attachments/assets/ea9f3290-b48f-4061-af3c-09c210387c06)

## CONTROLADOR.PY 

![image](https://github.com/user-attachments/assets/e9697808-e153-4d98-ac0f-d56b2d1a1b1b)


