# ECE-4180-Security-Checkpoint
by William Moore and Trent Hannan

This project is a simple security checkpoint. This was achieved by using a Raspberry Pi, a button, and a Raspberry Pi camera. A user would walk tup to the station and press the button. A preview pops up on the monitor and after 5 seconds the image is taken. The user is then prompted to enter their name, and after that information is entered an email with the image and there name is sent to a security officer. This can be used in many wasys such as at an airport or as an enterance to a gated community.

# Parts needed
Raspberry PI 4 or Zero ![Pi](https://user-images.githubusercontent.com/104606134/165873742-972a2898-082c-4c61-ad99-99e66e04e990.jpg)
Raspberry Pi NoIR Camera V2

![camera](https://user-images.githubusercontent.com/104606134/165873814-08d75191-73d7-4feb-b959-78066bb35bb4.jpg)


Breadboard Pushbutton 

![purshbutton](https://user-images.githubusercontent.com/104606134/165873885-0a8d9a4f-2b6d-4bf3-99eb-85c130713388.jpg)

In addition to the hardware, all the following cables, connectors, and accessories are needed:
- Raspberry Pi Power Supply
- HDMI Cord
- Wireless Keyboard and Mouse with Dongle
- Small breadboard
- Two Female to Male Wires
- Internet Connection to the Raspberry Pi

# Setup and Assembly
The first step to making this project is to set up the Raspberry Pi. Using the Raspberry Pi imager and a micro SD card, the newset OS can be installed realtively easy. After installing the SD card with the newly installed OS on it, the Raspberry Pi can now be set up very easily. After choosing prefernces and getting an internet connection, the Pi should now be running properly. Now check for updates by using the following commands:
```
sudo apt-get install update
sudo apt-get install upgrade
```
Next, camera supported must be enabled. Use the following line to open the Pi's configuation:
```
sudo raspi-config
```
Once the configuration window opens, use the arrow keys to go down to interface options then hit enter. Next, select Legacy Camera, click enter, and when prompted if you would like to enable legacy camera support, select yes. Lasty, the Pi should give a choice to reboot, so choose yes for this option as well.

After the Pi has rebooted, the wiring should be done. Below is an image of the wiring set up and connections.
![PiSetup](https://user-images.githubusercontent.com/104606134/165874956-ef1b9269-bc14-4ced-8a88-19e5bd954d4f.jpg)

Connect the camera to the ribbon slot on the Pi labeled "Camera." Ensure that the metal connections on the ribbon wire are facing away from the black clasp that holds the wire in place. The camera is set up after seating theis ribbon cabel to the Pi and the camera itself. Next, put a pushbutton onto a small breadboard. Connect one button lead to ground on the Pi and the other to GPIO pin 4. This concludes all the connections and setup needed for the project to work.

# Running the Software and Using the Device
Once all the above connections and setup is done the project can now be ran on the Raspberry Pi. Download the 4180Project.py file in this repository and save it to any destination on the Pi. The progam can be started by typing the following command in the terminal:
```
sudo python
