def build_scenario(agents, events):
    outcomes = []
    for event in events:
        for agent in agents:
            reaction = agent.evaluate_scenario([event])
            outcomes.extend(reaction)
    return outcomes

# Demo setup
if __name__ == "__main__":
    from agent_profile import Agent
    agent = Agent("BetaAgent", ["Cyberattack"], ["Preserve Stability"])
    print(build_scenario([agent], ["Cyberattack", "Market Crash"]))
