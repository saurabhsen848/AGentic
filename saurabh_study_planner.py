# Intelligent Study Planner System Using Python
subjects = {
    "Python": [],
    "Discrete Maths": [],
    "Linear Algebra": ["Discrete Maths"],
    "DBMS": ["Discrete Maths"],
    "Machine Learning": ["Python", "Linear Algebra"]
}

visited = set()
study_plan = []

def plan_subject(subject):
    if subject not in visited:
        visited.add(subject)
        for prereq in subjects[subject]:
            plan_subject(prereq)
        study_plan.append(subject)

for subject in subjects:
    plan_subject(subject)

print("INTELLIGENT STUDY PLANNER SYSTEM")
for i, sub in enumerate(study_plan, 1):
    print(f"Level {i}: {sub}")
