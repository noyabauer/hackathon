import Const
def accessability_type():
    accessability = {
        "wheelchair": True,
        "vision": True,
        "hearing": True
    }
    if input(Const.B_OWNER_QUESTION_STORE1_WHEELCHAIR) == 'no' or\
            input(Const.B_OWNER_QUESTION_STORE2_WHEELCHAIR) == 'no' or\
            input(Const.B_OWNER_QUESTION_STORE4_WHEELCHAIR) == 'no' or\
            input(Const.B_OWNER_QUESTION_STORE5_WHEELCHAIR) == 'no' or\
            input(Const.B_OWNER_QUESTION_STORE6_WHEELCHAIR) == 'no' or\
            input(Const.B_OWNER_QUESTION_STORE7_WHEELCHAIR) == 'no':
        accessability["wheelchair"] = False
    if input(Const.B_OWNER_QUESTION_STORE3_VISION) == 'no':
        accessability["vision"] = False
    return accessability


print(accessability_type())
