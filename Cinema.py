from hackathon.Const import *

accessability = {
    "wheelchair": True,
    "vision": True,
    "hearing": True
}


def accessibility_type():
    if input(B_OWNER_QUESTION_CINEMA1_WHEELCHAIR) == 'no' or \
            input(B_OWNER_QUESTION_CINEMA2_WHEELCHAIR) == 'no' or \
            input(B_OWNER_QUESTION_CINEMA3_WHEELCHAIR) == 'no' or \
            input(B_OWNER_QUESTION_CINEMA5_WHEELCHAIR) == 'no' or \
            input(B_OWNER_QUESTION_CINEMA6_WHEELCHAIR) == 'no' or \
            input(B_OWNER_QUESTION_CINEMA8_WHEELCHAIR) == 'no' or \
            input(B_OWNER_QUESTION_CINEMA9_WHEELCHAIR) == 'no':
        accessability["wheelchair"] = False
    if input(B_OWNER_QUESTION_CINEMA4_VISION) == 'no':
        accessability["vision"] = False
    if input(B_OWNER_QUESTION_CINEMA7_HEARING) == 'no':
        accessability["hearing"] = False
    return accessability


print(accessibility_type())
