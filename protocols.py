from uagents import Model, Protocol

class OpportunityQuery(Model):
    query: str
    user_tech_stack: str

class OpportunityResponse(Model):
    message: str

# Protocol definition for Opportunity Radar
opportunity_protocol = Protocol("OpportunityProtocol", version="1.0.0")
