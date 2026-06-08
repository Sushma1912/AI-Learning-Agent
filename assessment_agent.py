def assess_learning(learner):
    score = learner["practice_score_avg"]

    if score >= 80:
        status = "🟢 Ready for Exam"
    elif score >= 60:
        status = "🟡 Needs Improvement"
    else:
        status = "🔴 Not Ready"

    return f"""
🧪 Assessment Result

Score: {score}
Status: {status}
"""
