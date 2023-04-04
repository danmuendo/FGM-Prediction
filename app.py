import streamlit as st 

from prediction import predict
import joblib
clf = joblib.load('rf_model.sav')
st.title('Predicting Population Vulnerable to Female Genital Mutilation and Rape ')
st.markdown('Predicting FGM vulnerability population')

def predict(age,gender,education,income,location,poverty,low_education,cultural_beliefs,exposure_to_violence,other_risk_factors):

    age = int(age)

    if gender == 'Male':
        GENDER = 1
    else:
        GENDER = 0
    if education == 'No education':
        EDUCATION = 0
    elif education == 'Primary':
        EDUCATION = 1
    elif education == 'Secondary':
        EDUCATION = 2
    else:
        EDUCATION = 3
    if income == 'Below poverty line':
        income = 0
    elif income == 'Above poverty line':
        income = 1
    
    if location == 'Rural':
        location = 0
    else:
        location = 1

    if poverty == 'High':
        poverty= 0
    elif poverty == 'Medium':
        poverty=1
    else:
        poverty=2

    if low_education == 'No':
        low_education = 0
    else:
        low_education=1

    if cultural_beliefs == 'Strong':
        cultural_beliefs=0
    elif cultural_beliefs == 'Moderate':
        cultural_beliefs=1
    else:
        cultural_beliefs=2

    if exposure_to_violence == 'High':
        exposure_to_violence=0
    elif exposure_to_violence == 'Medium':
        exposure_to_violence=1
    else:
        exposure_to_violence=2
    if other_risk_factors =='No':
        other_risk_factors=0
    else:
        other_risk_factors=1


     # Making predictions 
    prediction = clf.predict( [[GENDER, age, EDUCATION, income, location, poverty, low_education, cultural_beliefs, exposure_to_violence, other_risk_factors]])

    # set prediction whole number integer
    prediction = prediction.astype(int)

    return prediction
    
# Define the Streamlit app
def main():
    # Set the page title
    # st.set_page_config(page_title='FGM and Rape Prevention', page_icon=':guardsman:', layout='wide')

    # Define the sidebar
    st.sidebar.header('Input Parameters')
    age = st.sidebar.slider('Age', 1, 100, 18)
    gender = st.sidebar.selectbox('Gender', ['Male', 'Female'])
    education = st.sidebar.selectbox('Education', ['No education', 'Primary', 'Secondary', 'Tertiary'])
    income = st.sidebar.selectbox('Income', ['Below poverty line', 'Above poverty line'])
    location = st.sidebar.selectbox('Location', ['Urban', 'Rural'])
    poverty = st.sidebar.selectbox('Poverty', ['High', 'Medium', 'Low'])
    low_education = st.sidebar.selectbox('Low Education', ['Yes', 'No'])
    cultural_beliefs = st.sidebar.selectbox('Cultural Beliefs', ['Strong', 'Moderate', 'Weak'])
    exposure_to_violence = st.sidebar.selectbox('Exposure to Violence', ['High', 'Medium', 'Low'])
    other_risk_factors = st.sidebar.selectbox('Other Risk Factors', ['Yes', 'No'])


    # Make predictions using the model
    if st.sidebar.button('Predict'):
        result = predict(age,gender,education,income,location,poverty,low_education,cultural_beliefs,exposure_to_violence,other_risk_factors)
        st.success(f'The predicted outcome is {result[0]}')

    
if __name__ == '__main__':
    main()

