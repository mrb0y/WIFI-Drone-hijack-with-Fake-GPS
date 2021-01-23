# WIFI-Drone-hijack-with-Fake-GPS
WPA2/WPA WIFI Drone hijack control by ROS with hackrf one fake GPS

## About The Project

Hong Kong Institute of Vocational Education (Chai Wan)

Information and Network Security (IT114104) Final Year Project

## Collaborators
* **Alex Wong**     - *WIFI WPA/WPA2 hacking , Fake GPS and crack password*
* **Cherry Zhang**  - *ROS (Parrot Bebop 2,DJI Tello) to take off , land down , take camera and open drone folder*
* **Sunny Chan**     - *Main program , GUI deskgn , WIFI connection and server tools* - [Github](https://github.com/SunnyChan-code)

## Getting Started
These instructions will provide you with a copy of the project running and running on your local computer for development and testing. For notes on how to deploy the project on a real-time system, see deployment.

### Set up environment 

Hardware
``` 
1. a Ubuntu 16.04 desktop (We set up in virtual machine)
2. two Wifi antenna (for the aircrack-ng)
3. a hackrf one(fakegps)
4. Drone (for testing e set up (Parrot Bebop 2,DJI Tello)
4. a server with powerful gpu (Used : pc with GTX1080 x 4 )
```


Software 
``` 
1. Ubuntu 16.04 desktop
2. ROS ROS Kinetic (need to set up for each model of drone)
3. a hackrf one
4. Drone (for testing e set up (Parrot Bebop 2,DJI Tello)
5. Python3 with tkinter , ttk , threading , os , time , subprocess , csv , datetime , pyautogui , string , sys , requests , re
6. nmap    (Parrot Bebop 2 control)
7. Mplayer (DJI tello control)
8. xdotool (DJI tello control)
9. hackrf (hackrf on drive)
```

Please keep the server (for crack password) and the pc can communication with each other 
For the api work please keep the pc connect to the internet 

## License

Distributed under the GPL-3.0 License. See `LICENSE` for more information.

## Code reference:

* "/CrackPasswdTools/hashcat-utils-master/":     https://github.com/hashcat/hashcat-utils


