# Mouse mover
I really hate when my status on games or chats goes to offline just because I haven't moved my mouse recently. 

So I decided to write a simple code to do this for me.
In my research I found PyAutoGUI https://pyautogui.readthedocs.io/en/latest/index.html

I used the mouse control functions to move the mouse to random spots in the set quadrant of coordinates. The quadrant is defined by x and y.
Then the time modules defines for how long the mouse should be moved - in this case the minutes are taken from the input box

When the programme is ran the following window pops up
![image](https://user-images.githubusercontent.com/101068051/206768570-94a69fe5-4eeb-45fe-888a-95a4d2165694.png)

After entering the minutes and clicking on the "Move!" button, the mouse coursor will start moving by itself for the given amount of time.
