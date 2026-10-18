
import os

import pandas as pd
import plotly.express as px
import streamlit as st
from dotenv import load_dotenv

from career_engine import recommend_careers, build_prompt, generate_gemini_advice


# Load private environment variables from .env
load_dotenv()

st.set_page_config(
    page_title="AI Career Advisor",
    page_icon="🧭",
    layout="wide",
)

st.markdown("""
<style>
.main {
    background: linear-gradient(
        180deg,
        rgba(90, 75, 190, 0.08),
        transparent 40%
    );
}
.hero {
    padding: 25px;
    border-radius: 16px;
    background: linear-gradient(120deg, #151a35, #5141a8);
    color: white;
}
.hero h1 { color: white; }
.hero p { color: #e5e7ff; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <h1>🧭 AI Career Advisor</h1>
    <p>Discover your next career move with Machine Learning and Gemini AI.</p>
</div>
""", unsafe_allow_html=True)

st.write("")
st.caption(
    "Explore career paths, discover skill gaps, and create a personalized "
    "learning roadmap."
)

with st.sidebar:
    st.header("👤 Your Career Profile")

    education = st.selectbox(
        "Education",
        [
            "High School",
            "Diploma",
            "Undergraduate",
            "Graduate",
            "Postgraduate",
            "Self-taught / Other",
        ],
    )

    experience = st.selectbox(
        "Experience",
        [
            "Student / Fresher",
            "0–2 years",
            "3–5 years",
            "6+ years",
        ],
    )

    skills_text = st.text_area(
        "Your skills",
        placeholder="Python, SQL, Machine Learning, Power BI",
        help="Separate skills with commas.",
    )

    interests_text = st.text_area(
        "Your interests",
        placeholder="Generative AI, data analysis, dashboards",
        help="Separate interests with commas.",
    )

    goal = st.selectbox(
        "Your career goal",
        [
            "Get my first job",
            "Switch careers",
            "Get promoted",
            "Build a portfolio",
            "Explore career options",
        ],
    )

    analyze = st.button(
        "✨ Analyze My Career",
        type="primary",
        use_container_width=True,
    )

if not analyze:
    st.subheader("🚀 What can this app do?")

    col1, col2, col3 = st.columns(3)
    col1.metric("Career paths", "8")
    col2.metric("Recommendation engine", "TF-IDF + similarity")
    col3.metric("AI career coach", "Gemini")

    st.info(
        "Enter your profile in the sidebar and click "
        "**Analyze My Career** to begin."
    )

    st.markdown("""
    ### Example profile

    - **Skills:** Python, SQL, Pandas, Machine Learning, Power BI
    - **Interests:** AI, data analysis, dashboards
    - **Goal:** Get my first job
    """)
    st.stop()

skills = [
    item.strip()
    for item in skills_text.replace("\n", ",").split(",")
    if item.strip()
]

interests = [
    item.strip()
    for item in interests_text.replace("\n", ",").split(",")
    if item.strip()
]

if not skills and not interests:
    st.warning("Please enter at least one skill or interest.")
    st.stop()

profile = {
    "education": education,
    "experience": experience,
    "skills": skills,
    "interests": interests,
    "goal": goal,
}

recommendations = recommend_careers(skills, interests)

if not recommendations:
    st.warning("No recommendations could be generated. Try entering more details.")
    st.stop()

st.subheader("🎯 Your Recommended Careers")

chart_data = pd.DataFrame([
    {
        "Career": item["career"],
        "Similarity score (%)": item["match_score"],
    }
    for item in recommendations
])

left, right = st.columns([1.4, 1])

with left:
    fig = px.bar(
        chart_data.sort_values("Similarity score (%)"),
        x="Similarity score (%)",
        y="Career",
        orientation="h",
        text="Similarity score (%)",
        range_x=[0, 100],
        title="Career Match Overview",
    )
    fig.update_traces(texttemplate="%{text:.1f}%", textposition="outside")
    fig.update_layout(
        height=380,
        xaxis_title="Similarity score (%)",
        yaxis_title="",
    )
    st.plotly_chart(fig, use_container_width=True)

with right:
    st.markdown("### 👤 Profile Summary")
    st.write(f"**Education:** {education}")
    st.write(f"**Experience:** {experience}")
    st.write(f"**Career goal:** {goal}")
    st.write("**Skills:** " + (", ".join(skills) or "Not provided"))
    st.write("**Interests:** " + (", ".join(interests) or "Not provided"))

st.caption(
    "Scores indicate text and skill similarity. They are not probabilities "
    "of getting hired or guarantees of suitability."
)

st.divider()
st.subheader("💼 Career Recommendations")

for number, item in enumerate(recommendations, start=1):
    with st.expander(
        f"{number}. {item['career']} — {item['match_score']:.1f}% similarity",
        expanded=(number == 1),
    ):
        st.write(item["description"])

        if item["matched_skills"]:
            st.markdown("**Skills you already listed that match**")
            st.write(", ".join(item["matched_skills"]))

        st.markdown("**Skills to consider learning**")
        if item["missing_skills"]:
            st.write(", ".join(item["missing_skills"]))
        else:
            st.success(
                "Your entered skills cover the skills listed for this role. "
                "Build projects to demonstrate your ability."
            )

st.divider()
st.subheader("🤖 Generate Your Personalized AI Career Plan")

st.write(
    "Gemini can use your profile and the recommendations above to create "
    "a learning roadmap, project ideas, and interview preparation plan."
)

if st.button("✨ Generate My AI Career Plan", type="primary"):
    api_key = os.getenv("GEMINI_API_KEY", "").strip()

    if not api_key or api_key == "PASTE_YOUR_ACTUAL_API_KEY_HERE":
        st.error(
            "Gemini API key not found. Add your key to the .env file "
            "in the project folder, then restart Streamlit."
        )
    else:
        prompt = build_prompt(profile, recommendations)

        with st.spinner("Gemini is creating your career plan..."):
            try:
                advice = generate_gemini_advice(prompt, api_key)
                st.markdown(advice)
            except Exception:
                st.error(
                    "Gemini could not generate the report. Check your API key, "
                    "internet connection, model access, and API quota. "
                    "If needed, review the terminal for diagnostic details."
                )
                with st.expander("Troubleshooting"):
                    st.write(
                        "Confirm that the key is valid, the Google API is "
                        "available to your project, and your account has "
                        "remaining quota. Restart the app after changing .env."
                    )

st.divider()
st.caption(
    "Built with Python, Scikit-learn, Streamlit, and Google Gemini. "
    "Use career suggestions as guidance, and verify current job requirements."
)
