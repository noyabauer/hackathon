
import Const


def accessability_type():
    accessability = {
        "wheelchair": True,
        "vision": True,
        "hearing": True
    }
    if input(Const.B_OWNER_QUESTION_RESTAURANT1_WHEELCHAIR) == 'no' or input(Const.B_OWNER_QUESTION_RESTAURANT2_WHEELCHAIR) == 'no' or input(Const.B_OWNER_QUESTION_RESTAURANT4_WHEELCHAIR) == 'no' or input(Const.B_OWNER_QUESTION_RESTAURANT5_WHEELCHAIR) == 'no' or input(Const.B_OWNER_QUESTION_RESTAURANT6_WHEELCHAIR) == 'no' or input(Const.B_OWNER_QUESTION_RESTAURANT7_WHEELCHAIR):
        accessability["wheelchair"] = False
    if input(Const.B_OWNER_QUESTION_RESTAURANRT3_VISION) == 'no' or input(Const.B_OWNER_QUESTION_RESTAURANT8_VISION) == 'no':
        accessability["vision"] = False
    return accessability


print(accessability_type())

