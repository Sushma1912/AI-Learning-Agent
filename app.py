import streamlit as st
from planner_agent import generate_study_plan
from assessment_agent import run_assessment
from tracker_agent import track_progress

st.set_page_config(page_title="AI Learning Agent", layout="centered")

st.title("🧠 AI Learning Agent System")
st.write("Multi-Agent AI that creates study plans, assessments, and tracks progress")

menu = st.sidebar.selectbox(
    "Choose Action",
    ["📘 Generate Study Plan", "🧪 Run Assessment", "📊 Track Progress"]
)

# ---------------- STUDY PLAN ----------------
if menu == "📘 Generate Study Plan":
    st.header("Study Plan Generator")

    role = st.text_input("Enter Role", "Cloud Engineer")
    cert = st.text_input("Enter Certification", "AZ-204")

    if st.button("Generate Plan"):
        result = generate_study_plan(role, cert)
        st.success("Study Plan Generated")
        st.write(result)

# ---------------- ASSESSMENT ----------------
elif menu == "🧪 Run Assessment":
    st.header("Assessment Agent")

    score = st.number_input("Enter Practice Score", 0, 100, 70)

    if st.button("Evaluate"):
        result = run_assessment(score)
        st.success("Assessment Completed")
        st.write(result)

# ---------------- TRACKER ----------------
elif menu == "📊 Track Progress":
    st.header("Progress Tracker")

    hours = st.number_input("Hours Studied", 0, 100, 10)

    if st.button("Track"):
        result = track_progress(hours)
        st.success("Progress Updated")
        st.write(result)
