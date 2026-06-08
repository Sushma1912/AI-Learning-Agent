def create_plan(learner):
    role = learner["role"]
    cert = learner["certification"]

    plan = f"""
📘 Study Plan Generated

Role: {role}
Certification: {cert}

Day 1-3: Understand fundamentals
Day 4-7: Practice core skills
Day 8-10: Mock tests
Day 11: Revision

💡 Recommendation: Study 2 hours daily for best results
"""
    return plan
