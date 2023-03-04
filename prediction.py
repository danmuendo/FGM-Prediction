import streamlit as st
# from prediction import predict

import joblib
def predict(data):
    clf = joblib.load('rf_model.sav')
    return clf.predict(data)
  # Make predictions using the model
    if st.sidebar.button('Predict'):
        result = predict(data)
        st.success(f'The predicted outcome is {result[0]}')



# git commit.
# git commit -a.
# git commit -m "commit message"
# git commit -am "commit message"
# git commit --amend.
# git add hello.py.