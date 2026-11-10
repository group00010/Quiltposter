# Quilt Poster
Quilt poster

<img width="820" height="880" alt="image" src="https://github.com/user-attachments/assets/43449152-ed8c-433f-b28d-0902c3d86d4a" />

# R.E.L. (AKA Ria, Eden, Landy)
Created by: Ria, Eden, Landy

Course: Creative Coding, Pratt Institute

Semester: Fall 2026

# About The Project
The idea behind our poster generator was that they would contrast each other with different colors and shades. Our different designs combine everyone's individuality; different shapes create different characters for each quilt tile while also seeing what those different shapes look like with each other's color palettes. This creates a unified composition as the user can create any combination they want to see.

# The Interface
The user can modify the color palette and the designs of the tiles, with any combination they desire. 

# Meet The Designers
Ria: Yellowr! I made one set of the colour palettes and tile designs. I coded the canvas configuartion, grid and the randomisation of the quilt :3

Eden: I created my own color palette and designed a tile function with the shapes I wanted. I then created the function for the title and color squares to appear on the screen, as well as putting together the function that put the quilt, title, and color squares on the same screen. 

Landy: I created a color palette and tile design set. I coded the user input correction system and the pallete randomiser (Interaction and Data Engineer). 
#Psuedo code

Begin
import modules such as colab turtle, numpy
import pre-determined tile functions (Ria, Landy, eden)
import pre-determined colour palettes

1: Defining functions=
function draw_poster_text which determines the fixed text and palette at the bottom of the poster

2: Interactive Code Section=
a) gets name of the poster
b) A while loop which lets you choose your colour palette and doesn't let you move forward until a valid input
c) prints the options you have chosen
d) gets the number of columns and rows with the set boundries (3,9)
if input column count less than 3 prints too small 
else if input column count greater than 8 then prints too large 
else column no is defined
e) if input rows count less than 3, print too small 
else if input rows count greater than 8 ,then prints too large 
else rows no is defined\

3: Canvas layout generation=
sets a fixed screen width as 820
sets a basic square size as 100
sets margin side space as 50

Determines the tile size based on the inputs: ( screen width- margin side space*2)/ column no
Determines quilt height : ( margin side space*2)+ ( tile size)* row no
Sets screen height: integer( total quilt height)+( basic square size*3)

clears screen
initialises the window based on the screen height and width
sets t as turle
hides the turtle
sets turle speed as the highest

sets available tile styles from the previous imported modules
sets selected tile function at random from the above

4: Grid calculations
for loop that assigns a number code to each square in the grid and cycles through the rows and columns
for the corner square, the row and column code was unique and individually coded
calls selected tile style function(t, x=x computed, y= y computed, size= tile size, rotation = determined by corner location, palette= palette input)
For the border squares, the row and column code was either the row or column as a constant ( 0 or row/column input -1)
calls selected tile style function(t, x=x computed, y= y computed, size= tile size, rotation = randomly selected between 0, 180/ 90,270 determind by horzizonla or vertical border, palette= palette input)
else, the remaining squares were the centre squares
calls selected tile style function(t, x=x computed, y= y computed, size= tile size, rotation = randomly selected between 0, 180, 270, 90, palette= palette input)

5:
calls draw psoter text (t, quilt_title, - total screen height/2+ basic square size*2.5, active_palette)
move to (t, x= bsic_square_soze*2.75, y= total screen heigh/2+bsic square size)
prints colour palette in squares 
moves to predetermined location to print text from the draw poster text function
closes grphic pipeline
converts to svg format
End
# Try It Yourself 
Copy this code into a Colab Notebook.
''' !git clone https://github.com/group00010/Quiltposter
%cd Quiltposter
!pip install -r requirements.txt
from project import generate_poster
generate_poster()'''

How to Use
Open the notebook in Google Colab.
Run the setup cells to download the project code and install the required libraries.
Run the cell that calls the function and prompts the user to choose a title, grid dimensions, and color palette.
Your own poster will be saved as poster.svg!

# Files
project.py – Main poster-generation program.

palette_options.py – Available color palettes.

ria_tile_.py – Ria's function.

Eden_TileFunction.py – Eden's function

Landy_TileFunction.py – Landy's Function

requirements.txt – Libraries.

Example_Poster01.svg

Example_Poster02.svg

Example_Poster03.svg
