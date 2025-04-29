from fing_agent_api.fing_agent_api import FingAgent
import asyncio

async def main():
    try:
        fing = FingAgent("192.168.42.6", 49090, "CHIAVETEST")
        # device = await fing.get_devices()
        # print(device.network_id)
        agent_info = await fing.get_agent_info()
        print(agent_info.agent_id)
        print(agent_info.manufacturer)
        print(agent_info.state)
        print(agent_info.model_name)
        print(agent_info.device_type)
        print(agent_info.friendly_name)
        print(agent_info.ip)
    except Exception as e:
        print(e)

asyncio.run(main())    