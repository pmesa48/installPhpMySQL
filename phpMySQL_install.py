'''
Created on Feb 16, 2014

LAB 3 INFRACOM 2014-I
Santiago Felipe Arteaga Martin ISIS/IMEC 200411086
Pablo Santiago Mesa Triviao ISIS 201023617
Richard Alejandro Becerra Espinosa ISIS/MATE 201012278

'''


'''
COMANDOS ORIGINALES:

#!/bin/bash
# Install PHP and MySQL
pass="labredesML340"
echo "Installing missing libraries"
echo mysql-server-5.5 mysql-server/root_password password $pass | sudo debconf-set-selections
echo mysql-server-5.5 mysql-server/root_password_again password $pass | sudo debconf-set-selections
sleep 5
echo $pass | sudo -S apt-get update
sleep 5
echo $pass | sudo -S apt-get install apache2 mysql-server php5 -y
sleep 5
echo "creating downloads directory"
mkdir Downloads
echo "fetching phpscheduleit"

wget http://sourceforge.net/projects/phpscheduleit/files/latest/download?source=files -O Downloads/phpScheduleIt.zip

echo "done fetching"
echo $pass | sudo -S apt-get install zip -y
cd Downloads
echo "unziping"
unzip phpScheduleIt.zip 
echo $pass | sudo -S mv booked phpScheduleIt
cd phpScheduleIt
echo $pass | sudo -S chmod 0775 ./tpl ./tpl_c ./uploads
echo $pass | sudo -S chown www-data:www-data ./tpl ./tpl_c ./uploads
cp ./config/config.dist.php ./config/config.php
cd ..
echo "directory moved to /var/www/"
echo $pass | sudo -S mv phpScheduleIt /var/www/
echo $pass | sudo -S mv phpScheduleIt.zip .phpScheduleIt.zip
'''

'''
#IMPORTACION DE MODULOS Y LIBRERIAS NATIVAS DE PYTHON
'''
import sys
import os
import time
import subprocess

'''
IMPORTACION DE MODULOS Y LIBRERIAS PROPIAS DEL PROGRAMA
'''
###### ----- NADA!!! ----- ######

'''
VARIABLES GLOBALES DEL MODULO
'''
#NOMBRE DEL USUARIO DE LA MAQUINA VIRTUAL
USER = "labredes"

#CLAVE DEL USUARIO DE LA MAQUINA VIRTUAL
PASSWORD = "labredesML340"

#HOST REMOTO CON LAS LIBRERIAS PARA BAJAR DE PHP
REMOTEDIR = "http://sourceforge.net/projects/phpscheduleit/files/latest/download?source=files -O Downloads/phpScheduleIt.zip"

#DIRECTORIO DONDE SE BAJARA EL ARCHIVO ZIP
ROOTDIR = "/Downloads"

# NOMBRE DEL ARCHIVO ZIP A DESCOMPRIMIR
ZIPFILE = "phpScheduleIt.zip"

SLEEPTIME = 5

if __name__ == '__main__':
    
    print("PYTHON SCRIPT FOR INSTALLING PHP & MySQL")
    print("Starting...")
    
    echo = "echo "
    cd = "cd "
    wget = "wget "
    unzip = "unzip "
    cp = "cp "
    
    starting_dir = os.curdir
    
    ####################################################
    ############## starting mysql install ##############
    ####################################################
    
    mysql_info = echo + "mysql-server-5.5 mysql-server/root_password password " + PASSWORD + " | sudo debconf-set-selections"
    cmd = mysql_info
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    print(proc.communicate())
    
    mysql_info = echo + "mysql-server-5.5 mysql-server/root_password_again password " + PASSWORD + " | sudo debconf-set-selections"
    cmd = mysql_info
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    print(proc.communicate())
    
    ####################################################
    ############## finishing mysql install #############
    ####################################################

    time.sleep(SLEEPTIME)
    
    ####################################################
    ############# starting apache install ##############
    ####################################################    

    update_info = echo + PASSWORD + " | sudo -S apt-get update -y"
    cmd = update_info
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    print(proc.communicate())
    time.sleep(SLEEPTIME)
    
    update_info = echo + PASSWORD + " | sudo -S apt-get install apache2 mysql-server php5 -y"
    cmd = update_info
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    print(proc.communicate())

    
    ####################################################
    ############ finishing apache install ##############
    #################################################### 
    
    time.sleep(SLEEPTIME)

    print("Creating Downloads directory...")
    download_dir = os.path.dirname(os.path.realpath(__file__)) + ROOTDIR
    
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)
        print("new dir created:")
        print(download_dir)

        
    else:
        print("dir Downloads already exists...")
    
    ####################################################
    ############## starting php install ################
    ####################################################    
    
    wget_info = wget + REMOTEDIR
    cmd = wget_info
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    print(proc.communicate())
    
    zip_info = echo + PASSWORD + " | sudo -S apt-get install zip -y"
    cmd = zip_info
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    print(proc.communicate())

    os.chdir(download_dir)
    print(os.curdir)
    
    unzip_info = unzip + ZIPFILE
    cmd = unzip_info
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    print(proc.communicate())
    
    unzip_info = echo + PASSWORD + " | sudo -S apt-get install zip -y"
    cmd = unzip_info
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    print(proc.communicate())
    
    php_info = echo + PASSWORD + " | sudo -S mv booked phpScheduleIt"
    cmd = php_info
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    print(proc.communicate())

    ####################################################
    ############### ending php install #################
    ####################################################  

    os.chdir(os.curdir + "\phpScheduleIt")
    print(os.curdir)
    
    php_info = echo + PASSWORD + " | sudo -S chmod 777 -R ./tpl ./tpl_c ./uploads"
    cmd = php_info
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    print(proc.communicate())

    php_info = echo + PASSWORD + " | sudo -S chown www-data:www-data -R ./tpl ./tpl_c ./uploads"
    cmd = php_info
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    print(proc.communicate())
    
    php_info = cp + "./config/config.dist.php ./config/config.php"
    cmd = php_info
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    print(proc.communicate())
    
    os.chdir(starting_dir)
    print(os.curdir)
    
    print("directory moved to /var/www/")
    
    ocult_info = echo + PASSWORD + " | sudo -S mv phpScheduleIt /var/www/"
    cmd = ocult_info
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    print(proc.communicate())
    
    ocult_info = echo + PASSWORD + " | sudo -S mv phpScheduleIt.zip .phpScheduleIt.zip"
    cmd = ocult_info
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    print(proc.communicate())

    print("ALL WELL DONE!")
    print("... Ending")
