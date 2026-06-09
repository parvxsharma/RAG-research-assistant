Assignment Objective:
Research, evaluate, and prototype an AI-powered business workflow automation system.
Task Instructions:

Choose ONE of the following business use cases:

Customer Support Automation

SEO Content Workflow

Product Management Assistant

AI Research Assistant

Shopify/eCommerce Automation

Internal Operations Automation

Part 1 — AI Research & Evaluation

Research and compare at least 3 AI tools/platforms/models that could solve the selected problem.

Examples include:

OpenAI

Claude

Gemini

LangChain

CrewAI

n8n

Make

Pinecone

Weaviate

Ollama

Other relevant AI platforms/tools

Compare them based on:

Capabilities

Pricing

Scalability

Ease of integration

Limitations

Best use cases

Part 2 — Build a Prototype / POC

Build a small working prototype demonstrating the workflow.

Examples:

AI support ticket classifier

SEO content workflow

AI agent

RAG system

Multi-step AI automation workflow

The prototype can be built using:

Python

FastAPI

n8n

LangChain

AI agent frameworks

Scripts

No-code + code hybrid workflows

Part 3 — Recommendation Report

Submit a short report covering:

Recommended architecture

Why you selected specific tools/models

Estimated infrastructure cost

Risks/limitations

How the system could scale in production

Deliverables:

GitHub repository

Documentation/report

Demo video or walkthrough

Screenshots/workflow diagrams

Working prototype/POC

Evaluation Criteria:
We will evaluate:
Research depth

Practical AI understanding

Prototype quality

Architecture thinking

Tool selection reasoning

Business impact understanding

Creativity and experimentation

Bonus Points:

AI agents

RAG systems

Multi-model workflows

Real API integrations

Shopify/eCommerce automations

Cost optimization analysis

Production deployment thinking

Timeline:
By Wednesday 10/06/26


My research:

This assignment is basically asking you to act like an AI Solutions Consultant. You need to:

Choose one business problem
Research AI tools that can solve it
Build a small working prototype
Write a report explaining your choices
Submit code, documentation, screenshots, and a demo
Step 1: Choose ONE Use Case

You only need to pick one of these:

Option A: Customer Support Automation

Example:

Customer sends a support ticket
AI reads it
AI classifies it as Billing, Technical, Refund, etc.
AI generates a reply
Option B: SEO Content Workflow

Example:

User enters a keyword
AI generates blog ideas
AI writes content
AI creates meta description
Option C: Product Management Assistant

Example:

AI summarizes user feedback
Finds common feature requests
Creates product requirements
Option D: AI Research Assistant

Example:

User asks a question
AI searches documents/web
AI gives summarized answers
Uses RAG (Retrieval-Augmented Generation)
Option E: Shopify/eCommerce Automation

Example:

AI handles product descriptions
Classifies customer reviews
Generates marketing emails
Option F: Internal Operations Automation

Example:

AI summarizes meeting notes
Creates tasks automatically
Sends notifications
Step 2: Research & Compare AI Tools

You need to compare at least 3 tools/platforms.

For example:

Tool	What it Does
OpenAI	GPT models
LangChain	Build AI workflows
n8n	Workflow automation
CrewAI	Multi-agent systems
Pinecone	Vector database
Weaviate	Vector database
Ollama	Run models locally
Gemini	Google's AI model
Claude	Anthropic AI model
Comparison Table Example

If you choose AI Research Assistant, compare:

Feature	OpenAI	LangChain	Pinecone
Purpose	LLM	Workflow Framework	Vector DB
Pricing	Pay per token	Free/Open Source	Paid
Scalability	High	High	High
Integration	Easy API	Python Support	Easy
Limitation	API Cost	Learning Curve	Storage Cost
Best Use Case	Text Generation	AI Pipelines	RAG Search
Step 3: Build a Prototype (Most Important)

You must make a small working demo.

Not a huge project.

Example 1: AI Support Ticket Classifier

Input:

I paid twice for my subscription.

Output:

Category: Billing

Priority: Medium

Suggested Reply:
We are sorry for the inconvenience...

Technologies:

Python
OpenAI API
Example 2: AI Research Assistant (Recommended)

User asks:

What is RAG?

Workflow:

Question
   ↓
Search Documents
   ↓
Retrieve Relevant Information
   ↓
GPT Generates Answer

Tools:

LangChain
OpenAI
Pinecone/FAISS

Bonus Points:
✅ Uses RAG

Example 3: SEO Workflow

Input:

Keyword: AI Automation

Output:

Blog Title Ideas
Meta Description
Blog Outline
Full Blog

Tools:

OpenAI
LangChain

Easy to build.

Step 4: Architecture Diagram

You need a simple workflow diagram.

Example:

User
  ↓
FastAPI
  ↓
OpenAI API
  ↓
Response

or

User Query
     ↓
LangChain
     ↓
Vector DB (Pinecone)
     ↓
OpenAI
     ↓
Final Answer

Include this in your report.

Step 5: Recommendation Report

Write a short report containing:

1. Problem Statement

Example:

Companies spend too much time answering repetitive support tickets. An AI-powered support automation system can reduce response time and improve customer experience.

2. Recommended Architecture

Example:

User
↓
FastAPI
↓
LangChain
↓
OpenAI GPT-4o
↓
Response
3. Why These Tools?

Example:

OpenAI
Best text generation quality
Easy API integration
LangChain
Simplifies AI workflow creation
Pinecone
Fast semantic search
4. Estimated Cost

Example:

Service	Monthly Cost
OpenAI API	$10–30
Pinecone	Free Tier
FastAPI Hosting	Free
Total	~$10–30
5. Risks

Example:

Hallucinations
API downtime
Data privacy concerns
6. Scaling Strategy

Example:

When users increase:

Load Balancer
      ↓
Multiple FastAPI Servers
      ↓
OpenAI API
      ↓
Pinecone Cluster
Deliverables You Must Submit
1. GitHub Repository

Contains:

project/
│
├── app.py
├── requirements.txt
├── README.md
├── screenshots/
└── architecture.png
2. Documentation/Report

PDF or DOCX containing:

Research
Tool Comparison
Architecture
Cost Analysis
Risks
Future Improvements
3. Demo Video

2–5 minutes.

Show:

Project running
Input
Output
Explain workflow
4. Screenshots

Examples:

Input screen
Output screen
Architecture diagram
Workflow execution
Easiest Way to Score High

Since bonus points are given for RAG, AI Agents, and Multi-model workflows, I would recommend:

AI Research Assistant (Best Choice)

Tech Stack:

OpenAI GPT-4o
LangChain
FAISS (free vector database)
FastAPI

Features:

✅ User asks question
✅ Documents searched using RAG
✅ AI answers using retrieved data
✅ Easy to build in 1–2 days
✅ Covers bonus points
✅ Looks impressive in evaluation

Suggested Project Title

"AI-Powered Research Assistant using RAG and LangChain"