
import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


CAREERS = [
    {
        "career": "Data Analyst",
        "description": "Analyze data, identify trends, and build business dashboards.",
        "skills": ["SQL", "Excel", "Python", "Power BI", "Statistics", "Data Visualization"],
        "interests": "data analysis reporting dashboards business insights",
    },
    {
        "career": "Data Scientist",
        "description": "Use statistics and machine learning to discover patterns and make predictions.",
        "skills": ["Python", "SQL", "Pandas", "NumPy", "Statistics", "Machine Learning"],
        "interests": "data science experiments predictive analytics research",
    },
    {
        "career": "Machine Learning Engineer",
        "description": "Build, test, deploy, and maintain machine learning models.",
        "skills": ["Python", "Machine Learning", "Scikit-learn", "SQL", "Git", "APIs"],
        "interests": "algorithms automation model deployment artificial intelligence",
    },
    {
        "career": "Generative AI Developer",
        "description": "Build applications using LLMs, prompts, APIs, and retrieval augmented generation.",
        "skills": ["Python", "LLM", "RAG", "Prompt Engineering", "APIs", "Streamlit"],
        "interests": "generative AI chatbots automation language models AI applications",
    },
    {
        "career": "NLP Engineer",
        "description": "Develop systems for text analysis, language understanding, and chatbots.",
        "skills": ["Python", "NLP", "Machine Learning", "Text Processing", "Deep Learning"],
        "interests": "natural language text analytics search sentiment analysis",
    },
    {
        "career": "Business Intelligence Developer",
        "description": "Build dashboards and data models to support business decisions.",
        "skills": ["SQL", "Power BI", "DAX", "Excel", "Data Modeling"],
        "interests": "business reporting KPIs visualization dashboards",
    },
    {
        "career": "Python Developer",
        "description": "Create software, automation scripts, backend services, and integrations.",
        "skills": ["Python", "SQL", "APIs", "Git", "Testing", "OOP"],
        "interests": "software development automation backend applications",
    },
    {
        "career": "Computer Vision Engineer",
        "description": "Build AI systems that understand images and video.",
        "skills": ["Python", "Deep Learning", "CNN", "OpenCV", "Machine Learning"],
        "interests": "image processing video recognition visual AI robotics",
    },
]


def normalize(text):
    """Normalize terms for forgiving skill matching."""
    return re.sub(r"[^a-z0-9+#. ]", "", text.lower()).strip()


def recommend_careers(skills, interests, top_n=5):
    """Rank career paths using TF-IDF similarity and skill overlap."""
    user_skills = [normalize(s) for s in skills if s.strip()]
    user_interests = [normalize(s) for s in interests if s.strip()]
    user_text = " ".join(user_skills + user_interests)

    if not user_text.strip():
        return []

    documents = []
    for career in CAREERS:
        documents.append(
            career["career"] + " "
            + career["description"] + " "
            + " ".join(career["skills"]) + " "
            + career["interests"]
        )

    vectorizer = TfidfVectorizer(
        stop_words="english",
        ngram_range=(1, 2)
    )
    matrix = vectorizer.fit_transform(documents + [user_text])
    similarities = cosine_similarity(matrix[-1], matrix[:-1]).flatten()

    results = []
    for index, career in enumerate(CAREERS):
        required = career["skills"]
        normalized_required = [normalize(s) for s in required]

        matched = []
        missing = []
        for original, required_norm in zip(required, normalized_required):
            found = any(
                required_norm == user_skill
                or required_norm in user_skill
                or user_skill in required_norm
                for user_skill in user_skills
                if len(user_skill) > 1
            )
            (matched if found else missing).append(original)

        coverage = len(matched) / max(len(required), 1)
        raw_score = 0.75 * float(similarities[index]) + 0.25 * coverage

        results.append({
            "career": career["career"],
            "description": career["description"],
            "required_skills": required,
            "matched_skills": matched,
            "missing_skills": missing,
            "match_score": round(raw_score * 100, 1),
        })

    return sorted(
        results,
        key=lambda result: result["match_score"],
        reverse=True
    )[:top_n]


def build_prompt(profile, recommendations):
    shortlist = "\n".join(
        f"- {r['career']}: {r['description']}. "
        f"Skills to develop: {', '.join(r['missing_skills']) or 'Build projects and deepen skills'}."
        for r in recommendations[:3]
    )

    return f"""
You are a practical and supportive AI career advisor.

Create a personalized career report using this profile:
- Education: {profile['education']}
- Experience: {profile['experience']}
- Skills: {', '.join(profile['skills']) or 'Not provided'}
- Interests: {', '.join(profile['interests']) or 'Not provided'}
- Career goal: {profile['goal']}

Machine-learning recommendations:
{shortlist}

Write the report in Markdown with these sections:
1. Best-fit career and explanation.
2. Two alternative career options.
3. Important skills to learn next.
4. A realistic 30-day learning plan divided into four weeks.
5. Three portfolio project ideas.
6. Interview preparation topics.
7. Five immediate next actions.

Treat matching scores as similarity indicators, not job probabilities.
Do not guarantee employment or salary. Be specific, realistic, and encouraging.
""".strip()


def generate_gemini_advice(prompt, api_key):
    """Generate a report using Google's Gemini API."""
    from google import genai

    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    if not response.text:
        raise RuntimeError("Gemini returned an empty response.")

    return response.text
