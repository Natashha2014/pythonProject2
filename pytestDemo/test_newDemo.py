import pytest

@pytest.mark.xfail
def test_first_creditcard():
    credit_card_type = "Visa"
    assert "Mastercard" == credit_card_type
    print(credit_card_type)


@pytest.mark.skip
def test_second_creditcard():
    credit_card_type = "Mastercard"
    assert "Visa" in credit_card_type
    print(credit_card_type)


@pytest.mark.smoke
def test_third_creditcard():
    creditcard_type = "Amex"
    print (creditcard_type)


@pytest.mark.smoke
def test_forth_creditcard():
    creditcard_type_new = "Discover"
    print(creditcard_type_new)