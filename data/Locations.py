from typing import NamedTuple, Optional, Callable, Dict
from ..Logic import *

class LocationData(NamedTuple):
    location_id: Optional[int]
    name: str
    access_rule: Optional[Callable[[CollectionState, int], bool]] = None
    checked_flag_address: Optional[Callable[["Addresses"], int]] = None
    enable_if: Optional[Callable[[Dict[str, Any]], bool]] = None
    is_vendor: bool = False


