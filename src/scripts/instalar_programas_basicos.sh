#!/bin/bash

sudo apt-get update > log
validArgs=1

showhelp() {
	echo "ayuda..."
	echo "-a : install all"
	echo "-b : install basic."
	echo "-d : install advanced"
	echo "-j : install java"
}

if [ "$#" -ne 1 ]; then
	echo "invalid argument number"
	$validArgs=0
	showhelp
	exit
fi

iBasic=0
iAdvanced=0
iJava=0
iTest=0

if [ "$1" == "-h" ]; then
	echo "Help chosen!"
	echo $iTest
	iTest=1
	echo $iTest
	exit
fi


if [ "$1" == "-a" ]; then
	echo "All chosen!"
	iBasic=1
	iAdvanced=1
	iJava=1
fi

if [ "$1" == "-b" ]; then
	echo "Basic only chosen!"
	iBasic=1
fi

if [ "$1" == "-d" ]; then
	echo "Advanced only chosen!"
	iAdvanced=1
fi

if [ "$1" == "-j" ]; then
	echo "Java only chosen!"
	iJava=1
fi

if [ "$iBasic" -eq 1 ]; then
echo "Installing Basic..."	
#basic
sudo apt-get install vim
sudo apt-get install git
sudo apt-get install indicator-cpufreq
sudo apt-get install psensor
sudo apt-get install caffeine
echo "finished Basic!"
fi

if [ "$iAdvanced" -eq 1 ]; then
echo "Installing Advanced..."	
#advanced
sudo apt-get install bleachbit
sudo apt-get install dropbox
sudo apt-get install unity-tweak-tool
echo "finished Advanced!"
fi

if [ "$iJava" -eq 1 ]; then
echo "Installing Java..."
#install java8
sudo add-apt-repository ppa:webupd8team/java
sudo apt-get update
sudo apt-get install oracle-java8-installer
echo "finished Java!"
fi
