import turtle

def draw_rectangle(t, width, height, color):
    """Draws a filled rectangle."""
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()

def draw_circle(t, radius, color):
    """Draws a filled circle."""
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

def setup_screen():
    """Sets up the turtle screen."""
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("#A8DDEE") # Light blue background
    screen.title("Simplified Airplane Drawing")
    return screen

def move_to(t, x, y):
    """Lifts the pen and moves the turtle to a new coordinate."""
    t.penup()
    t.goto(x, y)
    t.pendown()

def draw_airplane():
    """Draws the main components of the airplane."""
    t = turtle.Turtle()
    t.speed(0)  # Set speed to fastest
    t.hideturtle()

    # --- 1. Main Body (Simplified outline using a rounded shape) ---
    move_to(t, -200, 0)
    t.pensize(3)
    t.color("white", "white")
    t.begin_fill()

    # Draw the main fuselage as a rounded rectangle shape
    t.forward(300)
    t.circle(-50, 90)
    t.forward(50)
    t.circle(-100, 90)
    t.forward(300)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(300)
    t.circle(100, 90)
    t.forward(50)
    t.circle(50, 90)
    t.setheading(180) # Face left for better control
    t.forward(300)

    t.end_fill()
    t.setheading(0) # Reset to face right

    # --- 2. Wings ---
    t.color("white", "white")
    
    # Left Wing (downward angle)
    move_to(t, -100, -20)
    t.begin_fill()
    t.right(15)
    t.forward(150)
    t.left(105)
    t.forward(50)
    t.left(75)
    t.forward(150)
    t.end_fill()
    t.setheading(0) # Reset direction

    # Right Wing (upward angle, hidden behind body in 2D view)
    move_to(t, -100, 20)
    t.begin_fill()
    t.left(15)
    t.forward(150)
    t.right(105)
    t.forward(50)
    t.right(75)
    t.forward(150)
    t.end_fill()
    t.setheading(0) # Reset direction

    # --- 3. Tail Fin ---
    move_to(t, 100, 50)
    t.begin_fill()
    t.left(90)
    t.forward(100)
    t.right(135)
    t.forward(141.42) # Diagonal length (approx)
    t.left(135)
    t.forward(100)
    t.end_fill()
    t.setheading(0) # Reset direction

    # --- 4. Cockpit Window (Black oval/rectangle) ---
    move_to(t, -180, 50)
    t.color("black")
    t.begin_fill()
    t.right(90)
    t.circle(15, 180) # Half circle
    t.forward(30)
    t.end_fill()
    t.setheading(0)

    # --- 5. Windows (Black circles) and Doors (Rectangles) ---
    t.color("black", "black")
    window_x = -100
    window_y = 20
    
    # Front Door
    move_to(t, -150, 40)
    t.setheading(0)
    draw_rectangle(t, 30, 60, "white")
    t.color("black")
    t.setheading(270) # Face down
    t.circle(5, 360) # Door knob/window

    # Row of Circular Windows
    for i in range(5):
        move_to(t, window_x + i * 40, window_y)
        draw_circle(t, 5, "black")

    # Aft Door
    move_to(t, 100, 40)
    t.setheading(0)
    draw_rectangle(t, 30, 60, "white")
    t.color("black")
    t.setheading(270) # Face down
    t.circle(5, 360) # Door knob/window

    # --- 6. Landing Gear (Simplified circles/half-circles) ---
    t.color("black")
    t.pensize(2)
    
    # Front Gear (visible in image)
    move_to(t, -120, 10)
    t.right(90)
    t.circle(10, 180) # Half circle for wheel

    # Main Gear (visible in image)
    move_to(t, 50, -60)
    t.setheading(0)
    t.right(90)
    t.circle(20, 180) # Half circle for wheel

    # --- 7. Text "SOUTHERN C919" ---
    move_to(t, 100, 120)
    t.color("black")
    t.setheading(0) # Important for text orientation
    t.write("SOUTHERN", font=("Arial", 10, "normal"))
    move_to(t, 100, 100)
    t.write("C919", font=("Arial", 24, "bold"))


if __name__ == "__main__":
    screen = setup_screen()
    draw_airplane()
    screen.mainloop()