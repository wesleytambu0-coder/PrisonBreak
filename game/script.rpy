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

    scene hostage at full_screen with fade 
    scoffield "Everybody! Down!"
    scene vaut at full_screen
    scoffield "YOU! Open the vaut!"
    scene gun at full_screen
    scoffield "Now!"
    scene banker at full_screen
    hostage "I cant the manager is not here"
    scene police at full_screen
    "the police arrived and surrounded scoffield"
    define police = Character("Police")
    police "hands up! and turn around!"
    scene handsup at full_screen with dissolve
    scene handsupp at full_screen with fade
    scene car at full_screen
    police "drop your weapons now!!!"
    scene weapons at full_screen with fade 
    scene weaponss at full_screen with dissolve 
    

    # This ends the game.: return
