# Phase 3 — Agentic AI Fundamentals
**Duration**: Weeks 13–18 (Dec 7, 2026 – Jan 17, 2027)  
**Status**: 🔲 Not Started

> Agents that perceive, plan, and act. The heart of agentic engineering.

---

## 🎯 Learning Topics

### 1. What is an AI Agent?
- Definition: LLM + Tools + Memory + Planning
- Difference between a chatbot and an agent
- The agent loop: Observe → Think → Act → Observe
- When to use agents (and when NOT to)

### 2. Agent Architectures

#### ReAct (Reasoning + Acting)
- Interleave reasoning traces with actions
- How the loop works step by step
- Implementation from scratch
- Paper: "ReAct: Synergizing Reasoning and Acting in Language Models"

#### Plan-and-Execute
- Planner creates a plan upfront
- Executor runs each step
- Better for complex multi-step tasks

#### Reflexion
- Agent reflects on its failures
- Generates verbal reinforcement signals
- Self-improvement loop

#### MRKL Systems
- Modular Reasoning, Knowledge, and Language
- Routing queries to specialized modules

### 3. Tool Use
- Web search (Tavily, SerpAPI)
- Code execution (Python REPL, sandboxed environments)
- File system operations
- Database queries
- External APIs (weather, calendar, email)
- Browser automation

### 4. Memory Systems
- **Short-term memory**: in-context window (conversation history)
- **Long-term memory**: vector store (persistent across sessions)
- **Episodic memory**: past experiences and their outcomes
- **Semantic memory**: facts and knowledge
- Memory management: what to store, when to retrieve

### 5. Planning & Task Decomposition
- Breaking down complex goals into sub-tasks
- Hierarchical planning
- Handling dependencies between tasks
- Replanning when things go wrong

### 6. Agent Frameworks

#### LangGraph
- State machine approach to agents
- Nodes (actions) + Edges (transitions) + State
- Conditional edges for branching logic
- Streaming support
- Best for complex, stateful workflows

#### AutoGen (Microsoft)
- Conversation-based multi-agent
- Agent roles and capabilities
- Human-in-the-loop integration
- Code execution agents

#### CrewAI
- Role-based agent teams
- Tasks and crew orchestration
- Sequential and parallel execution

#### Phidata
- Lightweight agent framework
- Built-in tools and memory

### 7. Agent Safety & Guardrails
- Prompt injection attacks — what they are and how to prevent
- Output validation (Pydantic, Guardrails AI)
- Hallucination detection
- Rate limiting and cost controls
- Sandboxed code execution
- Human approval gates for irreversible actions

---

## 📚 Learning Resources

| Resource | Type | Priority | Link |
|----------|------|----------|------|
| LangGraph Documentation | Docs | ⭐⭐⭐ | https://langchain-ai.github.io/langgraph |
| Andrew Ng: AI Agentic Design Patterns (AutoGen) | Course (Free) | ⭐⭐⭐ | https://deeplearning.ai/short-courses |
| Lilian Weng: LLM-Powered Autonomous Agents | Blog | ⭐⭐⭐ | https://lilianweng.github.io/posts/2023-06-23-agent |
| AutoGen Documentation | Docs | ⭐⭐⭐ | https://microsoft.github.io/autogen |
| CrewAI Documentation | Docs | ⭐⭐ | https://docs.crewai.com |
| DeepLearning.AI: Functions, Tools and Agents | Course (Free) | ⭐⭐ | https://deeplearning.ai/short-courses |
| Hugging Face Agents Course | Course (Free) | ⭐⭐ | https://huggingface.co/learn/agents-course |

---

## 🏗️ Phase Project: Research Assistant Agent

**What it does**: An agent that autonomously researches a topic, searches the web, reads multiple sources, and writes a comprehensive report.

**Agent capabilities**:
- [ ] Web search (Tavily API)
- [ ] Read and summarize web pages
- [ ] Take structured notes
- [ ] Identify gaps in research
- [ ] Generate final markdown report
- [ ] Cite all sources

**Architecture**: LangGraph state machine  
**Location**: `projects/phase-3-research-agent/`

**Tech Stack**: Python, LangGraph, Tavily, OpenAI GPT-4o, Pydantic

---

## 🏗️ Hands-On Exercises

- [ ] Build a ReAct agent from scratch (no framework) with 3 tools
- [ ] Build the same agent with LangGraph
- [ ] Add persistent long-term memory using ChromaDB
- [ ] Implement an agent that can write and execute Python code
- [ ] Add guardrails to prevent prompt injection
- [ ] Compare LangGraph vs AutoGen for the same task

---

## ✅ Milestone Checkpoints

- [ ] Built a ReAct agent from scratch (truly from scratch)
- [ ] Agent has all 3 memory types working
- [ ] Research Agent can autonomously complete 5-step research task
- [ ] Agent has guardrails against prompt injection
- [ ] Traced agent execution in LangSmith

---

## 📝 LinkedIn Articles (This Phase)

### Article 10: "AI Agents Aren't Magic — Here's Exactly How They Work"
**Draft**: `notes/articles/article-10-how-agents-work.md`  
**Post When**: Week 13

### Article 11: "I Built a ReAct Agent From Scratch (No LangChain)"
**Draft**: `notes/articles/article-11-react-from-scratch.md`  
**Post When**: Week 15

### Article 12: "LangGraph vs AutoGen vs CrewAI — My Honest Comparison"
**Draft**: `notes/articles/article-12-framework-comparison.md`  
**Post When**: Week 17

### Article 13: "The 5 Memory Systems Every AI Agent Needs"
**Draft**: `notes/articles/article-13-agent-memory.md`  
**Post When**: Week 16

---

## 🔗 Key Papers

- [ReAct: Synergizing Reasoning and Acting](https://arxiv.org/abs/2210.03629)
- [Reflexion: Language Agents with Verbal Reinforcement](https://arxiv.org/abs/2303.11366)
- [Toolformer: LLMs Can Teach Themselves to Use Tools](https://arxiv.org/abs/2302.04761)
- [Plan-and-Solve Prompting](https://arxiv.org/abs/2305.04091)
- [AgentBench: Evaluating LLMs as Agents](https://arxiv.org/abs/2308.03688)
