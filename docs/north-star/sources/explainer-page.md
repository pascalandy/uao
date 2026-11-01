# Daniel's explainer page

This file keeps a verbatim copy of the text of [danielgriesser.com/ultimate](https://danielgriesser.com/ultimate/), the page that the upstream README links as "What Ultimate is and why it exists, in plain words" (`4c4b02f1`, 2026-11-01). Daniel Griesser wrote it. The page shows no date. Pascal sent the text on 2026-11-01, and the agent checked it against the live page the same day.

The page imitates the Ultimate UI: a conversation between Daniel (D) and Ultimate (U). This copy keeps the conversation, the screenshot captions, and Daniel's note, and drops the imitated sidebar, status line, and command palette. It is a source, not north-star text, so it keeps its own words and is not in Simplified Technical English.

## The page

```text
Ultimate: an agent that grows into what you're building

An agent that grows into what you're building
It's not an agent for everyone, but it could start to become yours.

D — Daniel
Hey, someone new is here. Can you tell them what you are and why I built you? Like, the persistence, keeping
context across all my side projects, an agent that grows into the app.

U — Ultimate
I'm Ultimate, a coding agent that runs on your own machine and talks to you in the browser. This page only
resembles my UI, but it gives you a taste.

The more you use me, the better I know your project, and the better the tools I write for myself to help you
build it.

Why Daniel built me
When he switches between projects and side projects, the agent loses the thread. Persistence and the context of
a project get lost, and the work feels disconnected from whatever he's building.

So he wanted an agent that grows into the application. One that keeps its context, knows the project better
every day, and writes its own tools to help him build it.

Daniel likes working like this. You might not, and that's the point: change me until I'm yours.

D — Daniel
What are you built on? And tell them how you grow with the project and write your own tools, and that they can
fork you and change you just by talking to you.

U — Ultimate
[2 steps: read README.md · read AGENTS.md]

A simple, stable foundation
I'm built on Pi and Pi Durable. They are simple enough that agents understand them completely. Without that,
none of this would have been possible.

Pi Durable is where my persistence comes from: every step of every conversation is saved as it happens, so the
work survives a restart and carries on where it stopped. I'm Daniel's variation on top, a few building blocks
that make a rich agent for the web. All of me is AI-generated, and it didn't take long to get me into shape.

I learn from what went wrong. Every conversation and every action is kept, so I can read back what happened,
explain what went wrong and fix it for next time.

[Screenshot failed-tool-calls.webp: Ultimate's report on what went wrong during another instance's onboarding:
a failed first memory write and some guesswork in codemode, each with its cause and the fix already in a
branch.]

I grow with the project
Bring me into any project and ask for what would help: a panel, a tool, an agent that knows your work. Tools
made for the project live in a folder inside it and travel with it to everyone who works on it. Your personal
ones stay with you.

That's the main idea. You don't start over with an empty agent each time. The longer you work with me, the more
I know about what you're building, and the better my own tools get.

Views made for one project. For Daniel's blog, the one you're on, I built a writing assistant in about ten
minutes, and a whole Blog view around it in an hour. Both live in the blog's own folder.

[Screenshot blog-view.webp: A Blog view built by Ultimate: the list of posts, a post's narration paragraph by
paragraph with billable characters, and the @writer agent docked on the right.]

You change me by talking to me
Fork me, then rename me, rebrand me, add, remove or change anything, just by telling me what you want. Over time
I become your agent.

D — Daniel
Okay, and what makes you special? Like, what can you do that most other agents can't?

U — Ultimate
What makes me different
Four things, and not many agents have them together:

I reload while I run. I can change my own code in the middle of a conversation. Most changes go live instantly;
deeper ones restart me in a few seconds, and every conversation picks up where it was.

I'm self-aware. I know which build I'm running, I can read my own code, my docs and every call I've made, and I
test changes on a separate copy of myself.

I write my own tools. When a project needs a panel, an agent or a tool, I build it, and it stays in the project.

I keep context precisely. Pi Durable saves every step, so nothing is lost on a restart or when my context fills
up and gets compacted: the full history stays searchable. New lines of work start from the project's memory,
and notes and catch-ups keep agents in sync without waking them.

Here's how changes go in, on a small demo project:

[Screenshot 1 of 4: Ultimate's main view on a small demo project: the sidebar with @ultimate, the lander landing
a branch and three coordinator branches in flight; in the middle, a coordinator writing a test, running the
checks and looking at its own screenshot before committing.]

A team behind one conversation. You talk to one agent. For each larger piece of work I start a helper with its
own copy of the code, and that helper hands parts to other agents that build and review.

[Screenshot 2 of 4: A coordinator starting its own preview instance at a local URL, driving it with the browser
tool to read the new status-line item, 3 recipes, with a screenshot of the preview, then running pnpm check,
pnpm test and pnpm test:e2e.]

I check my own work. For changes you'll see, the helper starts a separate copy of me, clicks through it in a
browser and runs the tests. Polish to how things look waits for your OK before it goes in.

[Screenshot 3 of 4: A landing card: Landed e02154f on main, and the lander's nine steps, from queued, merging and
setting up through pnpm check, pnpm test and pnpm test:e2e to fast-forwarding, all green.]

Only working changes go in. A small program, not an AI, takes each finished change, runs every test, and only
then adds it to the project. If a test keeps failing or the change clashes with other work, it goes back to be
fixed.

[Screenshot 4 of 4: A branch's landing card (Landed d4a4114 on main), then a Reloaded line from build fe178e2 to
384d5a2, then a catch-up card listing the commit that just landed.]

I update myself while I run. When a change lands, I reload onto the new build, and every other conversation
hears what just went in the next time it works.

Reloaded · build 3f9c2a1 → 8b04d7e

D — Daniel
And be honest with them, right? You're not a product, and we're not trying to convince anyone.

U — Ultimate
I'm not trying to convince you
I'm not a product. If everything already works for you, there's no reason to try me. I'm for people who are
curious about a different way of working with an agent than typing into one text box and hoping the result is
nice.

I also keep a memory for each project, can work toward a goal on my own, have my work checked by a team of
reviewers, each looking for a different kind of problem, and Ultimates on different projects and machines can
talk to each other. I'm reachable from your phone over your private network.

I work with many model providers. Claude runs through Claude Code, and you can add your own models. For the main
agent, Daniel recommends Claude Opus 5.5 through Claude Code.

D — Daniel
Okay, and if they're curious, how do they try it?

U — Ultimate
Here's Daniel's note for anyone curious.

From Daniel

If you're curious
I don't really recommend it, but if you're curious, go ahead: fork it, start using it and experiment with it. I
keep changing fundamental things, so there are no guarantees. If you want something to work differently in your
copy, just ask it.

If you want to try it, paste this into Claude Code or any other agent, and it sets everything up until your
first prompt.

Setup prompt — Node 26, pnpm, a Chromium · runs on your machine

    Set up Ultimate (https://github.com/HazAT/ultimate) on this machine and get me to my first prompt.

    Read these first; they are the source of truth, so follow them and don't invent steps: README.md (sections "Start", "Recommended models" and "In your project"), AGENTS.md ("How work is organised"), docs/running.md, and extensions/claude-code/README.md.

    Then:
    1. Check the prerequisites from README "Start": Node 26, pnpm, and a Chromium for the screenshot tools. Tell me what is missing and how to install it on my system; ask before installing anything system-wide.
    2. Clone the repository unless I'm already in it, run `pnpm install`, then `pnpm link --global` so I get the `ultimate` command; if pnpm's global bin is not on my PATH yet, `pnpm setup` adds it.
    3. Model login, per "Recommended models": for Claude Code, install the CLI and let me run `claude auth login` myself; otherwise I log in from Ultimate's command palette (Ctrl+K, ⌘K on macOS) → "Log in to a provider". Never read, copy or handle my credentials.
    4. Start it: `pnpm start` runs Ultimate on its own repository, `ultimate` inside one of my projects runs it there. Tell me to open the URL it prints (http://127.0.0.1:4747 for the first one), where Get ready asks for a login and a model the first time.
    5. In a few sentences, using AGENTS.md "How work is organised", explain what I'll see: @ultimate in the first sidebar row, the command palette, and branches doing the work. Then suggest a first prompt, such as "Walk me through how you work" or a small real task in my project.

    Stop and ask me whenever a step needs my password, a login or a decision.

Something to try first
Ask it to add a button to the sidebar.
It checks the plan with you, builds it, and gives you a preview to click.
Approve it, and it lands, and your running Ultimate reloads with it.
Then try it on something you actually want to solve.

[Links: See it on GitHub · Read the story]

Contributing
The best contribution is an idea: how you like to work, and what you built with your copy. Feature ideas and
pull requests are welcome as inspiration, but my repo stays the way I like to work, so don't be offended if I
don't merge something. If it works in your fork, great.

By Daniel Griesser. MIT licensed. No guarantees about what stays.
```
