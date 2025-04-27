from random import randrange
from graphics import *
from buttons import Button, Dropdown
from die import DieView


def main():
    # create application window with modern styling
    win = GraphWin("Dice Roller", 600, 450)
    win.setCoords(0, 0, 10, 10)
    win.setBackground("#2E3B4E")
    
    # Title of the app
    title = Text(Point(5, 9.5), "Dice Roller")
    title.setSize(20)
    title.setStyle("bold")
    title.setTextColor("white")
    title.draw(win)

    # Control Panel area
    control_panel = Rectangle(Point(0.5, 7.5), Point(9.5, 8.75))
    control_panel.setFill("#F8F9FA")
    control_panel.setOutline("#DEE2E6")
    control_panel.draw(win)
    
    dice_options = ["1", "2", "3", "4", "5"]
    dice_dropdown = Dropdown(win, Point(1.75, 8.125), 2, 0.75, dice_options, "Dice")
    sides_options = ["4", "6", "8", "10", "20"]
    sides_dropdown = Dropdown(win, Point(8.25, 8.125), 2, 0.75, sides_options, "Sides")
    rollButton = Button(win, Point(5, 3), 1.35, 0.8, "ROLL")
    rollButton.activate()

    # Container for dice display area
    dice_container = Rectangle(Point(0.5, 4), Point(9.5, 6.5))
    dice_container.setFill("#FFFFFF")
    dice_container.setOutline("#EEEEEE")
    dice_container.setWidth(2)
    dice_container.draw(win)
    
    # Initialize dice array
    dice = []
    max_dice = 5
    
    # Calculate positions for the dice (they'll be evenly spaced)
    positions = []
    for i in range(max_dice):
        x_pos = 1.5 + (i * 1.75)
        positions.append(Point(x_pos, 5.25))
    
    # Create the dice views with modern styling
    for i in range(max_dice):
        die = DieView(win, positions[i], 1.5)
        # Initially hide dice beyond the first 2
        if i >= 2:
            die.hide()
        dice.append(die)

    # Create the total display with modern styling
    total_label = Text(Point(5, 2), "TOTAL")
    total_label.setSize(12)
    total_label.setTextColor("#DDDDDD")
    total_label.draw(win)
    
    totalText = Text(Point(5, 1.5), "0")
    totalText.setSize(24)
    totalText.setStyle("bold")
    totalText.setTextColor("#DDDDDD")
    totalText.draw(win)
    
    # Modern quit button
    quitButton = Button(win, Point(9, 0.7), 1, 0.6, "✕")
    quitButton.activate()

    # Event Loop
    pt = win.getMouse()
    while not quitButton.clicked(pt):
        if rollButton.clicked(pt):
            # Get the number of dice to roll
            num_dice = dice_dropdown.get_value()
            
            # Get the number of sides on each die
            sides = sides_dropdown.get_value()
            
            # Roll the dice and calculate total
            total = 0
            for i in range(max_dice):
                if i < num_dice:
                    # Show and roll dice that are active
                    dice[i].show()
                    value = randrange(1, sides + 1)
                    dice[i].setValue(value)
                    total += value
                else:
                    # Hide dice that aren't being used
                    dice[i].hide()
            
            # Update total display
            totalText.setText(str(total))
            
        # Check if dropdowns were clicked
        dice_dropdown.clicked(pt)
        sides_dropdown.clicked(pt)
        
        # Get next mouse click
        pt = win.getMouse()

    win.close()


if __name__ == "__main__":
    main()
