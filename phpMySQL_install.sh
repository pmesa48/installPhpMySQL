#!/bin/bash
# Install PHP and MySQL
# LAB 3 INFRACOM 2014-I
# Santiago Felipe Arteaga Martin ISIS/IMEC 200411086
# Pablo Santiago Mesa Triviao ISIS 201023617
# Richard Alejandro Becerra Espinosa ISIS/MATE 201012278

pass="labredesML340"

echo "Installing missing libraries"

echo mysql-server-5.5 mysql-server/root_password password $pass | sudo debconf-set-selections
echo mysql-server-5.5 mysql-server/root_password_again password $pass | sudo debconf-set-selections
sleep 5
echo $pass | sudo -S apt-get update -y
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

echo $pass | sudo -S chmod 777 -R ./tpl ./tpl_c ./uploads

echo $pass | sudo -S chown www-data:www-data -R ./tpl ./tpl_c ./uploads

cp ./config/config.dist.php ./config/config.php

cd ..

echo "directory moved to /var/www/"

echo $pass | sudo -S mv phpScheduleIt /var/www/

echo $pass | sudo -S mv phpScheduleIt.zip .phpScheduleIt.zip

echo $pass | sudo -S chown labredes:labredes /etc/php5/apache2/php.ini

echo $pass | sudo -S chmod 777 /etc/php5/apache2/php.ini

echo date.timezone = America/Bogota >> /etc/php5/apache2/php.ini

echo $pass | sudo service apache2 restart

echo "You may now visit http://<your-ip>/phpScheduleIt/"


