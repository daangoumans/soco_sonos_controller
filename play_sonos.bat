@echo off
echo Starting Sonos Controller
echo.
echo For BBC Radio 1 use: bbc1,
echo For NPO Radio 2 use: radio2
echo.
set /p channel="Please enter a channel: "

IF /i "%channel%"=="1" goto bbc1
IF /i "%channel%"=="bbc1" goto bbc1
IF /i "%channel%"=="2" goto radio2
IF /i "%channel%"=="radio2" goto radio2

echo No correct command found.
goto commonexit

:bbc1
plink -ssh sonos@192.168.1.78 -pw sonos python play.py bbc1
goto commonexit

:radio2
plink -ssh sonos@192.168.1.78 -pw sonos python play.py radio2
goto commonexit

:commonexit
pause
