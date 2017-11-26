@echo off
echo pushing to heroku
git add .
set INPUT=
set /P INPUT=Type commit message:
git commit -m %INPUT%
git push heroku master
echo ...
echo Pushing to Github > dev
git push origin dev
pause