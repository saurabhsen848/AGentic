class ExecutionAgent:
    def execute_tasks(self, plan):
        completed = []
        print("[Execution Agent] Executing tasks...")

        for task in plan:
            if all(dep in completed for dep in task["dependencies"]):
                print(f"Executing: {task['name']}")
                completed.append(task["name"])
            else:
                print(f"Waiting for dependencies: {task['name']}")

        return completed
