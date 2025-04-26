from random import randrange
from graphics import *
from buttons import Button, Dropdown
from die import DieView


def main():
    # create application window
    win = GraphWin("Dice Roller", 500, 400)
    win.setCoords(0, 0, 10, 10)
    win.setBackground("green2")

    # Create a dropdown menu for selecting the number of dice
    dice_options = ["1", "2", "3", "4", "5"]
    dice_dropdown = Dropdown(win, Point(2.5, 9), 2, 0.8, dice_options, "Dice")
    
    # Initialize dice array - we'll create up to 5, but only display based on selection
    dice = []
    max_dice = 5
    
    # Calculate positions for the dice (they'll be evenly spaced)
    positions = []
    for i in range(max_dice):
        x_pos = 1.5 + (i * 1.75)
        positions.append(Point(x_pos, 7))
    
    # Create the dice views
    for i in range(max_dice):
        die = DieView(win, positions[i], 1.5)
        # Initially hide dice beyond the first 2
        if i >= 2:
            die.hide()
        dice.append(die)

    # Buttons for interaction
    rollButton = Button(win, Point(5, 4.5), 6, 1, "Roll Dice")
    rollButton.activate()

    # Create the total display
    totalText = Text(Point(5, 3), "Total: 0")
    totalText.setSize(16)
    totalText.draw(win)

    quitButton = Button(win, Point(5, 1), 2, 1, "Quit")
    quitButton.activate()

    # Event Loop
    pt = win.getMouse()
    while not quitButton.clicked(pt):
        if rollButton.clicked(pt):
            # Get the number of dice to roll
            num_dice = dice_dropdown.get_value()
            
            # Roll the dice and calculate total
            total = 0
            for i in range(max_dice):
                if i < num_dice:
                    # Show and roll dice that are active
                    dice[i].show()
                    value = randrange(1, 7)
                    dice[i].setValue(value)
                    total += value
                else:
                    # Hide dice that aren't being used
                    dice[i].hide()
            
            # Update total display
            totalText.setText(f"Total: {total}")
            
        # Check if dropdown was clicked
        dice_dropdown.clicked(pt)
        
        # Get next mouse click
        pt = win.getMouse()

    win.close()


main()
