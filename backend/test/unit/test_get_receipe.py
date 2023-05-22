import pytest
import unittest.mock as mock
from unittest.mock import patch
from src.controllers.receipecontroller import ReceipeController
from src.static.diets import Diet

receipe = {
    "diets": [
        "normal", "vegetarian"
    ]
}

available_items = {}

diet1 = Diet.NORMAL

diet2 = Diet.VEGAN

# add your test case implementation here
@pytest.mark.unit
def test_get_receipe_readiness_1():
    mockedDao = mock.MagicMock()
    sut = ReceipeController(mockedDao)
    with patch('src.controllers.receipecontroller.calculate_readiness', return_value = 0.09):
       readiness =  sut.get_readiness_of_receipes(receipe, {}, diet1)
    assert readiness is None

@pytest.mark.unit
def test_get_receipe_readiness_2():
    mockedDao = mock.MagicMock()
    sut = ReceipeController(mockedDao)
    with patch('src.controllers.receipecontroller.calculate_readiness', return_value = 0.11):
       readiness =  sut.get_readiness_of_receipes(receipe, {}, diet1)
    assert readiness == 0.11

@pytest.mark.unit
def test_get_receipe_readiness_3():
    mockedDao = mock.MagicMock()
    sut = ReceipeController(mockedDao)
    with patch('src.controllers.receipecontroller.calculate_readiness', return_value = 0.1):
       readiness =  sut.get_readiness_of_receipes(receipe, {}, diet1)
    assert readiness == 0.1

@pytest.mark.unit
def test_get_receipe_readiness_4():
    mockedDao = mock.MagicMock()
    sut = ReceipeController(mockedDao)
    with patch('src.controllers.receipecontroller.calculate_readiness', return_value = 0.1):
       readiness =  sut.get_readiness_of_receipes(receipe, {}, diet2)
    assert readiness == None
