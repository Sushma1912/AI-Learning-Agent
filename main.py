from planner_agent import create_plan
from assessment_agent import assess_learning
from tracker_agent import track_progress
import json

def load_data():
    with open("data/sample_data.json", "r") as f:
        return json.load(f)

def main():
    print("🚀 AI Learning Agent System Started\n")

    data = load_data()

    learner = data["learner"]

    print("📌 Generating Study Plan...\n")
    plan = create_plan(learner)
    print(plan)

    print("\n🧠 Running Assessment...\n")
    result = assess_learning(learner)
    print(result)

    print("\n📊 Tracking Progress...\n")
    progress = track_progress(learner)
    print(progress)

if __name__ == "__main__":
    main()
