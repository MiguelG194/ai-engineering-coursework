
from pathlib import Path

import yaml
from smolagents import (
    CodeAgent,
    DuckDuckGoSearchTool,
    OpenAIServerModel,
    tool,
)
from tools.final_answer import FinalAnswerTool
from Gradio_UI import GradioUI


NETWORK_CONFIG = {
    "Ethernet": {
        "description": "Intel Ethernet Connection",
        "status": "Connected",
        "ipv4_address": "192.168.1.25",
        "subnet_mask": "255.255.255.0",
        "default_gateway": "192.168.1.1",
        "dns_servers": ["192.168.1.1", "8.8.8.8"],
    },
    "Wi-Fi": {
        "description": "Wireless Network Adapter",
        "status": "Disconnected",
        "ipv4_address": None,
        "subnet_mask": None,
        "default_gateway": None,
        "dns_servers": [],
    },
}

DNS_CONFIG = {
    "configured_dns_servers": ["192.168.1.50"],
    "expected_dns_servers": ["192.168.1.1", "8.8.8.8"],
}


@tool
def get_ethernet_configuration() -> str:
    """
    Return the simulated Ethernet IPv4 address, subnet mask,
    and default gateway.

    Use this tool to inspect Ethernet network settings.
    Returns plain text containing the configuration values.
    These values are simulated.
    """
    info = NETWORK_CONFIG["Ethernet"]

    return (
        f"IPv4 address: {info['ipv4_address']}\n"
        f"Subnet mask: {info['subnet_mask']}\n"
        f"Default gateway: {info['default_gateway']}"
    )


@tool
def get_dns_configuration() -> str:
    """
    Return the simulated DNS configuration.

    Use this tool to investigate DNS configuration problems
    or compare configured DNS servers with expected servers.

    Returns plain text containing the configured and expected
    DNS servers. These values are simulated.
    """
    configured = ", ".join(
        DNS_CONFIG["configured_dns_servers"]
    )
    expected = ", ".join(
        DNS_CONFIG["expected_dns_servers"]
    )

    return (
        f"Configured DNS servers: {configured}\n"
        f"Expected DNS servers: {expected}\n"
        "Note: These are simulated settings."
    )


@tool
def test_dns_resolution(hostname: str) -> str:
    """
    Simulate a DNS resolution test for a hostname.

    Args:
        hostname: The hostname to test, such as example.com.

    Returns a string describing the simulated test result.
    Use this tool when investigating whether a hostname
    can be resolved. This is not a real network test.
    """
    hostname = hostname.strip()

    if not hostname:
        return "Error: hostname cannot be empty."

    if hostname.lower() == "example.com":
        return (
            f"Hostname: {hostname}\n"
            "DNS resolution: FAILED\n"
            "Error: DNS server did not respond.\n"
            "This is a simulated test result."
        )

    return (
        f"Hostname: {hostname}\n"
        "DNS resolution: SUCCESSFUL\n"
        "Resolved IP address: 203.0.113.10\n"
        "This is a simulated test result."
    )


final_answer = FinalAnswerTool()

model = OpenAIServerModel(
    model_id="llama3.2:3b",
    api_base="http://localhost:11434/v1",
    api_key="ollama",
)

with open(
    Path(__file__).with_name("prompts.yaml"),
    "r",
    encoding="utf-8",
) as stream:
    prompt_templates = yaml.safe_load(stream)


agent = CodeAgent(
    model=model,
    tools=[
        final_answer,
        get_ethernet_configuration,
        get_dns_configuration,
        test_dns_resolution,
        DuckDuckGoSearchTool(),
    ],
    max_steps=6,
    verbosity_level=1,
    grammar=None,
    planning_interval=None,
    name=None,
    description=None,
    prompt_templates=prompt_templates,
)

GradioUI(agent).launch(inbrowser=True)
