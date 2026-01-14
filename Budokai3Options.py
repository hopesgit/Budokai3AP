from dataclasses import dataclass

from Options import (
    PerGameCommonOptions,
    Choice,
    Toggle,
    OptionSet,
    ItemSet
)
from .data.Items import DU_CHARACTERS_AS_DICT, DU_CHARACTER_NAMES


class StartWithStoryCharacters(Toggle):
    """
    Start with all story characters. Makes it easier to jump into your favorite Dragon World story.\n
    Adds Goku, Kid Gohan, Teen Gohan, Gohan, Piccolo, Vegeta, Krillin, Tien, Yamcha, Uub, and Broly to the starting items.
    """
    default = False
    display_name = "Start with Story Characters"


class RequireSuperAttacks(Choice):
    """Turn this on if you want to ensure that you have a special attack for a character before you can use them in Dragon World.\n
    For example, if you have Goku, you wouldn't be considered being able to use him until you acquire Kamehameha or Dragon Fist.

    NOTE: The starting capsule(s) in each Dragon Universe route will still be checkable with only the character, so be sure
    to start a route if you have the character! This does not apply to Kid Gohan, who has no starting items.

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
    Turn this on if you want to play with progressive character unlocks. For example, there are 11 Progressive Goku-s in the pool.
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

    NOTE: This ONLY applies to Dragon World characters. The rest work as normal. Tien, Yamcha, and Uub also only have
    one progressive items path because of a lack of transformations.

    Choices:\n
    - **off** - No progressive items for me, thanks.\n
    - **prog_normal** - Your progressive item progression is as described above.\n
    - **prog_attacks** - Your item progression will put attacks after the character.\n
    - **prog_transforms** - Your item progression will put transformations ahead of attacks.\n

    NOTE: Prioritizing transformations may mean that you won't be able to play Goku or Vegeta for some time if you also chose to require super attacks for your DW characters.
    """

    default = 0
    option_off = 0
    option_prog_normal = 1
    option_prog_attacks = 2
    option_prog_transforms = 3
    rich_text_doc = True
    display_name = "Progressive Characters"


class StartWithDragonRadar(Toggle):
    """
    Start with the Dragon Radar for each of your story routes (and adds its locations in each story to the location pool).
    """
    default = False
    display_name = "Start with Dragon Radar"
    visibility = False

# Additional Option ideas:
# Option that sets the flags for each DU route to be the second route 
#   This eliminates some backtracking (though notably, not all. Some routes have branching bosses, and those can't be planned around)
#   Will not be included in 0.1
# Option that removes requirements for red capsules
#   This would allow the player to use more moves. This would be relevant for Vegeta, Teen Gohan, Piccolo, Broly, Goku...
# Option that adds money spots in to the pool. This would allow for more locations, but makes it more difficult to make money in-game
# Option to implement special bonus rando, similar to Smash Bros Melee. Most aren't exactly relevant... So this is just an idea, mostly


class BallRando(Toggle):
    """
    Adds Dragon Balls for each story route to the item pool (and their locations to the location pool). Makes it so that 
    you can't get wish items without having all seven of that character's Dragon Balls.
    """
    display_name = "Dragon Ball Randomizer"
    default = False
    visibility = False


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


class Completionist(Toggle):
    """
    Set this to true to change your goal to 100% capsules. If there are more capsules than checks,
    then the remainder will be granted to you at the start of the game.
    """
    default = False
    display_name = "Completionist"
    visibility = False


@dataclass
class Budokai3Options(PerGameCommonOptions):
    start_with_story_characters: StartWithStoryCharacters
    require_super_attacks: RequireSuperAttacks
    super_attack_starters: SuperAttackStarters
    progressive_characters: ProgressiveCharacters
    start_with_dragon_radar: StartWithDragonRadar
    ball_rando: BallRando
    attack_rando: AttackRando
    shop_rando: ShopRando
    inspiration: Inspiration
    pandemic: Pandemic
    completionist: Completionist
