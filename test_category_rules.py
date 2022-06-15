"""
Description: this python module contains the tests about category rules.
Notes: a test function's name must start with 'test_'.
Author: Yimian Zhao
Date created: 15/06/2022
"""

import pytest
import helpers_http

testdata = [
    ("https://api.tmsandbox.co.nz/v1/Categories/6327/Details.json?catalogue=false", 6327, "Carbon credits", True)
]


@pytest.mark.parametrize("url, category_id, category_name, can_relist", testdata)
def test_promotion_gallery_has_good_position_in_category(url, category_id, category_name, can_relist):
    actual_response_json = helpers_http.send_request_get(url)

    assert(category_id == actual_response_json['CategoryId'])
    assert(category_name == actual_response_json['Name'])
    assert(can_relist == actual_response_json['CanRelist'])

    for element in actual_response_json['Promotions']:
        if element['Name'] == "Gallery":
            assert("Good position in category" in element['Description'])
