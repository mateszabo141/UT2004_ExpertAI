# UT2004_ExpertAI
A little script that maxes out the difficulty settings for the AI in Unreal Tournament 2004.
# Purpose
The game's hardest difficulty (godlike) allows for additional modification in certain abilities of the bots. These modifying values are hardcoded into the game files and cannot be changed in the game. Some examples:

- Tactics=1.5
- StrafingAbility=+1.5
- Accuracy=0.5
- Aggressiveness=+0.4

If you're looking for challange, this program boosts all these values for all the bots to +9.9. (Extra fun with the instagib mode.)

# How to use

- Copy modifier.py into the games System directory. For example: C:\Program Files\Unreal Tournament 2004\System
- Double click on modifier.py
- It's going to attempt to modify the files "xplayersL1.upl", "xplayersL2.upl", "xaplayersl3.upl". If all went well, you get a message in the console and you can close the program.
- In the game set the bot difficulty to godlike for the effect to be the most perceptible.
# Notes
Use at your own risk! Since the program overwrites game files, it's a good idea to make a backup copy of the following files found in the System directory of the game before you run the program:

- xplayersL1.upl
- xplayersL2.upl
- xaplayersl3.upl