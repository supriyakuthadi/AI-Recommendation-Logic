courses = {
    "Python Programming": ["programming", "coding", "technology"],
    "Java Development": ["programming", "software", "technology"],
    "Machine Learning": ["ai", "data", "technology"],
    "Data Science": ["ai", "data", "analytics"],
    "Graphic Design": ["design", "creativity", "art"],
    "UI/UX Design": ["design", "user experience", "creativity"],
    "Digital Marketing": ["marketing", "business", "analytics"]
}

print("=" * 50)
print("AI RECOMMENDATION SYSTEM")
print("=" * 50)

user_input = input("Enter your interests (comma-separated): ")

user_interests = [
    interest.strip().lower()
    for interest in user_input.split(",")
]

recommendations = []

for course, tags in courses.items():
    score = 0

    for interest in user_interests:
        if interest in tags:
            score += 1

    if score > 0:
        recommendations.append((course, score))

recommendations.sort(key=lambda x: x[1], reverse=True)

print("\nTop Recommendations")
print("-" * 50)

if recommendations:
    for course, score in recommendations:
        print(f"{course} | Match Score: {score}")
else:
    print("No suitable recommendations found.")