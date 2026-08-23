import pickle


def predict_placement(
    cgpa,
    attendance,
    coding_score,
    projects,
    internship
):

    with open("model.pkl", "rb") as file:
        model = pickle.load(file)

    student = [[
        cgpa,
        attendance,
        coding_score,
        projects,
        internship
    ]]

    prediction = model.predict(student)

    if prediction[0] == 1:
        return "PLACED"
    else:
        return "NOT PLACED"


if __name__ == "__main__":

    result = predict_placement(
        8.2,
        90,
        80,
        3,
        1
    )

    print("Predicted Placement:", result)