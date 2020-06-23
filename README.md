# ChromeDinoAutomation
Autonomous Dino run using pyautogui and pillow.
###
<img src="https://github.com/kanish51/ChromeDinoAutomation/blob/master/playing.gif" width="800" height="300"/>

## Working
<img src="https://github.com/kanish51/ChromeDinoAutomation/blob/master/working.jpg" width="800" height="400"/>

Region of pixels(box) is selected for obstacle detection.   
The pixels of this region are then compared with a static pixel in background to detect obstacle.  
If the obstacle is near ground then the up arrow key is simulated.   
If obstacle is near the head then the dino ducks by simulating down arrow.

With the increasing speed the region is also shifted to accomodate the change in speed.

## Dependencies
- pyautogui  
- PIL for region

## Usage  
The capturing region of pixels must be tuned as per your display.
