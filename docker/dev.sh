#!/bin/sh
echo "<<<<<<<<<<<<<<< sleep >>>>>>>>>>>>>>>>>>>"
sleep 10

echo "<<<<<<<<<<<<<<< migration started >>>>>>>>>>>>>>>>>>>"
python manage.py migrate --no-input
echo "<<<<<<<<<<<<<<< migration completed >>>>>>>>>>>>>>>>>>>"

echo "<<<<<<<<<<<<<<< set collectstatic  >>>>>>>>>>>>>>>>>>>"
python manage.py collectstatic --no-input
echo "<<<<<<<<<<<<<<< completed >>>>>>>>>>>>>>>>>>>"

echo "<<<<<<<<<<<<<<< starting server >>>>>>>>>>>>>>>>>>>"

python manage.py runserver 0.0.0.0:8000

echo "<<<<<<<<<<<<<<< server running >>>>>>>>>>>>>>>>>>>"