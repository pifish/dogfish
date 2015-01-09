#!/usr/bin/env python
#-*- encoding: utf-8 -*-
import os
import commands
import subprocess
import sys

print "Isso levará vários minutos, aguarde..."
subprocess.call("apt-get -y update", shell=True)
subprocess.call("apt-get -y install sudo", shell=True)
subprocess.call("apt-get -y install python", shell=True)
subprocess.call("apt-get -y install python-dev", shell=True)
subprocess.call("apt-get -y install python-rpi.gpio", shell=True)
subprocess.call("apt-get -y install git-core", shell=True)
subprocess.call("apt-get -y install apache2 php5 libapache2-mod-php5", shell=True)
subprocess.call("git clone git://git.drogon.net/wiringPi", shell=True)
subprocess.call("git clone git://github.com/pifish/dogfish", shell=True)

c=commands.getoutput("pwd")

moveWeb="mv "+str(c)+"/dogfish/Web/ /var/www/web"
subprocess.call(moveWeb, shell=True)

subprocess.call("apt-get -y install make", shell=True)
subprocess.call("apt-get -y install python-setuptools", shell=True)
subprocess.call("easy_install -U distribute", shell=True)
subprocess.call("apt-get -y install python-pip", shell=True)
subprocess.call("pip install rpi.gpio", shell=True)

caminho=str(c)+"/wiringPi/"
os.chdir(caminho)
print "Atualizando wiringPi"
subprocess.call("git pull origin", shell=True)
print "Construindo wiringPi"
subprocess.call("sudo ./build", shell=True)

subprocess.call("gpio -v", shell=True)
subprocess.call("gpio readall", shell=True)
print "Pronto para usar acesse http://ipDaSuaRaspberry/web/"
