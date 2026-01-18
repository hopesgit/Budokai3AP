from dataclasses import dataclass

from Options import (
    PerGameCommonOptions,
    Choice,
    Toggle,
    ItemSet,
    OptionDict
)
from .data.Items import DU_CHARACTERS_AS_DICT, DU_CHARACTER_NAMES


class Completionist(Toggle):
    """
    Set this to true to change your goal to 100% capsules. If there are more capsules than checks,
    then the remainder will be granted to you at the start of the game.
    """
    default = False
    display_name = "Completionist"
    visibility = False


class ChooseDUCharacters(OptionDict):
    """
    By default, all Dragon Universe stories are included in the location pool.\n
    If you want, you can reduce the pool of locations to only include certain stories.\n
    This is a more "sync-friendly" option.
    """
    option_goku = 0
    option_kid_gohan = 1
    option_teen_gohan = 2
    option_gohan = 3
    option_krillin = 4
    option_piccolo = 5
    option_vegeta = 6
    option_tien = 7
    option_yamcha = 8
    option_uub = 9
    option_broly = 10
    default = [0] # delete this later after more characters are added
    display_name = "Choose DU Characters"


class StartWithStoryCharacters(Toggle):
    """
    Start with all relevant story characters. Makes it easier to jump into your favorite Dragon Universe story.\n
    Adds all characters selected in "Choose DU Characters" to the starting items.\n
    If Progressive Characters is on, then the items given will be progressive items for those characters.
    """
    default = False
    display_name = "Start with Story Characters"


class RequireSuperAttacks(Choice):
    """Turn this on if you want to ensure that you have a special attack for a character before you can use them in Dragon Universe.\n
    For example, if you have Goku, you wouldn't be considered being able to use him until you acquire Kamehameha or Dragon Fist.

    NOTE: The starting capsule(s) and other first-saga items in each Dragon Universe route will still be checkable with only the character, 
    so be sure to start a route if you have the character! You may need to view a story event before some/any locations become available. 

    Choices:\n
    - **Off** - You don't want for the logic to consider whether you have any super attacks for a route to be playable.\n
    - **Random** - You do want for the logic to consider whether you have any super attacks, and you don't want to be given them.\n
    - **Plando/Vanilla** - A super move for each character will be in the capsules given at the beginning of his route.\n
    - **Start** - A random special move (->E or <-E) for each Dragon Universe story character when you first connect.\n
    - **Choose** - You choose who to start with a special attack for.\n
    You might want this if you want to be challenged with Goku, but not with Krillin, for example.\n
    NOTE: Plando is how the unmodified game works. Once you start a character's route, you are given a red capsule or two for that character.
    Except for Kid Gohan.\n
    """
    default = 0
    option_off = 0
    option_randomize = 1
    option_plando = 2
    alias_vanilla = 2
    option_start = 3
    option_choose = 4
    # option_expand = 5
    #     - **Expand** - Same as random, but include Ultimate and Dragon Rush moves.
    # I want to add the above option but it's not worth doing before reaching v0.1
    display_name = "Require Super Attacks"


class SuperAttackStarters(ItemSet):
    """List of character names whom you want to start with one of their super attacks (red capsules). Only has an effect
    if 'Start with Super Attacks' is 'choose'.\n
    Valid Choices: Goku, Kid Gohan, Teen Gohan, Gohan, Krillin, Piccolo, Tien, Yamcha, Vegeta, Uub, Broly"""
    options = DU_CHARACTERS_AS_DICT
    display_name = "Super Attack Starters"
    valid_keys = DU_CHARACTER_NAMES


class ProgressiveCharacters(Choice):
    """
    NOTE: This changes how "Start With Super Attacks' works. Instead of including the attack, a progressive item for that character will be included in the spots you choose.\n 
    Turn this on if you want to play with progressive character unlocks. For example, there are 14 Progressive Goku-s in the pool.
    Rather than receiving Goku and his moves separately, you can choose to receive them in a planned order.
    The order would be in roughly story order, but more specifically as follows:\n
    1) Goku (The character is always first)
    2) Kamehameha
    3) Kaioken
    4) Dragon Fist
    5) Spirit Bomb
    6) Super Saiyan
    7) Warp Kamehameha
    8) Super Saiyan 2
    9) Super Saiyan 3
    10) Super Saiyan 4
    11) Breakthrough (Breakthrough is always last, but fusions/potara will go after it if applicable)
    12) Fusion - Gogeta
    13) Fusion - Super Saiyan 4 Gogeta
    14) Potara - Vegito

    NOTE: This ONLY applies to Dragon Universe characters. The rest work as normal. Tien, Yamcha, and Uub also only have
    one progressive items path because of a lack of transformations.

    Choices:\n
    - **off** - No progressive items for me, thanks.\n
    - **prog_normal** - Your progressive item progression is as described above.\n
    - **prog_attacks** - Your item progression will put attacks after the character.\n
    - **prog_transforms** - Your item progression will put transformations ahead of attacks.\n

    NOTE: Prioritizing transformations may mean that you won't be able to play Goku or Vegeta for some time if you also chose to require super attacks for your Dragon Universe characters.
    """

    default = 0
    option_off = 0
    option_prog_normal = 1
    option_prog_attacks = 2
    option_prog_transforms = 3
    rich_text_doc = True
    display_name = "Progressive Characters"


