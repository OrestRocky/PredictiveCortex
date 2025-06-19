class Agent:
    def __init__(self, name, beliefs, goals, risk_tolerance=0.5):
        self.name = name
        self.beliefs = beliefs
        self.goals = goals
        self.risk_tolerance = risk_tolerance

    def evaluate_scenario(self, context):
        # Basic decision heuristic
        decisions = []
        for belief in self.beliefs:
            if belief in context:
                decisions.append(f"{self.name} activates response to belief: {belief}")
        return decisions

# Example usage
if __name__ == "__main__":
    a = Agent("AlphaAgent", ["Resource Scarcity", "Geopolitical Tension"], ["Protect Assets"])
    context = ["Geopolitical Tension", "Rising Inflation"]
    print(a.evaluate_scenario(context))
