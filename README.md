# ChromeDinoAutomation
Chrome dino game automation using python

Region of pixels is selected for obstacle detection
The pixels of this region are then compared with a static pixel in background to detect obstacle

if the obstacle is near ground then the up arrow key is simulated
if obstacle is near the head then the dino ducks by simultaion down arrow

with the increasing speed the region is also shifted to accomodate the change in speed


Dependencies:
pyautogui
PIL for region
