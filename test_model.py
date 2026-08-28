from predict import predict_placement


def test_high_performing_student():

    result = predict_placement(
        8.5,
        92,
        85,
        4,
        1
    )

    assert result == " NOT PLACED"


def test_low_performing_student():

    result = predict_placement(
        5.8,
        60,
        45,
        1,
        0
    )

    assert result == "NOT PLACED"





