# Fing Agent API

**FingAgent** is a Python library for interfacing with the local APIs of the Fingbox. It allows you to easily interact with the devices and contacts managed by your Fingbox.

## Requirements

- Python 3.11.1 or higher
- [httpx](https://www.python-httpx.org/) (for asynchronous HTTP requests)

## Example

Here is a complete example of using the library:

```python
from fing_agent_api import FingAgent
import asyncio

async def main():
    # Configure the Fing agent
    agent = FingAgent(ip='your_agent_ip', port=49090, key='your_api_key')
        
    # Get devices
    devices = await agent.get_devices()
    
    # Get contacts (only available for desktops)
    contacts = await agent.get_contacts()
    
    # Get agent (only available for fingboxes and agents)
    agent_info = await agent.get_agent_info()


if __name__ == "__main__":
    asyncio.run(main())
```
