# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define scoffield = Character("Scoffield")

transform full_screen:
    size (config.screen_width, config.screen_height)

label start:

    # fULL SCREEN BG
    scene bank at full_screen 

    "And i found  myself  near a bank "

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show eileen happy

    # These display lines of dialogue.

    scoffield "You've created a new Ren'Py game."

    scoffield "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
