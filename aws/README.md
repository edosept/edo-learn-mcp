# Travel Agent

Strands Agents can use the MCP Client Tool available with Strands SDK to connect to external MCP Servers and dynamically load remote tools.

![strands_agentcore](https://github.com/edosept/edo-learn-mcp/blob/main/aws/images/strandsWithAgentCore.png)

The strands-travel-agent Lambda function will be the MCP Client that will make a call to the Attractions MCP Server that you will create using Agent Core Gateway. This MCP Server is secured using OAuth2 using Cognito. The Attractions Lambda function has various tools like List Attractions, Reserve Ticket, and Cancel ticket to allow you to use various methods that are defined depending on the tool that you need.

## Project Overview

This project consists of two main parts:

1.  **The Attractions MCP Server:**
    * An AWS Lambda function (`attractions`) holds the business logic for `list_attractions`, `reserve_ticket`, and `cancel_ticket`.
    * **Amazon Bedrock AgentCore Gateway** is placed in front of this Lambda, instantly turning it into a secure, discoverable server for agent tools.
    * **Amazon Cognito** is used to secure the gateway, requiring an OAuth2 token for access.

2.  **The Travel Agent Client:**
    * An AWS Lambda function (`strands-travel-agent`) acts as the main conversational agent.
    * It uses the **Strands SDK** and `MCPClient`.
    * Before running, it fetches an access token from Cognito.
    * It then connects to the `GATEWAY_URL`, authenticates, and dynamically loads the remote tools (`list_attractions`, etc.) to assist the user.

## Technology Used

* **Amazon Bedrock:** For the foundational agent model.
* **Amazon Bedrock AgentCore Gateway:** To create an MCP Server from a Lambda function.
* **AWS Lambda:** To host the agent logic (`strands-travel-agent`) and the tool logic (`attractions`).
* **Amazon Cognito:** For OAuth2 authentication (Client Credentials flow).
* **Amazon S3:** For storing agent chat session history.
* **Python**
* **Strands SDK**
