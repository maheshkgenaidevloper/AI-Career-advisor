# AI-Career-advisor
 <div align="center">

# 🧭 AI CAREER ADVISOR

### ✨ Discover Your Potential. Build Your Future. Get Career-Ready.

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=24&duration=3000&pause=800&color=9B8CFF&center=true&vCenter=true&width=750&lines=Your+Personal+AI+Career+Coach;Powered+by+Machine+Learning+%26+Gemini+AI;Discover+Skills.+Explore+Careers.+Grow+Faster." alt="Animated typing banner" />

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit" />
  <img src="https://img.shields.io/badge/Google-Gemini%20AI-4285F4?style=for-the-badge&logo=google&logoColor=white" alt="Gemini AI" />
  <img src="https://img.shields.io/badge/Machine-Learning-8A2BE2?style=for-the-badge" alt="Machine Learning" />
  <img src="https://img.shields.io/badge/Status-Active-22C55E?style=for-the-badge" alt="Project status" />
</p>

**An intelligent career guidance application that transforms your skills and interests into personalized career recommendations, skill-gap insights, and actionable learning roadmaps.**

</div>

---

## 🌌 Welcome to Your Future

Choosing the right career can be confusing. **AI Career Advisor** helps you explore suitable career paths using Machine Learning and Generative AI.

Enter your skills, education, experience, interests, and career goals. The application ranks career options and uses Google's Gemini API to generate personalized guidance.

<div align="center">

<img src="https://media.giphy.com/media/L8K62iTDkzGX6/giphy.gif" width="320" alt="Animated technology and coding GIF" />

### 💡 From Skills to Strategy. From Learning to Opportunity.

</div>

## 🚀 What Makes This Project Special?

<table>
<tr>
<td width="50%" valign="top">

### 🧠 Intelligent Career Matching

Uses TF-IDF vectorization and cosine similarity to rank careers based on your profile.

### 🎯 Skill-Gap Analysis

Highlights skills you already have and identifies additional skills to learn for selected roles.

### 🤖 Gemini AI Career Coach

Generates personalized career guidance, project ideas, and a structured learning roadmap.

</td>
<td width="50%" valign="top">

### 📊 Interactive Analytics

Explore career-fit scores through interactive Plotly charts.

### 🗺️ Learning Roadmap

Get a practical 30-day plan with weekly learning goals and suggested portfolio projects.

### 🔐 API-Key Protection

Keeps your Gemini API key in a local environment file instead of hardcoding it into Python.

</td>
</tr>
</table>

---

## ⚡ How It Works

<div align="center">

| Step | Process | Outcome |
|:---:|---|---|
| 01 | 👤 Enter Your Profile | Skills, education, experience, interests |
| 02 | 🧠 Machine Learning Analysis | Career similarity ranking |
| 03 | 🔍 Identify Skill Gaps | Skills to improve for each role |
| 04 | ✨ Gemini AI Generation | Personalized career guidance |
| 05 | 📈 Explore Your Results | Career recommendations and learning roadmap |

</div>

## 🛠️ Technology Stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=python,git,github,vscode" alt="Technology icons" />
</p>

| Technology | Role in the Project |
|---|---|
| Python | Core application logic |
| Pandas | Data preparation and manipulation |
| Scikit-learn | TF-IDF and cosine similarity |
| Google Gemini API | Generative AI career guidance |
| Streamlit | Interactive web application |
| Plotly | Career-match visualizations |
| python-dotenv | Secure local environment configuration |
| Git & GitHub | Version control and project hosting |

---

## 🖥️ Application Preview

> Add screenshots of your actual running application here after testing it locally.

<div align="center">

| Career Dashboard | AI Career Report |
|---|---|
| Add `screenshots/dashboard.png` | Add `screenshots/career-report.png` |
| Career match charts and profile summary | Learning plan, project ideas, and skill gaps |

</div>

You can also add a short screen recording or an optimized GIF of your running application to demonstrate its functionality to recruiters.

---

## 📂 Project Structure

```text
AI_Career_Advisor/
│
├── app.py                  # Streamlit application
├── career_engine.py        # ML recommendations and Gemini integration
├── requirements.txt        # Python dependencies
├── .env                    # Private API key - never upload
├── .env.example            # Safe API-key template, if included
├── .gitignore              # Excludes secrets and temporary files
├── README.md               # Project documentation
│
└── screenshots/            # Optional application screenshots
```

---

## ⚙️ Installation Guide

