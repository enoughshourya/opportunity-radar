from uagents import Agent

from protocols import opportunity_protocol

agent = Agent()

agent.include(opportunity_protocol, publish_manifest=True)

if __name__ == "__main__":
    agent.run()
