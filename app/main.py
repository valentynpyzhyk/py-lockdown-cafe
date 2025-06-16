from app.errors import VaccineError, NotWearingMaskError
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_to_buy = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            # count friends not wearing a mask
            masks_to_buy += 1
    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"
    return f"Friends can go to {cafe.name}"
