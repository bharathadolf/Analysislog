# Analysis log
<p align="center">
  <a href="/docs/README-en.md">English</a> •
  <a href="/docs/README-esla.md">Español (Latinoamérica)</a> •
  <a href="/docs/README-fr.md">Français</a> •
  <a href="/docs/README-iteu.md">Italiano (Italian)</a> •
  <a href="/docs/README-kokr.md">한국어 (Korean)</a> •
  <a href="/docs/README-ptbr.md">Português (Brasil)</a> •
  <a href="/docs/README-zhcn.md">简体中文 (Simplified Chinese)</a> •
  <a href="/docs/README-zhtw.md">繁體中文 (Taiwanese Mandarin)</a>
</p>


##                                                               log anlysis project is udacity based project

<h1 align="center">
  <a href="https://github.com/bharathadolf/Analysislog"><img src="http://mathalope.co.uk/wp-content/uploads/2015/04/python-udacity-672x299.png" alt="python-icon" width="300"></a>
  <br>

### Log analysis is?
       A Reporting page that prints out reports in a plain text format based on the data in the database. This reporting tool is a python program using the `psycopg2` module to connect to the database.

#### brief about project
> This project is written in python 
> using database (can be anything either software based or written format )
> major requirement is psycopg2 module
> This project is developed in windows 10 os
> using sublime text application
> compiled in gitbash

## Software requirements
* [Python](https://www.python.org/) - Interpreted Language
* [Git](https://git-scm.com/) - for compiling the programs and vagrant
* [Virtual Box](https://www.virtualbox.org/) -Running multiple operating systems simultaneously.
* [vagrant](https://www.vagrantup.com/) - Vagrant is software that is used to manage a development environment. Through the command line, you can grab any available OS
* [vagrantfile](https://https//github.com/udacity/fullstack-nanodegree-vm) - Vagrant is written in Ruby, but it can be used in projects written in other programming languages such as PHP, Python, Java, C#, and JavaScrip
* [Sublime Text](https://www.sublimetext.com/3) - Sublime Text is a proprietary cross-platform source code editor with a Python application programming interface

## Installation process
>Download and install applications in order 
>of 1)git 2)sublime text 3)virtual box and 4)vagrant
>clone the Udacity vagrantfile from the site "https://https//github.com/udacity/fullstack-nanodegree-vm"
>goto vagrant dictory and download zip file and place here
>open terminal or git
>launch the vagrant VM (vagrant up)
>run vagrant VM (vagrant ssh)
>Now change the directory into vagrant folder  like cd /vagrant

## Questions in this projects
* 1. What are the most popular three aricles of all time?
*  2. Who are the most popular article authors of all time?
* 3. On which days did more than 1% of requests lead to errors?

### Consecutive commands used in the project (git/terminal)
| commands | reasons for command|
| ------ | ------ |
| 1)vagrant up | For launching the vagrant  |
| 2)vagrant ssh | for running vagrant VM |
| 3)cd /vagrant | changing the directory to vagrant |
| 4) ll | for checking the sub folders/files in the directory |
| 5) cd "directory name" | cd is used to change the directory  |
| 6) psql -d news -f newsdata.sql| command for Loading the data in local database |
| 7) python "Analysis".py | For running the python projects |