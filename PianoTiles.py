import mss #this can be aquired through pip
import time
import pyautogui #this can be aquired through pip

pyautogui.PAUSE = 0.01#This helps pyautogui do actions faster
time.sleep(1)
start = time.time()
#Note: it is currently set to "move to". this is to prevent unwanted click when starting/stoping program
#Note: Do to bad programing of piano tiles game that this bot plays, you can just click and hold the first tile, and you won't need to click the other tiles (just hold down click while bot moves itself)
while True:
	with mss.mss() as sct:
		monitor = sct.monitors[1]
		# Top and left represent the top left point. note that top is the y and left is the x. 
		# Width and height is the manhattan distances to the bottom left point.
		# Example: one gets the pixels between (420,360) and (520,460)
		one = sct.grab({'mon': 1, 'top':350, 'left':420, 'width':100, 'height':100})
		if one.pixel(0,0)[0] == 0:
			pyautogui.moveTo(420,350)

		two = sct.grab({'mon': 1, 'top':350, 'left':500, 'width':100, 'height':100})
		if two.pixel(0,0)[0] == 0:
			pyautogui.moveTo(500,350)

		three = sct.grab({'mon': 1, 'top':350, 'left':570, 'width':100, 'height':100})
		if three.pixel(0,0)[0] == 0:
			pyautogui.moveTo(570,350)

		four = sct.grab({'mon': 1, 'top':350, 'left':640, 'width':100, 'height':100})
		if four.pixel(0,0)[0] == 0:
			pyautogui.moveTo(640,350)