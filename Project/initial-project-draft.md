## Section 1: Problem Statement

While working at a help desk position, technicians receive tickets about problems that users are experiencing. Network-related tickets can require multiple diagnostic commands before the root cause is identified. The purpose of this project is to create an AI agent that can analyze a network troubleshooting ticket, decide on an appropriate course of action, and perform available diagnostic actions. For example, the agent could be given access to commands for checking IP configurations, pinging an address, and performing DNS lookups. After receiving the results of a diagnostic, it could interpret them and decide which diagnostic to run next.

This could reduce the amount of manual troubleshooting that a help-desk technician has to perform for common network problems. Instead of manually running commands and determining what to check next, the technician could use the agent for the initial diagnostic process and provide a likely explanation.

An AI agent is useful for this task because the appropriate next action can depend on the results of previous commands. A simple script could run a fixed sequence of commands, but it would be less flexible when different problems produce different results. The agent would need to interpret the diagnostic results and reason about which action is appropriate next.

---

## Section 2: Target Users

The primary users of this agent would be help-desk technicians. When a ticket arrives, the agent could analyze the problem and perform an initial set of diagnostic actions to help determine the likely cause. This could save technicians time by handling basic troubleshooting that they would otherwise have to perform manually.

The agent would focus on diagnostics rather than making changes to network configurations, allowing the technician to remain responsible for deciding how the problem should ultimately be resolved. A technician would be more likely to use the agent again if it consistently provided useful diagnostic information and helped them reach the root cause more quickly. However, they would likely stop using it if it performed unnecessary commands, produced meaningless results, or repeatedly reached incorrect conclusions.

---

## Section 3: Candidate Approach

The initial approach will use an AI agent with prompting and access to network diagnostic tools. I have used Qwen models in previous assignments, so I am considering using a Qwen model for this project as well. Since Qwen has models with varying parameter sizes, I could potentially compare smaller and larger models to see how model capability affects the agent's performance.

The agent would use role-based prompting to establish that it is a help-desk network troubleshooting assistant. The prompt would explain its goal, available tools, and expected output. I would provide context explaining how the available networking tools work and when they should be used. For example, the agent could be given information about commands such as ipconfig, ping, and nslookup, along with examples of their output and what those results can indicate.

However, providing more context and examples also increases token usage. Since the agent may make multiple decisions during a troubleshooting session, sending a large amount of context with every request could become inefficient. I could investigate using RAG to retrieve only relevant information.

I think the hardest part of this project will be getting the agent to consistently choose appropriate diagnostic tools and to reach the correct conclusion from their results. The agent needs to understand both what information it has already gathered and what information it still needs before choosing its next action.

---

## Section 4: First-Draft Evaluation Plan

I will measure the agent's performance by looking at whether it chooses appropriate diagnostic tools and reaches the correct likely cause of the network problem. I will build a test set of simulated help-desk tickets covering common problems such as DNS failures, incorrect IP configurations, and connectivity issues. For each ticket, I will define the expected diagnosis and useful diagnostic steps before testing the agent.

For an initial success threshold, I would aim for the agent to reach the correct diagnosis on at least 80% of the test cases while generally choosing appropriate diagnostic commands. I will also measure unnecessary commands, since an agent that reaches the correct answer but performs many irrelevant diagnostics would not be very helpful.

One difficult part to measure will be the quality of the agent's troubleshooting process. Reaching the correct conclusion does not necessarily mean that it followed an efficient process, so I will also examine the sequence of tools it uses.
