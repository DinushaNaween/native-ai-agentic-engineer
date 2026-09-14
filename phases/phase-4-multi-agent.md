# Phase 4 — Multi-Agent Systems & Swarms
**Duration**: Weeks 19–24 (Jan 18 – Feb 28, 2027)  
**Status**: 🔲 Not Started

> Orchestrate teams of specialized agents working in concert.

---

## 🎯 Learning Topics

### 1. Multi-Agent Patterns

#### Supervisor Pattern
- Central orchestrator routes tasks to worker agents
- Supervisor decides which agent to call next
- LangGraph implementation: supervisor node + worker nodes

#### Peer-to-Peer Pattern
- Agents communicate directly with each other
- No central coordinator
- Better for autonomous, decentralized behavior

#### Hierarchical Pattern
- Multiple levels of supervisors
- Top-level planner → mid-level coordinators → workers
- Scales to very complex tasks

#### Competitive Pattern
- Multiple agents produce solutions independently
- Best solution selected (voting, scoring)
- Great for creative tasks or quality checks

### 2. Agent Communication
- Message passing between agents
- Shared state management
- Event-driven communication
- Asynchronous vs synchronous coordination
- Avoiding deadlocks and race conditions

### 3. Agent Specialization
- **Planner Agent**: Breaks down goals into tasks
- **Researcher Agent**: Web search and information gathering
- **Coder Agent**: Writes and executes code
- **Critic/Reviewer Agent**: Reviews and improves output
- **Executor Agent**: Runs actions in the real world
- **Summarizer Agent**: Condenses information

### 4. Swarm Intelligence
- Emergent behavior from simple agent rules
- Consensus mechanisms (voting, averaging)
- Stigmergy — indirect coordination through environment
- Self-organizing systems
- Practical applications in AI

### 5. Orchestration Frameworks

#### CrewAI
- Role, goal, backstory for each agent
- Task dependencies and sequential/parallel execution
- Human input at task level
- Built-in tool sharing

#### AutoGen Group Chat
- Multi-agent conversations
- Agent selection strategies (auto, round-robin, custom)
- Code execution in group settings
- Termination conditions

#### LangGraph Multi-Agent
- Subgraphs for agent modularity
- Cross-graph communication
- Shared memory and state
- Conditional routing between agents

#### Google Antigravity SDK
- Production-grade multi-agent framework
- Subagent invocation and messaging
- Built-in parallelism
- Artifact and workspace management

### 6. Human-in-the-Loop (HITL)
- Interrupt handling in agent workflows
- Approval gates before irreversible actions
- Feedback injection mid-workflow
- LangGraph interrupt mechanism

### 7. Agent Observability & Debugging
- **LangSmith** — LangChain's tracing platform
- **Arize Phoenix** — open-source ML observability
- **Weights & Biases** — experiment tracking
- Logging agent decisions and tool calls
- Debugging multi-agent conversations
- Identifying bottlenecks in pipelines

### 8. Agent-to-Agent (A2A) Protocol (Google)
- Standard protocol for agent interoperability
- Agent cards — capability discovery
- Task management across agents
- Multimodal communication
- Why it matters for the AI ecosystem

### 9. Model Context Protocol (MCP) — Anthropic
- Standard for connecting LLMs to data sources/tools
- MCP servers (expose capabilities) vs clients (consume)
- Resources, tools, and prompts in MCP
- Building MCP servers
- Ecosystem of existing MCP servers

---

## 📚 Learning Resources

| Resource | Type | Priority | Link |
|----------|------|----------|------|
| CrewAI Documentation | Docs | ⭐⭐⭐ | https://docs.crewai.com |
| LangGraph Multi-Agent Tutorial | Docs | ⭐⭐⭐ | https://langchain-ai.github.io/langgraph/tutorials |
| AutoGen Multi-Agent | Docs | ⭐⭐⭐ | https://microsoft.github.io/autogen |
| Google A2A Protocol | Docs | ⭐⭐⭐ | https://google.github.io/A2A |
| Anthropic MCP Docs | Docs | ⭐⭐⭐ | https://modelcontextprotocol.io |
| DeepLearning.AI: Multi AI Agent Systems (CrewAI) | Course (Free) | ⭐⭐ | https://deeplearning.ai/short-courses |
| LangSmith Documentation | Docs | ⭐⭐ | https://docs.smith.langchain.com |

---

## 🏗️ Phase Project: Software Development Swarm

**What it does**: A full multi-agent pipeline that takes a feature request and produces working, tested, documented code.

**Agent Team**:
| Agent | Role | Tools |
|-------|------|-------|
| Product Manager | Writes user stories & acceptance criteria | None |
| Architect | Designs system architecture | None |
| Developer | Writes code | Python REPL, file system |
| Code Reviewer | Reviews for quality & bugs | None |
| Tester | Writes and runs tests | Python REPL |
| Documenter | Writes README & docs | File system |

**Location**: `projects/phase-4-dev-swarm/`  
**Tech Stack**: CrewAI or LangGraph, OpenAI GPT-4o, LangSmith

---

## 🏗️ Hands-On Exercises

- [ ] Build a supervisor + 3 worker agents pattern
- [ ] Implement a competitive agent pattern (3 agents, best answer wins)
- [ ] Add human-in-the-loop approval gate
- [ ] Build an MCP server exposing a custom tool
- [ ] Connect two agents using the A2A protocol
- [ ] Set up full LangSmith tracing for a multi-agent workflow

---

## ✅ Milestone Checkpoints

- [ ] Supervisor pattern: routes tasks to 3+ specialized agents correctly
- [ ] Human-in-the-loop: workflow pauses for human approval before destructive action
- [ ] Dev Swarm: feature request → working code, autonomously
- [ ] Full observability: every agent step traced in LangSmith
- [ ] Built and tested an MCP server

---

## 📝 LinkedIn Articles (This Phase)

### Article 14: "What Are AI Agent Swarms? (And Why They're the Future)"
**Draft**: `notes/articles/article-14-agent-swarms.md`  
**Post When**: Week 19

### Article 15: "I Built a 5-Agent Software Development Pipeline"
**Draft**: `notes/articles/article-15-dev-swarm.md`  
**Post When**: Week 22

### Article 16: "Google A2A vs Anthropic MCP — The Standards Battle for AI Agents"
**Draft**: `notes/articles/article-16-a2a-vs-mcp.md`  
**Post When**: Week 21

### Article 17: "Human-in-the-Loop AI: When to Let Humans Take the Wheel"
**Draft**: `notes/articles/article-17-hitl.md`  
**Post When**: Week 20

---

## 🔗 Key Papers

- [Communicative Agents for Software Development (ChatDev)](https://arxiv.org/abs/2307.07924)
- [AutoGen: Enabling Next-Gen LLM Applications](https://arxiv.org/abs/2308.08155)
- [AgentVerse: Facilitating Multi-Agent Collaboration](https://arxiv.org/abs/2308.10848)
- [CAMEL: Role-Playing Agents](https://arxiv.org/abs/2303.17760)
