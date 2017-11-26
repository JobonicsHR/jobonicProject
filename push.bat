@echo off
echo pushing to heroku
set INPUT=
set /P INPUT=Type commit message:
git add .
git commit -am "%INPUT%""
git push heroku master
echo ...
echo Pushing to Github > dev
git push origin dev
pause