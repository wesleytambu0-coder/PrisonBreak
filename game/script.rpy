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
    scene weaponsss at full_screen with dissolve 
    scene weaponssss at full_screen with dissolve
    scene weaponsssss at full_screen with dissolve
    scene court at full_screen
    "Scoffield was arrested and sent to court"
    define judge = Character("Judge")
    scene judge at full_screen
    judge "Scoffield, you are found guilty of armed robbery and sentenced to 5 years in prison"
    scene judged at full_screen with fade
    "Scoffield was sent to prison"
    scene prison at full_screen
    scene inprison at full_screen with fade
    menu:
        "talk to the prison cop?"
        "yes":
            scene cop at full_screen
            define prison_cop = Character("Prison Cop")
            prison_cop "What are you in for?"
            menu:
                "tell the truth?":
                    "im in for armed robbery"
                    scene copshock at full_screen
                    "Prison Cop was shocked to hear that"

                    prison_cop "Damn, you really are a bad guy"
                    scene papper at full_screen
                "lie?":
                    "im in for beating up a cop"  
                    scene copshock at full_screen
                    prison_cop "you deserve this you people dont see value in us cops"
            "Scoffield was sent to his cell"        
        "No":
            scene cells at full_screen with dissolve
            scene incell at full_screen
            "Scoffield decided not to talk to the prison cop and was sent to his cell"
           
    




        

    # This ends the game.: return
