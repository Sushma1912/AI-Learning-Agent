def track_progress(learner):
    hours = learner["hours_studied"]

    if hours > 20:
        level = "🔥 Strong Progress"
    elif hours > 10:
        level = "📈 Moderate Progress"
    else:
        level = "⚠️ Low Progress"

    return f"""
📊 Progress Tracking

Hours Studied: {hours}
Level: {level}
"""
