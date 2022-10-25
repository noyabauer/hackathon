import Const
def accessability_type():
    accessability = {
        "wheelchair": True,
        "vision": True,
        "hearing": True
    }
    if input(Const.B_OWNER_QUESTION_RESTAURANT1_WHEELCHAIR) == 'no':
        accessability["wheelchair"] = False
    return accessability


print(accessability_type())