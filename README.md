# Budokai3AP
This repo is designed to work with the Archipelago system of multi-game randomizing. You can learn more at https://archipelago.gg and view the source code at https://github.com/ArchipelagoMW/Archipelago.

This repo is a randomizer for Dragon Ball Z: Budokai 3 for the PS2. It will likely never work with the PS3/Xbox360 Budokai HD Collection version of the game.

## What is Dragon Ball Z: Budokai 3?
Budokai 3 is the third game in a series of 3D fighting games for the Sony Playstation 2 (and until Budokai 3, the Nintendo Gamecube) that are defined by their Dragon Ball Z association. You can expect to be slinging energy blasts, clashing with energy beams, flying around the stage, and beating up baddies. In the story mode, you can fly all over the world, finding various items, events, and money to buy even more items with in the shop. 


## Goals and fixes to implement:
If you have any ideas, the best place to let me know would be by creating an [issue](/issues) if you don't see your suggestion here. The second best place would be the Archipelago Discord's Budokai 3 thread.
* Randomize item locations
* Allow for receiving items from the Archipelago server
* Add in-game map markers for various items (keep red dot for bosses/story events, use blue dots for items, orange dots for dragon balls)
* Sending Death Link signals (currently the game only receives them)
* Allow for collecting all items on the Shenron screen
  * This could be just granting all 3 when one is selected
  * This could be making the screen wait until all options are chosen
* Fix typos in the original game as well as any mistakes I make:
  * "Namekains": Typo in Bulma's speech on Planet Namek in either Kid Gohan or Krillin's DU
  * "Paragas' Admonsihment": Typo in capsule name
  * "Guage": Common misspelling of "gauge". Very common in item descriptions and that one training
  * "Concnetration" Misspelling of "Concentration", spotted in skill shop (US non-GH)
* Implement options:
  * Remove Red Capsule Requirements:
    * This would allow for more variety if I could pull it off. Part QoL. Not sure about logical implications
  * Level up rando:
    * *screams*
* Implement various trap ideas:
  * No Ki
    * This could be emptying the ki bar
    * This could be preventing charging up
  * Heal opponent
    * Probably just by 1 HP bar
  * Buff opponent
    * There are many kinds of buffs, Ed boy
      * It could be fun to let this be random
  * Scramble controls
  * Teleport player
    * In battle: 
* Implement various QOL changes:
  * Skip credits on first viewing (second viewing and onward, they can be skipped with Start)
  * Skip intro videos (*Atari noises*)
  * Set flags to make all DU playthroughs NG+
    * This has some logical implications and is planned to be a YAML option
  * Update some elements to be more friendly to colorblind people.
    * This means red dots on maps (and any more dots I may add)
    * This means the green text boxes for saving
    * Blue background for level up screen


## Known Bugs
Adding Broly's capsule and continuing his DU may load you into Goku's DU with messed up map markers and too low on the Z-axis to do anything.
- No idea what causes this. I may put more into fixing it if others encounter this issue.