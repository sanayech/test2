import pickle
import streamlit as st
from sklearn.ensemble import AdaBoostClassifier
import sklearn
from sklearn.preprocessing import LabelEncoder

# Load your trained model
with open('modelfinancial.pkl', 'rb') as model_file2:
    model = pickle.load(model_file2)
model_file2.close()

# Load your encoder model
with open('encoder.pkl', 'rb') as model_file3:
    model_le = pickle.load(model_file3 )
model_file3.close()


# Main Streamlit app
def main():
    st.title('Financial Inclusion Prediction')

    # Add input fields for features
    country = st.selectbox('country', ['Kenya', 'Rwanda' ,'Tanzania' ,'Uganda'])
    year  = st.selectbox('year', ['2018', '2016', '2017'])
    uniqueid = st.number_input('uniqueid')
    location_type = st.selectbox('location_type', ['Rural' ,'Urban'])
    cellphone_access= st.checkbox('cellphone_access')
    # If the checkbox is checked, set value to 0; otherwise, set value to 1
    cellphone_access= 0 if cellphone_access else 1
    household_size = st.number_input('household_size')
    age_of_respondent = st.number_input('age_of_respondent')
    gender_of_respondent =  st.selectbox(' gender_of_respondent ', ['Male', 'Female'])
    relationship_with_head = st.selectbox(' relationship_with_head ', ['Spouse', 'Head of Household' ,'Other relative', 'Child' ,'Parent', 'Other non-relatives'])
    marital_status = st.selectbox(' marital_status ', ['Married/Living together' , 'Widowed' , 'Single/Never Married', 'Divorced/Seperated', 'Dont know'])
    education_level = st.selectbox(' education_level ', ['Secondary education' ,'No formal education', 'Vocational/Specialised training' , 'Primary education','Tertiary education', 'Other/Dont know/RTA'])
    job_type=st.selectbox(' job_type ', ['Self employed','Government Dependent', 'Formally employed Private' ,'Informally employed' 'Formally employed Government' ,'Farming and Fishing', 'Remittance Dependent', 'Other Income' ,'Dont Know/Refuse to answer' ,'No Income'])

    # Validation button
    if st.button('Predict'):
        try:
            country = model_le.transform([[country]])[0] if country else None
        except:
            country = -1
        try:
            year = model_le.transform([[year]])[0] if year else None
        except:
            year = -1
        try:
            location_type = model_le.transform([[location_type]])[0] if location_type else None
        except:
            location_type = -1
        try:
            gender_of_respondent = model_le.transform([[gender_of_respondent]])[0] if gender_of_respondent else None
        except:
            gender_of_respondent = -1
        try:
            relationship_with_head = model_le.transform([[relationship_with_head]])[0] if relationship_with_head else None
        except:
            relationship_with_head = -1
        try:
            marital_status = model_le.transform([[marital_status]])[0] if marital_status else None
        except:
            marital_status = -1
        try:
            education_level = model_le.transform([[education_level]])[0] if education_level else None
        except:
            education_level = -1
        try:
            job_type = model_le.transform([[job_type]])[0] if job_type else None
        except:
            job_type = -1


        resultat=model.predict([[country,year,uniqueid,location_type ,cellphone_access,household_size,age_of_respondent ,gender_of_respondent,relationship_with_head,marital_status,education_level,job_type]])
        if resultat == 0:
            st.success(' Individual will open a bank account')
        else:
            st.warning('Individual will not open a bank account')

if __name__ == '__main__':
    main()