class RandomizeDragonRadar(Choice):
    """
    Adds the Dragon Radar for each story route to the item pool (and adds its locations in each story to the location pool).\n
    Choices:\n
    * **off**: Dragon radars can continue to be picked up where they usually are.
    * **on**: Dragon radar items will be included in the item pool. The locations where they can be found will be randomized.
    * **start**: Dragon radars will always be available at the beginning of each story. The locations where they can be found will be randomized.
    """
    default = 0
    display_name = "Randomize Dragon Radar"
    option_off = 0
    option_on = 1
    option_start = 2


class RandomizeDragonBalls(Toggle):
    """
    Adds Dragon Balls for each story route to the item pool (and their locations to the location pool). Makes it so that 
    you can't get wish items without having all seven of that character's Dragon Balls.
    """
    display_name = "Randomize Dragon Balls"
    default = False


class RandomizeMoneySpots(Toggle):
    """
    Adds spots where you would usually gain money in Dragon Universe to the location pool.\n
    While this adds locations, money will likely be more tight in your seed, as you can only get it from
    the Archipelago server or World Tournament.
    """
    display_name = "Randomize Money Spots"
    default = False


class AttackRando(Toggle):
    """
    Randomize red capsule attacks (->E or <-E) between characters.\n
    DOES NOT INCLUDE: Ultimates, Dragon Rushes, transformations\n
    NOTE: This is an experimental option and may be removed.
    """
    display_name = "Attack Randomizer"
    default = False
    visibility=False


class ShopRando(Toggle):
    """
    Randomize shop slots into the location pool. Would otherwise be called "Shopsanity".
    """
    default = False
    display_name = "Shop Randomizer"


class Inspiration(Toggle):
    """
    Everyone's suddenly had a "breakthrough"...
    """
    default = False
    visibility=False
    display_name = "Inspiration"


class Pandemic(Toggle):
    """
    A rapidly-spreading infection has derailed the story! Can you survive if all your story mode bosses are equipped with
    the Viral Heart Disease effect?

    Viral Heart Disease causes a health drain to both fighters. It can be negated with the Vaccine item capsule,
    but you will need to use that capsule in every battle.
    """
    default = False
    visibility = False
    display_name = "Pandemic"


class ColorblindModeRed(Choice):
    """
    The menus in this game often use red, green, or blue.\n
    To improve readability and understandability for those with visual impairments, you can suggest replacement colors.\n
    This option only impacts what red can be turned into. Red is most prominently used in the following places: 
    * map markers in Dragon Universe
    * the scouter display of drained energy during hyper mode
    * the glow of the character who's in hyper mode
    * red capsules (they aren't visually distinct from green capsules)
    """
    default = 0
    option_red = 0
    option_yellow = 1
    option_purple = 2
    option_orange = 3
    option_pink = 4
    option_brown = 5
    visibility = False
    

class ColorblindModeGreen(Choice):
    """
    The menus in this game often use red, green, or blue.\n
    To improve readability and understandability for those with visual impairments, you can suggest replacement colors.\n
    This option only impacts what green can be turned into. Green is most prominently used in the following places: 
    * health bars in battle
    * many ground textures are green
    * the save menu background color
    * green capsules (they aren't visually distinct from red capsules)
    * green overlay while using Vegeta's scouter in DU
    """
    default = 0
    option_green = 0
    option_yellow = 1
    option_purple = 2
    option_orange = 3
    option_pink = 4
    option_brown = 5
    visibility = False


class ColorblindModeBlue(Choice):
    """
    The menus in this game often use red, green, or blue.\n
    To improve readability and understandability for those with visual impairments, you can suggest replacement colors.\n
    This option only impacts what blue can be turned into. Blue is most prominently used in the following places:
    - save prompt background
    - Battle results screen
    - level-up screen
    - in-battle scouter background color
    """
    default = 0
    option_blue = 0
    option_yellow = 1
    option_purple = 2
    option_orange = 3
    option_pink = 4
    option_brown = 5
    visibility = False


@dataclass
class Budokai3Options(PerGameCommonOptions):
    completionist: Completionist
    choose_du_characters: ChooseDUCharacters
    start_with_story_characters: StartWithStoryCharacters
    require_super_attacks: RequireSuperAttacks
    super_attack_starters: SuperAttackStarters
    progressive_characters: ProgressiveCharacters
    randomize_dragon_radar: RandomizeDragonRadar
    randomize_dragon_balls: RandomizeDragonBalls
    randomize_money_spots: RandomizeMoneySpots
    shop_rando: ShopRando
    attack_rando: AttackRando
    inspiration: Inspiration
    pandemic: Pandemic
    colorblind_mode_red: ColorblindModeRed
    colorblind_mode_blue: ColorblindModeBlue
    colorblind_mode_green: ColorblindModeGreen
