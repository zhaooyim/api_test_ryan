"""
Description: this python module contains the tests about category rules.
Notes: a test function's name must start with 'test_'.
Author: Yimian Zhao
Date created: 15/06/2022
"""
import pytest
import helper_http
from helper_constants import PromotionNames


# Each item of the test data contains the target API URL and expected values for the details of interest;
# add more test data items to add more scenarios of the same test.
testdata_category_details = [
    ("https://api.tmsandbox.co.nz/v1/Categories/6327/Details.json?catalogue=false", 6327, "Carbon credits", True, [PromotionNames.GALLERY])
]


@pytest.mark.parametrize("url, category_id, category_name, can_relist, promotions", testdata_category_details)
def test_category_details(url, category_id, category_name, can_relist, promotions):
    actual_response_json = helper_http.send_request_get(url)

    assert (category_id == actual_response_json["CategoryId"])
    assert (category_name == actual_response_json["Name"])
    assert (can_relist == actual_response_json["CanRelist"])

    actual_promotions = actual_response_json["Promotions"]
    for promotion_name in promotions:
        actual_promotions_with_the_name = [item for item in actual_promotions if promotion_name == item["Name"]]

        # Verify the expected promotion(s) exists,
        assert (len(actual_promotions_with_the_name) > 0)

        # and it (or they, if not just one) has the correct description
        assert (all(PromotionNames.description[promotion_name] == item["Description"]
                    for item in actual_promotions_with_the_name))
