def predict_result(marks):
    if marks >= 40:
        return "PASS"
    else:
        return "FAIL"


if __name__ == "__main__":
    marks = 75
    result = predict_result(marks)

    print("Marks:", marks)
    print("Prediction:", result)