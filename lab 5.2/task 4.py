def score_applicant(applicant):
    """
    Scores a job applicant based on education, experience, gender, and age.
    Returns a score out of 100.
    """
    score = 0

    # Education scoring
    education_levels = {
        "none": 0,
        "highschool": 10,
        "associate": 20,
        "bachelor": 30,
        "master": 40,
        "phd": 50
    }
    edu = applicant.get("education", "").lower()
    score += education_levels.get(edu, 0)

    # Experience scoring (up to 30 points)
    years_exp = applicant.get("experience", 0)
    if years_exp < 0:
        years_exp = 0
    score += min(years_exp * 3, 30)

    # Age scoring (prefer 22-60, up to 10 points)
    age = applicant.get("age", 0)
    if 22 <= age <= 60:
        score += 10
    elif 18 <= age < 22 or 61 <= age <= 70:
        score += 5
    # else: 0 points for age

    # Gender scoring (no bias, 0 points for all)
    # gender = applicant.get("gender", "").lower()
    # score += 0

    return min(score, 100)

def main():
    print("Job Applicant Scoring System")
    education = input("Enter education level (None, Highschool, Associate, Bachelor, Master, PhD): ").strip()
    try:
        experience = int(input("Enter years of experience: "))
    except ValueError:
        experience = 0
    gender = input("Enter gender: ").strip()
    try:
        age = int(input("Enter age: "))
    except ValueError:
        age = 0

    applicant = {
        "education": education,
        "experience": experience,
        "gender": gender,
        "age": age
    }

    score = score_applicant(applicant)
    print(f"Applicant Score: {score}/100")

if __name__ == "__main__":
    main()