### 1️⃣ Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/AI_Career_Advisor.git
cd AI_Career_Advisor
```

Replace `YOUR_USERNAME` with your GitHub username.

### 2️⃣ Create a virtual environment

**Windows:**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, use Command Prompt:

```bat
.venv\Scripts\activate.bat
```

### 3️⃣ Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4️⃣ Configure your Gemini API key

Generate your key through the official Google AI Studio page:

🔗 **[Get Your Gemini API Key](https://aistudio.google.com/app/apikey)**

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_actual_gemini_api_key
```

Replace the placeholder with your own key.

**Security checklist:**

- Never commit `.env` to GitHub.
- Add `.env` to `.gitignore`.
- Do not publish your key in screenshots or documentation.
- If your key is exposed, revoke it and create a replacement.

### 5️⃣ Launch the application

```bash
python -m streamlit run app.py
```

Open the local URL displayed in your terminal, typically:

`http://localhost:8501`

---

## 🎯 Example User Profile

```text
Education       : Undergraduate
Experience      : Student / Fresher

Skills          : Python, SQL, Pandas,
                  Machine Learning, Power BI

Interests       : Artificial Intelligence,
                  Data Analysis, Dashboards

Career Goal     : Get My First Job
```

### Expected Results

The application may recommend career paths such as:

- 📊 Data Analyst
- 📈 Data Scientist
- 🤖 Machine Learning Engineer
- ✨ Generative AI Developer
- 🗣️ NLP Engineer
- 💻 Python Developer
- 📉 Business Intelligence Developer
- 👁️ Computer Vision Engineer

Recommendations depend on the profile entered and the career dataset. Scores represent relative similarity, not probabilities of employment.

---

## 🧬 Machine Learning Behind the Project

The recommendation engine follows these steps:

1. **Text preparation:** combines career descriptions, skills, and interests.
2. **TF-IDF vectorization:** converts profile text and career descriptions into numerical features.
3. **Cosine similarity:** estimates how closely the profile matches each career.
4. **Skill-overlap calculation:** compares entered skills with the required-skill lists.
5. **Career ranking:** combines similarity and skill coverage to produce ranked recommendations.
6. **Generative AI:** Gemini uses the profile and recommended roles to create a personalized report.

### 📐 Recommendation Score

The current implementation uses:

```text
Recommendation Score =
    75% × Text Similarity
  + 25% × Required-Skill Coverage
```

This is a heuristic ranking formula for an educational project, not a validated hiring prediction model.

---

## 🌱 Future Enhancements

- [ ] 📄 Resume PDF upload and skill extraction
- [ ] 🔎 Job-description and resume matching
- [ ] 🎓 Course and certification recommendations
- [ ] 🧪 Career-specific interview question generation
- [ ] 📥 Downloadable PDF career reports
- [ ] 🌐 Live job listings through authorized APIs
- [ ] 👤 Optional user profiles and saved career plans
- [ ] ☁️ Cloud deployment
- [ ] 🧪 Automated unit tests and recommendation evaluation

---

## ☁️ Deployment

The project can be adapted for hosting on Streamlit Community Cloud or another Python-compatible platform.

For deployment:

1. Push the project source code to GitHub.
2. Connect the repository to your chosen hosting service.
3. Configure `GEMINI_API_KEY` in the platform's secrets or environment-variable settings.
4. Set `app.py` as the application entry point.
5. Deploy and test the application.

Never upload the actual `.env` file to a public repository.

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome!

```bash
git checkout -b feature/new-feature
git add .
git commit -m "Add a new career advisor feature"
git push origin feature/new-feature
```

Then open a pull request on GitHub.

---

## ⚠️ Disclaimer

This is an educational portfolio project. Its career recommendations are informational and depend on the quality of the input profile and sample dataset. They do not guarantee employment, salary, or career success. Verify role requirements using current job listings and trusted professional guidance.

---

## 👨‍💻 Author

<div align="center">

### Built with 💜 and Python

**AI Career Advisor — Your Next Career Move Starts Here.**

<a href="https://github.com/maheshkgenaidevloper">
  <img src="https://img.shields.io/badge/GitHub-Visit%20My%20Profile-181717?style=for-the-badge&logo=github" alt="Visit GitHub profile" />
</a>

⭐ **If you find this project useful, give the repository a star!**

<img src="https://capsule-render.vercel.app/api?type=waving&color=6C5CE7&height=100&section=footer" width="100%" alt="Purple animated-style footer banner" />

</div>
