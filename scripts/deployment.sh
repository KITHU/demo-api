#!/bin/bash
echo " "
echo " "

echo "<<<<<<<<<<< Installing requirements >>>>>>>>>>>>>>"
echo " "

make install

echo ‘'<<<<<<<<<<<<<<' Run migration '>>>>>>>>>>>>>>>>>>>>>>>'’

echo " "

make migrate

echo "<<<<<<<<<<<<<< Daemon Reload >>>>>>>>>>>>>>>>>>>>"
sudo systemctl daemon-reload

echo " "
echo "<<<<<<<<<<<<<< Restarting gunicorn >>>>>>>>>>>>>>>>>>>>"
sudo  systemctl restart gunicorn

echo " "
echo " "

echo "<<<<<<<<<<<<<<<< Restarting nginx >>>>>>>>>>>>>>>>>>>>>>"
echo " "
sudo systemctl restart nginx

exit