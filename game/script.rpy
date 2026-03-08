# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define scoffield = Character("Scoffield")
define hostage = Character("Hostage")
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
    scene hostage at full_screen
    scoffield "Everybody! Down!"
    scene vaut at full_screen
    scoffield "YOU! Open the vaut!"
    scene gun at full_screen
    scoffield "Now!"
    scene banker at full_screen
    hostage "I cant the manager is not here"
    scene police at full_screen
    "the "
    # This ends the game.: return
