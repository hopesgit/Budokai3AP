from typing import TYPE_CHECKING

from NetUtils import NetworkItem
from . import ItemPool
from .TextManager import colorize_item_name
from .data import Items

if TYPE_CHECKING:
    from .Budokai3Client import Budokai3Context


## For Budokai 3:
## - process item
## - save to client queue
## - wait for player not in menu
## - use capsule spin function


def show_item_reception_message(ctx: 'Budokai3Context', item: NetworkItem, item_name: str = None, qty: int = 1):
    """
    Queues an in-game message which informs the player they received an item.

    :param ctx: The client context
    :param item: The NetworkItem that was received
    :param item_name: The name to use for the item (if unspecified, it is obtained from the NetworkItem)
    :param qty: The amount obtained
    """
    item_data = Items.from_id(item.item)
    item_classification = item.flags
    if item_name is None:
        item_name = ctx.item_names.lookup_in_slot(item.item, ctx.slot)
    if item.location < 0:
        # For some reason, starting items don't have their classification flags set properly
        item_classification = ItemPool.get_classification(item_data).as_flag()
    if qty > 1:
        item_name += f" x{qty}"
    item_name = colorize_item_name(item_name, item_classification)

    if item.location == -2:
        # This is a starting item, mention it in the message
        message = f"Received {item_name} (Starting Item)"
    elif qty > 1:
        # This is a group of packed collectables, don't indicate where they come from
        message = f"Received {item_name}"
    elif item.player == ctx.slot:
        # This is an item we found by ourselves
        message = f"Found {item_name}"
    else:
        # This is an item we received from someone
        player_name = ctx.player_names.get(item.player, "???")
        message = f"Received {item_name} from {player_name}"
    ctx.notification_manager.queue_notification(message)


async def handle_received_items(ctx: 'Budokai3Context', current_items: dict[str, int]):
    for network_item in ctx.items_received:
        item = Items.from_id(network_item.item)
        
        if item in Items.GRAY_CAPSULES:
            ctx.game_interface.give_system_capsule_to_player(item)
        elif item in [Items.ZENIE_2K, Items.ZENIE_5K, Items.ZENIE_10K, Items.ZENIE_25K, Items.ZENIE_100K]:
            ctx.game_interface.increment_money(item)
        elif item in Items.PROGRESSIVE_CAPSULES:
            prog_type = {
                1: "prog_normal",
                2: "prog_attacks",
                3: "prog_transforms"
            }
            item = Items.from_id(ItemPool.progressive_order(item, prog_type[ctx.slot_data["progressive_characters"]], current_items[item.name]))
        else:
            ctx.game_interface.give_capsule_to_player(item)

        print(f"Item Received: {item.name}")
        ctx.game_interface.give_capsule_to_player(item)
        