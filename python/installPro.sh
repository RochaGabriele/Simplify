#!/bin/bash
mysql -u root -p < simplify.sql
echo #!/bin/bash python3 Main.py > simplify
chmod +x simplify
cp simplify /usr/bin
simplify

