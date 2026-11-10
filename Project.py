# project.py

from ColabTurtlePlus.Turtle import *
import numpy as np

# Import your own code from TileFunctions.py and PaletteOptions.py
from Eden_TileFunction import *
from Landy_TileFunction import *
from ria_tile_ import *
from palette_options import
def generate_poster():
    
    def draw_poster_text(t, title, y_position, palette):
        # canvas_height = quilt_height + side_space
        t.penup()
        t.jumpto(0, y_position)
        t.pencolor(palette["primary"])
        t.write(title, align="center",
                font=("Times New Roman", 35, "bold"))
    
        t.penup()
        t.jumpto(0, y_position - 30)
        t.pencolor((palette["secondary"]))
        t.write("Created by: Ria, Eden, Landy.team(R.E.L.)",
                align="center",
                font=("Times New Roman", 18, "bold"))
    # Interactive Part
    #ChooseTitle
    import random
    title = input ("Enter the name of your quilt:")
    
    #ChooseColorPalette
    p_name = input("Enter the name of the color palette you wish to use: ")
    
    while p_name not in palette_names:
      print(f"Invalid palette name. The valid names are {palette_names}.")
      p_name = input("Enter the name of the color palette you wish to use: ")
    
    print(f"You have selected the {p_name} palette.")
    
    if p_name == "random":
      print("Now generating a random color palette...")
      # Generate random palette.
    else:
      palette = palette_options[p_name]
    
    print("Success! Now generating your poster...")
    
    #Choosing a random color palette
    if p_name == "random":
        print("Now generating a random color palette...")
        # Pick a random list of colors from the available non-random palettes
       # available_palettes = list(palette_options.values())
       # palette = random.choice(available_palettes)
        palette = {}
        for key in ["bg", "primary", "secondary", "accent"]:
          r = np.random.randint(256)
          g = np.random.randint(256)
          b = np.random.randint(256)
          palette[key] = (r, g, b)
        print("Generated palette:", palette)
    else:
        palette = palette_options[p_name]
        print("Selected palette:", palette)
    
    #ChooseNumberColumns
    
    min_max = (3,4,5,6,7,8)
    n_col = int(input("Enter the number of columns: "))
    
    while n_col not in min_max:
      if n_col < 3:
        print("The number is too small. Choose a number between 3 and 8.")
        n_col = int(input("Enter the number of columns for the quilt: "))
    
      elif n_col > 8:
        print("The number is too large. Choose a number between 3 and 8.")
        n_col = int(input("Enter the number of columns for the quilt: "))
    
    else:
        print(f"You have chosen {n_col} columns for the quilt.")
    #ChooseNumberRows
    min_max = (3,4,5,6,7,8)
    n_row = int(input("Enter the number of rows: "))
    
    while n_row not in min_max:
      if n_row < 3:
        print("The number is too small. Choose a number between 3 and 8.")
        n_row = int(input("Enter the number of rows for the quilt: "))
    
      elif n_row > 8:
        print("The number is too large. Choose a number between 3 and 8.")
        n_row = int(input("Enter the number of rows for the quilt: "))
    
    else:
        print(f"You have chosen {n_row} rows for the quilt.")
    
    
    screen_width = 820
    
    square_size = 100
    
    # defining screen width
    side_space = 50
    
    size_p = (screen_width - side_space * 2) / n_col # size of each tile in the quilt
    quilt_height= side_space*2 + size_p*n_row
    
    screen_height = int(quilt_height + square_size * 3)
    
    clearscreen()
    setup(screen_width, screen_height)
    t = Turtle()
    t.hideturtle()
    t.speed(0)
    
    TILE_FUNCTIONS =[draw_ria_tile, draw_landy_tile, draw_eden_tile] #creating the set for the dictionaries
    TILE_FUNCTION= random.choice(TILE_FUNCTIONS)# picking a random dictionary
    
    for row in range(n_row):
       for col in range(n_col):
        xval = -screen_width / 2 + side_space + size_p*(col+0.5)
        yval = screen_height/2 - size_p*(row+0.5) - 50
    
        if row == 0 and col == 0:
      # Upper left corner
         tile_type = "corner"
         rotation = 90
         TILE_FUNCTION(t, x=xval, y=yval, size = size_p, rotation = rotation, palette = palette, tile_type="corner")
    
        elif row == 0 and col == n_col-1:
      # Upper right corner
         tile_type = "corner"
         rotation = 0
         TILE_FUNCTION(t, x=xval, y= yval, size = size_p, rotation = rotation, palette = palette, tile_type="corner")
    
        elif row == n_row-1 and col == 0:
      # Lower left corner
         tile_type = "corner"
         rotation = 180
         TILE_FUNCTION(t, x=xval, y= yval, size = size_p, rotation = rotation, palette = palette, tile_type="corner")
    
        elif row == n_row-1 and col == n_col-1:
      # Lower right corner
         tile_type = "corner"
         rotation = 270
         TILE_FUNCTION(t, x=xval, y= yval, size = size_p, rotation = rotation, palette = palette, tile_type="corner")
    
        elif (col == 0 or col == n_col - 1) and row != 0 and row != n_row - 1:
      # Vertical border
         tile_type = "border"
         rotation = 90 + np.random.randint(2) * 180  # should be 90 or 270
         TILE_FUNCTION(t, x=xval, y= yval, size=size_p, rotation=rotation, palette= palette, tile_type="border")
    
        elif (row == 0 or row == n_row - 1) and col != 0 and col != n_col - 1:
      # Horizontal border
         tile_type = "border"
         rotation = np.random.randint(2) * 180  # should be 0 or 180
         TILE_FUNCTION(t, x=xval , y=yval, size=size_p, rotation=rotation, palette= palette, tile_type="border")
    
        else:
         tile_type = "center"
         rotation = np.random.randint(4) * 90  # should be 0, 90, 180, or 27
         TILE_FUNCTION(t, x= xval, y= yval, size=size_p, rotation=rotation, palette= palette, tile_type="center")
    
    
    
    draw_poster_text(t, title, -screen_height/2 + square_size * 2.5, palette)
    
    t.jumpto(-square_size * 2.75, -screen_height / 2 + square_size * 1)
    
    # Loop through all key, value pairs in the color palette dictionary.
    for label, rgb_value in palette.items():
    
      t.setheading(0)
      # Set the line color and the fill color.
      t.color(rgb_value, rgb_value)
    
      # Draw and fill the square.
      t.pendown()
      t.begin_fill()
      for i in range(4):
        t.forward(square_size)
        t.left(90)
      t.end_fill()
    
      # Write the label.
      t.penup()
      t.right(90)
      t.forward(20)
      t.left(90)
      t.forward(square_size / 2)
      t.write(rgb_value, align="center", font=("Arial", 16, "bold"))
    
      # Prepare for the next square.
      t.forward(square_size)
      t.left(90)
      t.forward(20)
      t.right(90)
    
    t.hideturtle()
    t.done()
    
     # Save the poster as an SVG file
    saveSVG("/content/poster.svg")
