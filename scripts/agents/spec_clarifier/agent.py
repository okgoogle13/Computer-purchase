import json
from pydantic import BaseModel, Field
from google.adk.agents import Agent
from google.adk.tools import FunctionTool

from .prompt import spec_clarifier_prompt

class SpecRequirements(BaseModel):
    track_preference: str = Field(description='One of "1A", "1B", "1.5", "2", or "Any"')
    vram_floor_gb: float = Field(description='Minimum required VRAM/Unified memory in GB')
    budget_cap_aud: float = Field(description='Maximum budget in AUD')
    portability_requirement: str = Field(description='One of "Laptop", "Desktop", "Mini PC", or "Any"')
    au_stock_urgency: bool = Field(description='True if immediate AU stock is required, False otherwise')

def finalize_requirements(requirements: SpecRequirements) -> str:
    """
    Call this tool ONLY when you have gathered all the necessary information
    from the user to finalize their hardware specifications.
    """
    req_dict = requirements.model_dump()
    print("\n--- FINALIZED REQUIREMENTS ---")
    print(json.dumps(req_dict, indent=2))
    print("------------------------------\n")
    # By returning a specific string, we can signal the caller to stop or save the file.
    return f"Requirements finalized:\n{json.dumps(req_dict)}"

root_agent = Agent(
    model="gemini-2.5-flash",
    name="spec_clarifier_agent",
    instruction=spec_clarifier_prompt,
    tools=[
        FunctionTool(
            func=finalize_requirements,
        )
    ]
)

if __name__ == "__main__":
    print("Starting Spec Clarifier Agent. Type 'exit' to quit.")
    # Simple CLI loop for testing
    while True:
        try:
            user_input = input("\nYou: ")
            if user_input.lower() in ['exit', 'quit']:
                break
            
            # Simple stateless call for demonstration (adk web would maintain state)
            # In a real CLI loop, you'd maintain memory. But for a quick test, we can use a session.
            # Here we just rely on ADK's native `__call__` or session mechanics.
            response = root_agent(user_input)
            print(f"\nAgent: {response.text}")
            
        except KeyboardInterrupt:
            break
