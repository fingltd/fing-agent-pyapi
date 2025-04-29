from fing_agent_api.fing_agent_api import FingAgent
import asyncio

async def main():
    # Configure the Fing agent
    agent = FingAgent(ip='your_agent_ip', port=49090, key='your_api_key')
    
    # Get and print devices
    devices = await agent.get_devices()
    print("Devices:", devices)
    
    # Get and print contacts
    # contacts = await agent.get_contacts()
    # print("Contacts:", contacts)

    # agent_info = await agent.get_agent_info()
    # print("Agent Info:", agent_info)

if __name__ == "__main__":
    asyncio.run(main())