"""
Description: this python module contains definitions of business constants
Author: Yimian Zhao
Date created: 16/06/2022
"""


class PromotionType:
    BASIC = "Basic"
    GALLERY = "Gallery"
    FEATURE = "Feature"

    descriptions = {
        BASIC: "Lowest position in category",
        GALLERY: "Good position in category",
        FEATURE: "Better position in category"
    }

    def __init__(self):
        raise NotImplementedError("{0} is not instantiable".format(self.__class__.__name__))
