echo """
----------------------
|Choose your platform|
|====================|
| [1] Linux----------|
| [2] Termux---------|
|====================|
|____________________|
"""
read platform

if [ $platform  = '1' ]
then
	apt install colorama
	apt install time
	apt install argparse
	apt install os
	apt install sys
	apt install requests
elif [ $platform = '2' ]
then
	pkg install colorama
	pkg install time
	pkg install argparse
	pkg install os
	pkg install sys
	pkg install requests
fi
