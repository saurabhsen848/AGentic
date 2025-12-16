class PlanningAgent:
    def create_plan(self, tasks):
        print("[Planning Agent] Creating task plan...")
        return sorted(tasks, key=lambda x: x["priority"])
