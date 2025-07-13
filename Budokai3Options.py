from Options import (
    DeathLink,
    StartInventoryPool,
    PerGameCommonOptions,
    Choice,
    DefaultOnToggle,
    Toggle,
    Range,
)
from dataclasses import dataclass


class StartWithStoryCharacters(Toggle):
    """
    Start with all story characters. Makes it easier to jump into your favorite Dragon world story.
    Adds Goku, Kid Gohan, Teen Gohan, Gohan, Piccolo, Vegeta, Krillin, Tien, Yamcha, Uub, and Broly to the starting items.
    """
    default = False


class StartWithSuperAttacks(Toggle):
    """
    Start with a random red capsule for each of your starting characters.
    """
    default = True


class StartWithDragonRadar(Toggle):
    """
    Start with the Dragon Radar for each of your story routes.
    """
    default = True


class BallSanity(Toggle):
    """
    Adds Dragon Balls for each story route to the item pool.
    """
    default = False


class AttackSanity(Toggle):
    """
    Randomize red capsule attacks (->E or <-E) between characters.
    DOES NOT INCLUDE: Ultimates, Dragon Rushes, transformations
    """
    default = False


class Inspiration(Toggle):
    """
    This APWorld's maintainer finds it more interesting if you don't know what this does.
    """
    default: False


class Pandemic(Toggle):
    """
    A rapidly-spreading infection has derailed the story! Can you survive if all your story mode bosses are equipped with
    the Viral Heart Disease effect?
    """
    default: False


@dataclass
class Budokai3Options(PerGameCommonOptions):
    start_with_story_characters = StartWithStoryCharacters
    start_with_super_attacks = StartWithSuperAttacks
    start_with_dragon_radar = StartWithDragonRadar
    ball_sanity = BallSanity
    attack_sanity = AttackSanity
    inspiration = Inspiration
    pandemic = Pandemic