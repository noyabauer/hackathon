
import Const


def accessability_type():
    accessability = {
        "wheelchair": True,
        "vision": True,
        "hearing": True
    }
    if input(Const.B_OWNER_QUESTION_RESTAURANT1_WHEELCHAIR) == 'no' or input(Const.B_OWNER_QUESTION_RESTAURANT2_WHEELCHAIR) == 'no' or input(Const.B_OWNER_QUESTION_RESTAURANT5_WHEELCHAIR) == 'no' or input(Const.B_OWNER_QUESTION_RESTAURANT6_WHEELCHAIR) == 'no' or input(Const.B_OWNER_QUESTION_RESTAURANT7_WHEELCHAIR) == 'no':
        accessability["wheelchair"] = False
    if input(Const.B_OWNER_QUESTION_)
    return accessability


print(accessability_type())

B_OWNER_QUESTION_RESTAURANT1_WHEELCHAIR = "in case you have more than 1 floor,does your business have an elevator?(if you have 1 floor press 'yes')"
B_OWNER_QUESTION_RESTAURANT2_WHEELCHAIR = "does your door width equal or bigger than 80 cm?"
B_OWNER_QUESTION_RESTAURANT3_VISION = "does your door's business is transparent?"
B_OWNER_QUESTION_RESTAURANT4_VISION = "in case your door is transparent, do you have a colored sticker?(if your door isn't transparent press 'yes')"
B_OWNER_QUESTION_RESTAURANT5_WHEELCHAIR = "in case you have stairs in the entrance,do you have a ramp?(if you don't have stairs press 'yes')"
B_OWNER_QUESTION_RESTAURANT6_WHEELCHAIR = "do you have bathroom stalls for handicaps?"
B_OWNER_QUESTION_RESTAURANT7_WHEELCHAIR = "do you have handicaps parking near your business?"
B_OWNER_QUESTION_RESTAURANT8_WHEELCHAIR = "does your business's corridor width equal or bigger than 130 cm?"
B_OWNER_QUESTION_RESTAURANT9_VISION = "do you have a menu in Braille?"

