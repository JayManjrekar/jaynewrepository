{% include nav.html %}
# Create Task 
### Jay - (Memory Game) [Video Link](https://youtu.be/IBTZKOMER5w)
### 3A
**Overall purpose:** The overall purpose of the program is to provide a fun, beach-themed game, in which users can participate. The game is a classic matching game, through which the agents can enjoy themselves to a witty game.
**Functionality/Input:** The functionality of the program is to essentially flip two cards over permanently depending on whether they are a match or not. If the cards are not a match, then they will flip over. However, if the agent picks two matching cards, they will receive an alert that tells them that got a match. The overall object of the game is to have all matching cards.
**Input/Output:** Essentially the input is the moves in which the agent chooses the cards in the game. The output would be the feedback received from the backend that lets the agent know if it was a match or not. If it was a match then the agent would be alerted with a message.

### 3B
Storing Data in a List:

![list](https://user-images.githubusercontent.com/89176673/155947975-520b7929-4add-4196-a2b9-58fe719b32f4.PNG)

Using the Data:

![usinglist](https://user-images.githubusercontent.com/89176673/155948178-6960c95b-98cf-4441-8433-6bbcaec0cf31.PNG)


The list being used in this example is front images. The list manages complexity so that I do not have to keep restating the same content. Instead, the list is called once so that it is not repetitive, and more efficient. The list just refers to the ids that I have given to my images (1-11).

### 3C
Procedure:

![3ci](https://user-images.githubusercontent.com/89176673/155948573-136b2b00-4c24-462e-a3f6-b5997c91e79c.PNG)


Calling the procedure:


![3cii](https://user-images.githubusercontent.com/89176673/155948659-6fba6dcc-4d17-4916-86d6-dd537b103303.PNG)

The procedure essentially iterates over the image data. Additionally, it prints to the debugger console. Overall the functionality is made more efficient because repetition is not required.

**Detailed Description:** The algorithm starts off with a for loop which takes the variable "front image" from the array front images and prints it in the console. Then, if validate, ensures that there are no errors in the code and functionality. Then the first and second remove event listeners make it so that the images are flipped when they are clicked on.
### 3D
**Call 1:**
![call 1](https://user-images.githubusercontent.com/89176673/155948991-1cd93926-8afb-453a-a4dd-dd8f3d9d8d16.PNG)
The conditions which are being tested in the first call are whether or not the cards are matching. The cards are either permanently flipped or they are unflipped. In more general terms, they are either flipped or turned down.
**Call 2:**
The same condition is being tested by the second call, as to whether the cards are matching or not. This essentially determines the functionality of the overall process.

![call 2](https://user-images.githubusercontent.com/89176673/155949061-6a76cc32-7fa2-4eef-8327-abbd04dd5ca9.PNG)

