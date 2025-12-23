from Options import (
    DeathLink,
    StartInventoryPool,
    PerGameCommonOptions,
    Choice,
    DefaultOnToggle,
    Toggle,
    Range,
    NamedRange,
    OptionSet
)

from .data.Items import DW_CHARACTER_NAMES
from dataclasses import dataclass


class StartWithStoryCharacters(Toggle):
    """
    Start with all story characters. Makes it easier to jump into your favorite Dragon World story.
    Adds Goku, Kid Gohan, Teen Gohan, Gohan, Piccolo, Vegeta, Krillin, Tien, Yamcha, Uub, and Broly to the starting items.
    """
    default = False


class StartWithSuperAttacks(Choice):
    """Turn this on if you want to ensure that you have a special attack for a character before you can use them in Dragon World.
    For example, if you have Goku, you wouldn't be considered being able to use him until you acquire Kamehameha or Dragon Fist.

    NOTE: The starting capsule(s) in each Dragon World route will still be checkable with only the character, so be sure
    to start a route if you have the character! This does not apply to Kid Gohan, who has no starting items.

    Choices:\n
    Off - You don't want for the logic to consider whether you have any super attacks for a route to be playable.\n
    Random - You do want for the logic to consider whether you have any super attacks, and you don't want to be given them.\n
    Plando - A super move for your character will be in the starting items for the route.\n
    NOTE: Plando is how the unmodified game works. Once you start a character's route, you are given a red capsule or two for that character.
    Except for Kid Gohan.\n
    Start - You will be given a random special move for each Dragon World story character when you first connect.\n
    Choose - You choose who to start with a special attack for.
    You might want this if you want to be challenged with Goku, but not with Krillin, for example.
    """
    default = 'off'
    choices = ['off', 'random', 'plando', 'start', 'choose']


class SuperAttackStarters(OptionSet):
    """List of character names whom you want to start with one of their super attacks (red capsules). Only has an effect
    if 'Start with Super Attacks' is 'choose'."""
    options = DW_CHARACTER_NAMES
    visibility = StartWithSuperAttacks.value is 'choose'


class ProgressiveCharacters(Choice):
    """
    Turn this on if you want to play with progressive character unlocks. For example, there are 11 Progressive Gokus in the pool.
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

    Choices:
    - off: No progressive items for me, thanks.
    - prog_normal: Your progressive item progression is as described above.
    - prog_attacks: Your item progression will put attacks after the character.
    - prog_transforms: Your item progression will put transformations ahead of attacks.

    NOTE: Prioritizing transformations may mean that you won't be able to play Goku or Vegeta for some time if you also chose to require super attacks for your DW characters.
    """
    choices = ['off', 'prog_normal', 'prog_attacks', "prog_transforms"]
    default = 'off'


class StartWithDragonRadar(Toggle):
    """
    Start with the Dragon Radar for each of your story routes.
    """
    default = True


class BallRando(Toggle):
    """
    Adds Dragon Balls for each story route to the item pool.
    """
    name = "Dragon Ball Randomizer"
    default = False


class AttackRando(Toggle):
    """
    Randomize red capsule attacks (->E or <-E) between characters.
    DOES NOT INCLUDE: Ultimates, Dragon Rushes, transformations
    NOTE: This is an experimental option and may be removed.
    """
    name = "Attack Randomizer"
    default = False


class Inspiration(Toggle):
    """
    Everyone's suddenly had a "breakthrough"...
    """
    default = False


class Pandemic(Toggle):
    """
    A rapidly-spreading infection has derailed the story! Can you survive if all your story mode bosses are equipped with
    the Viral Heart Disease effect?

    Viral Heart Disease causes a health drain to both fighters. It can be negated with the Vaccine item capsule,
    but you will need to use that capsule in every battle.
    """
    default = False


class Completionist(Toggle):
    """
    Set this to true to change your goal to 100% capsules. If there are more capsules than checks,
    then the remainder will be granted to you at the start of the game.
    """
    default = False


class ExpMultiplier(NamedRange):
    """
    It's a range, but it's flavored as "What kind of training would you like to do?"
    """
    range_start = 1
    range_end = 20
    special_range_names={
        "sparring": 1, # 1x
        "training": 2, # 2x
        "punch_machine": 3, # 3x
        "spaceship": 5, # 5x
        "time_chamber": 10, # 10x
        "champion": 15, # 15x
        "strongest": 20, # 20x
        "one_arm": -1 # this is half exp
    }
    default = 1


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
    exp_multiplier: ExpMultiplier