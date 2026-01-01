from dataclasses import dataclass

from Options import (
    PerGameCommonOptions,
    Choice,
    Toggle,
    OptionSet,
)
from .data.Items import DW_CHARACTER_NAMES


class StartWithStoryCharacters(Toggle):
    """
    Start with all story characters. Makes it easier to jump into your favorite Dragon World story.\n
    Adds Goku, Kid Gohan, Teen Gohan, Gohan, Piccolo, Vegeta, Krillin, Tien, Yamcha, Uub, and Broly to the starting items.
    """
    default = False
    display_name = "Start with Story Characters"


class StartWithSuperAttacks(Choice):
    """Turn this on if you want to ensure that you have a special attack for a character before you can use them in Dragon World.\n
    For example, if you have Goku, you wouldn't be considered being able to use him until you acquire Kamehameha or Dragon Fist.

    NOTE: The starting capsule(s) in each Dragon World route will still be checkable with only the character, so be sure
    to start a route if you have the character! This does not apply to Kid Gohan, who has no starting items.

    Choices:\n
    - **Off** - You don't want for the logic to consider whether you have any super attacks for a route to be playable.\n
    - **Random** - You do want for the logic to consider whether you have any super attacks, and you don't want to be given them.\n
    - **Plando** - A super move for your character will be in the starting items for the route.\n
    - **Start** - You will be given a random special move for each Dragon World story character when you first connect.\n
    - **Choose** - You choose who to start with a special attack for.\n
    You might want this if you want to be challenged with Goku, but not with Krillin, for example.\n
    NOTE: Plando is how the unmodified game works. Once you start a character's route, you are given a red capsule or two for that character.
    Except for Kid Gohan.\n
    """
    default = 0
    option_off = 0
    option_randomize = 1
    option_plando = 2
    option_start = 3
    option_choose = 4
    display_name = "Start with Super Attacks"


class SuperAttackStarters(OptionSet):
    """List of character names whom you want to start with one of their super attacks (red capsules). Only has an effect
    if 'Start with Super Attacks' is 'choose'."""
    options = DW_CHARACTER_NAMES
    display_name = "Super Attack Starters"


class ProgressiveCharacters(Choice):
    """
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
    11) Breakthrough (Breakthrough is always last)

    NOTE: This ONLY applies to Dragon World characters. The rest work as normal.

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
    Start with the Dragon Radar for each of your story routes.
    """
    default = True
    display_name = "Start with Dragon Radar"


class BallRando(Toggle):
    """
    Adds Dragon Balls for each story route to the item pool.
    """
    display_name = "Dragon Ball Randomizer"
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


@dataclass
class Budokai3Options(PerGameCommonOptions):
    start_with_story_characters: StartWithStoryCharacters
    start_with_super_attacks: StartWithSuperAttacks
    super_attack_starters: SuperAttackStarters
    progressive_characters: ProgressiveCharacters
    start_with_dragon_radar: StartWithDragonRadar
    ball_rando: BallRando
    attack_rando: AttackRando
    inspiration: Inspiration
    pandemic: Pandemic
    completionist: Completionist
