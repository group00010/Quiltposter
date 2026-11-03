# Landy_TileFunction.py

def draw_landy_tile(t, x, y, size, rotation, palette, tile_type="center"):


  # ==========================================
  # TURTLE SETUP
  # ==========================================
  t.penup()
  t.jumpto(x, y)
  t.setheading(rotation)s

  # Useful relative dimension constants (derived from size)
  half = size / 2
  quarter = size / 4

  # ==========================================
  # BASE BACKGROUND
  # All tile variations share a clean backdrop
  # ==========================================
  # Move to the bottom-left corner relative to orientation
  t.forward(-half)
  t.left(90)
  t.forward(-half)
  t.right(90)

  t.pencolor(palette["bg"])
  t.fillcolor(palette["bg"])
  t.pensize(2)
  t.pendown()
  t.begin_fill()
  for _ in range(4):
      t.forward(size)
      t.left(90)
  t.end_fill()
  t.penup()

  # Return turtle to the true center of the tile
  t.jumpto(x, y)
  t.setheading(rotation)


  if tile_type == "corner":


      t.forward(half - quarter)
      t.pendown()
      t.color(palette["primary"], palette["primary"])
      t.begin_fill()
      t.left(90)
      t.circle(quarter, 90) # Drawst 90-degree corner arc
      t.left(90)
      t.forward(quarter)
      t.left(90)
      t.forward(quarter)
      t.end_fill()
      t.penup()


      t.jumpto(x, y)
      t.setheading(rotation)
      t.color(palette["primary"], palette["primary"])
      t.forward(quarter + quarter / 2)
      t.left(90)
      t.forward(quarter)

      t.pendown()

      t.circle(quarter/2)
      t.left(90)
      t.forward(quarter/2)
      t.color(palette["secondary"])
      t.dot(quarter)
      t.penup()

      t.jumpto(x, y)
      t.setheading(rotation)


      t.jumpto(x, y)
      t.setheading(rotation)
      t.forward(half)          # Move to the edge of your tile boundaries
      t.left(90)
      t.forward(half)
      t.left(135)             # Turn inward along the diagonal axis of symmetry
      t.pendown()
      t.color(palette["accent"])
      t.pensize(5)
      t.forward(quarter)
      t.penup()

      t.jumpto(x, y)
      t.setheading(rotation)

  # ------------------------------------------
  # OPTION 2: BORDER TILE
  # ------------------------------------------
  elif tile_type == "border":


      t.color(palette["primary"], palette["primary"])
      t.forward(-half)
      t.left(90)
      t.forward(quarter)
      t.right(90)

      t.pendown()
      t.begin_fill()
      for _ in range(2):
          t.forward(size)
          t.left(90)
          t.forward(quarter)
          t.left(90)
      t.end_fill()
      t.penup()

      t.jumpto(x, y)
      t.setheading(rotation)
      t.pencolor(palette["accent"])
      t.pensize(1)
      t.forward(-half)
      t.pendown()
      t.forward(size)
      t.penup()

   #Dotted
      t.penup()
      t.jumpto(x, y)
      t.setheading(rotation)
      t.pencolor(palette["accent"])
      t.pensize(4)

      # Dotted Accent Border
      t.forward(-half)
      t.left(90)
      t.forward(quarter)
      t.right(90)

      # Draw dashed/dotted accent line across the top
      for _ in range(4):
          t.pendown()
          t.forward(size / 8)
          t.penup()
          t.forward(size / 8)
# bottom border dots
      t.penup()
      t.jumpto(x, y)
      t.setheading(rotation)
      t.forward(-half)
      t.right(90)
      t.forward(-half/2) # Move to the bottom edge
      t.left(90)

      # Draw 3
      for _ in range(3):
          t.forward(size / 4)
          t.pendown()
          t.circle(2) # Tiny accent dot
          t.penup()
      t.forward(size / 4)

  # ------------------------------------------
  # OPTION 3: CENTER TILE
  # ------------------------------------------
  else:


      t.pencolor(palette["secondary"])
      t.pensize(2)
      t.jumpto(x, y)
      t.setheading(rotation)
      t.penup()
      t.forward(quarter * 1.1)  # Move out to radius
      t.left(90)
      t.pendown()
      t.circle(quarter * 1.1)    # Draw a framing circle
      t.penup()

      # 2. Rounded Flower Petals
      t.color(palette["primary"], palette["primary"])
      t.jumpto(x, y)
      t.setheading(rotation)

      for _ in range(4):
          t.pendown()
          t.begin_fill()
          t.circle(quarter * 0.4, 180)
          t.left(90)
          t.circle(quarter * 0.4, 180)
          t.end_fill()
          t.penup()

          # Rotate 90 degrees around the center for the next petal
          t.jumpto(x, y)
          t.left(90)

      # 3. Star Center
      t.jumpto(x, y)
      t.setheading(rotation)
      t.pencolor(palette["accent"])
      t.pensize(3)

      for _ in range(8):
          t.penup()
          t.forward(quarter * 0.2) # Leave a small gap near the exact center
          t.pendown()
          t.forward(quarter * 0.3) # Draw a dash
          t.penup()
          t.jumpto(x, y)
          t.right(45)




  # ==========================================
  # DRAW BORDER (OPTIONAL IF YOU WANT A BORDER)
  # ==========================================

  ############## This part is my own drawing #######################
  ################## Change it to your design ######################
  t.pencolor(palette["secondary"])
  t.pensize(2)

  # Go to the corner
  t.penup()
  t.jumpto(x, y)
  t.setheading(rotation)
  t.forward(-half)
  t.left(90)
  t.forward(-half)
  t.right(90)

  # Draw the border
  t.pendown()
  for _ in range(4):
      t.forward(size)
      t.left(90)
  t.penup()
