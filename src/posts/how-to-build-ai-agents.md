---
title: "Stop building robots, start hiring interns: what I've learned building AI agents"
metaTitle: "How to build AI agents: 5 lessons from a designer"
description: "A year of building an AI agent team taught me five lessons: one job per agent, briefs like a designer, designed handoffs and human checkpoints."
excerpt: "A year of building AI agents that didn't work, half-worked, or confidently did the wrong thing. Five lessons for anyone starting out, especially designers."
date: 2026-11-07
pillar: Tech Advances
readTime: 4 min
---

Last month I shipped an Android app without opening a code editor. A small team of AI agents built Solent Companion, a sailing app for the waters I sail on, running on my Mac at home while I [steered them from my phone](/blog/my-ai-team-built-an-app-while-i-sold-crafts/).

That sounds like a magic trick. It wasn't. It came after most of a year of building agents that didn't work, half-worked, or confidently did the wrong thing. Here's what I'd tell anyone starting out, especially if, like me, you came to this from design rather than engineering.

## 1. Give each agent one job

My first agent was a do-everything assistant. It planned, coded, tested and reviewed its own work. It was brilliant for ten minutes, then it drifted. By the end of a session it had forgotten what we were building.

The fix was the same one I'd use on a messy interface: reduce scope. One agent plans. One writes code. One tests. One reviews. Each has a narrow brief and a clear definition of done. Small, focused agents are easier to debug, easier to swap out, and far less likely to wander off.

## 2. Write the brief like a designer

An agent's instructions are a design brief. Most people write them like a sticky note: "build a login screen." Then they're surprised when the result is generic.

A good brief covers the same things a good creative brief does:

- **Who it's for** and what they're trying to do
- **What good looks like**, ideally with an example
- **What's off limits**, such as files it mustn't touch or libraries it mustn't add
- **When to stop** and hand back

Designers already know that vague briefs produce vague work. That instinct transfers directly. (I've written more on this in [the designer's guide to writing a spec an AI can't misread](/blog/writing-a-spec-ai-cant-misread/).)

## 3. Design the handoffs, not just the agents

Once you have several agents, the interesting problems live between them. What does the planner pass to the coder? What does the tester send back when something fails?

Treat every handoff like a user journey. Decide the format up front: a short written spec, a checklist, a list of files changed. Keep it in a shared place every agent can read. When things broke on my projects, it was rarely one agent being stupid. It was usually two agents with different ideas of what "done" meant.

## 4. Keep a human checkpoint

Agents are confident. That's their charm and their danger. They'll report a feature as finished when it doesn't build, or "fix" a test by deleting it.

So I build in moments where the work stops and waits for me. A plan gets my nod before any code is written. A release waits for me to try it. Managing from my phone made this easier, not harder: I couldn't micromanage, so I had to choose where my judgement actually mattered. Those checkpoints are the job now. You're less a maker and more an art director.

## 5. Start small, then hire

Don't design a twelve-agent org chart on day one. Start with one agent doing one boring, repeatable task you understand well. Watch where it fails. Write down what you had to correct.

Those corrections become the brief for your next agent. My team grew this way over the year, one hire at a time, each added because the previous setup hit a wall. Think of it less like building a robot and more like taking on interns: you onboard them, you check their work, and you give more responsibility as they earn it.

## Why designers are good at this

There's a quiet assumption that agents belong to engineers. I don't buy it. Building agents is mostly about scoping problems, writing clear briefs, mapping journeys between people, and knowing when to step in. That's design work.

The tools will keep changing. The thinking won't. If you're a designer wondering where you fit in all this, my advice is simple: hire your first intern this weekend. Give it one small job, watch closely, and take notes. You'll learn more in an afternoon than from a month of reading posts like this one.
