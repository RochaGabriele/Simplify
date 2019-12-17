#!/bin/bash
sudo pacman -Syyu mariadb gvim
sudo mysql_install_db --user=mysql --basedir=/usr --datadir=/var/lib/mysql
sudo mysql_secure_installation 
123456 
n 
y
y
y
y
y

mysql -u root -p < simplify.sql
echo #!/bin/bash python3 Main.py > simplify
chmod +x simplify
cp simplify /usr/bin/
simplify



	
