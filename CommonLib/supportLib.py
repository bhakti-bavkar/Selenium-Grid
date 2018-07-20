import pytest


def check_element_visible(parent, locator, description='element'):
    try:
        return parent.find_element(locator[0], locator[1])
    except:
        pytest.fail('Exception occured while locating ' + description)



