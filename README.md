# ECE-4180-Security-Checkpoint
Created by:
- William Moore
- Trent Hannan

This project is a simple security checkpoint. This was achieved by using a Raspberry Pi, a button, and a Raspberry Pi camera. A user would walk up to the station and press the button. A preview pops up on the monitor and after 5 seconds the image is taken. The user is then prompted to enter their name, and after that information is entered an email with the image and their name is sent to a security officer. This can be used in many ways such as at an airport or as an entrance to a gated community.

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
The first step to making this project is to set up the Raspberry Pi. Using the Raspberry Pi imager and a micro SD card, the newest OS can be installed relatively easily. After installing the SD card with the newly installed OS on it, the Raspberry Pi can now be set up very easily. After choosing preferences and getting an internet connection, the Pi should now be running properly. Now check for updates by using the following commands:
```
sudo apt-get install update
sudo apt-get install upgrade
```
Next, camera support must be enabled. Use the following line to open the Pi's configuration:
```
sudo raspi-config
```
Once the configuration window opens, use the arrow keys to go down to interface options then hit enter. Next, select Legacy Camera, click enter, and when prompted if you would like to enable legacy camera support, select yes. Lastly, the Pi should give a choice to reboot, so choose yes for this option as well.

After the Pi has rebooted, the wiring should be done. Below is an image of the wiring setup and connections.
![PiSetup](https://user-images.githubusercontent.com/104606134/165874956-ef1b9269-bc14-4ced-8a88-19e5bd954d4f.jpg)

Connect the camera to the ribbon slot on the Pi labeled "Camera." Ensure that the metal connections on the ribbon wire are facing away from the black clasp that holds the wire in place. The camera is setup after seating this ribbon cable to the Pi and the camera itself. Next, put a pushbutton onto a small breadboard. Connect one button lead to ground on the Pi and the other to GPIO pin 4. This concludes all the connections and setup needed for the project to work.

# Running the Software and Using the Device
Once all the above connections and setup are done the project can now be run on the Raspberry Pi. Download the Project4180.py file in this repository and save it to any destination on the Pi. The program can be started by typing the following command in the terminal after navigating to the directory where the file is saved:
```
sudo python Project4180.py
```
Another option is to use the pre-installed Thonny IDE. By clicking on the Raspberry Pi logo on the top left of the screen, hovering over programming, then clicking on Thonny Python IDE. Then click on "Load" and chose Project4180.py as the file. The program can then be started by clicking "Run."

With the code now running, the Pi waits for the user input in form of the button being pressed. Once it is clicked, the camera preview will pop up and then capture the image after 5 seconds. The user is then prompted to type their name in using the wireless keyboard. After typing the user's name and hitting enter, an email will be sent to an address of the programmer's choice. Below is an example of what an email sent from this program looks like.

![TestEmail](https://user-images.githubusercontent.com/104606134/165876215-7982bd76-41ac-403f-a0b4-30c08312559e.JPG)

The email account that sends the email and the account that recives this email can be changed by simply editing the lines 29, 30, and 31 in the given code. Below is the code snippit of these lines and what each variable does. Note that the email account that sends the emails mult be a Gmail account. In addition to this, less secure app access mult be enabled on the account. This can be found by going to the Goggle acount settings and searching "Less secure app access." (NOTE: It appears Google is removing this feature mid 2022, without it some other steps may be needed in the future for Gmail account access).
```
29        address = '# insert sender's email here in the form: ____@gmail.com'
30        password = '# insert Gmail password for the address entered above'
31        securityAddr = '# insert reciver's email address here in the form: ___@gmail.com'
```

That is all that is needed to get the project running!

# Video Demo
Below is a YouTube link to a short demo that shows everything working.

https://youtu.be/rHeFz6U5Va8
