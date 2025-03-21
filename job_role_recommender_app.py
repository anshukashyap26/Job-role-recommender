import streamlit as st
import pandas as pd
from sklearn.metrics import jaccard_score
from sklearn.preprocessing import MultiLabelBinarizer

roles_skills = {
    "Data Scientist": {"Python", "Machine Learning", "Statistics", "SQL", "Data Visualization"},
    "Machine Learning Engineer": {"Python", "Machine Learning", "Deep Learning", "TensorFlow", "Data Structures"},
    "Data Analyst": {"SQL", "Excel", "Data Visualization", "Statistics", "Python"},
    "AI Researcher": {"Deep Learning", "Python", "PyTorch", "Mathematics", "NLP"},
    "Business Analyst": {"Excel", "SQL", "Data Visualization", "Business Intelligence", "Power BI"},
    "Software Engineer": {"Java", "Data Structures", "Algorithms", "System Design", "Databases"},
}

mlb = MultiLabelBinarizer()
skill_matrix = mlb.fit_transform(roles_skills.values())
skill_df = pd.DataFrame(skill_matrix, index=roles_skills.keys(), columns=mlb.classes_)

def recommend_roles(input_role):
    if input_role not in skill_df.index:
        return []
    input_vector = skill_df.loc[input_role].values
    similarities = []
    for role in skill_df.index:
        if role == input_role:
            continue
        sim = jaccard_score(input_vector, skill_df.loc[role].values)
        similarities.append((role, sim))
    similarities.sort(key=lambda x: x[1], reverse=True)
    return similarities[:3]

st.title("Job Role Recommendation Engine")
st.write("Select a job role to get the top 3 similar roles based on skill similarity.")
selected_role = st.selectbox("Choose a job role:", list(roles_skills.keys()))
if st.button("Recommend Similar Roles"):
    recommendations = recommend_roles(selected_role)
    st.write(f"### Top 3 recommendations for '{selected_role}':")
    for role, score in recommendations:
        st.write(f"- {role} (Similarity Score: {score:.2f})")
