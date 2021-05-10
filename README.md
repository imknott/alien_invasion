# alien_invasion
 A project to learn pygame and development tools with python. 
In Alien invasion, the player controls a rocket ship that appears at the bottom center of the screen. The player can move the ship right and left using the arrow keys and shoot bullets using the spacebar. When the game begins, a fleet of aliens fills the sky and moves across and down the screen. The player shoots and destroys the aliens. If the player shoots all the aliens, a new fleet appears that moves faster than the previous fleet. If any alien hits the players ship or reaches the bottom of the screen the player loses a ship. If the player loses three ships, the game ends. 

Development Phase 1:
------------------------------------------------------------------------- 
Make a ship that can move right and left and fires bullets when the player presses the spacebar. The ship image was saved as a rect since it is a simple geometric shape and will make collisions in the program easier to recognize. 

        #load the ship image and get its rect. 
        self.image = pygame.image.load('assets/images/ship.bmp')
        self.rect = self.image.get_rect()
        
After this I will begin the phase of creating aliens and refine gameplay. 



Development Phase 2:
--------------------------------------------------------------------------
Generate a fleet of aliens that will move down, and side to side until they have all been eliminated by the player. I will also be analyzing which areas of the code I might need to refactor before building the new ideas. 

Development Phase 3: 
---------------------------------------------------------------------------
Create a score system. Analyze code to see if any methods or classes can be refactored. Decide if there are any additional features to be adeed. 

Final Development Phase: 
----------------------------------------------------------------------------
Sound effects added, as well as a highscore that will be stored in a json file to be used to keep the high score persistent everytime the game is reopened. I also plan to tweak the sound efeects more once I learn a bit more about pygame mixer.


Imports for this project: 
-------------------------------------------------------------------------

import sys: uses system tools for quit so the player can exit game 
import pygame: contains the functionality needed to make the game. 
import json: to store the highscores

Thank you so much for checking out my project and I hope that you enjoyed the game. I am currently lookig for work, so if you would like to hire me contact me at ianmatknott@gmail.com 

