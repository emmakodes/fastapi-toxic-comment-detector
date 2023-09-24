import pickle
from . import schemas


def check_toxicity(comment: schemas.Comment):
    comment_dictionary = {}
    comment_dictionary['comment_key'] = [comment.comments]

    # load the vectorizer and vectorize comment
    vectorizer = pickle.load(open("./Vectorize.pickle", "rb"))
    testing = vectorizer.transform(comment_dictionary['comment_key'])

    # load the model
    with open('./Pickle_LR_Model.pkl', 'rb') as file:
        lr_model = pickle.load(file)

    # predict toxicity. prediction range from 0.0 to 1.0 (0.0 = non-toxic and 1.0 toxic)
    prediction = lr_model.predict_proba(testing)[:, 1]
    prediction = float(prediction)

    if prediction >= 0.9 and prediction <= 1.0:
        response_list = ["toxic comment", prediction]
        return {"response": response_list}

    elif prediction >= 0.0 and prediction <= 0.1:
        response_list = ["non toxic comment", prediction]
        return {"response": response_list}

    else:
        response_list = ["Manually check this", prediction]
        return {"response": response_list}
