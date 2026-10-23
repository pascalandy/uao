# Daniel's first prompt

This file keeps a verbatim copy of the first prompt for Ultimate. Daniel Griesser wrote it, and he ran it in bb ([getbb.app](https://getbb.app)). He wrote it before 2026-10-01 (inferred: the first commit, `9b341af`, says "The v0 plan lives in bb task ULT-1"). The prompt is public, but it has no public URL that we know, so uao keeps this copy.

The copy starts with the message that Daniel sent with the prompt. It is a source, not north-star text, so it keeps its own words and is not in Simplified Technical English.

[Daniel's post](https://danielgriesser.com/posts/ultimate/) tells how the first version started, in the section "How it Started". It names a Claude Code session with Opus 5.5 after a long planning session.

## The message and the prompt

```text
yo, I used getbb.app with this inital prompt, and tbf bb already quite a setup on my side, but here is the prompt, I dictate 😅. curious what you use it for and Opus 5.5 on Extra High

>  PROMPT

Okay, so I want to, so this is going to be a big project that we need to definitely break it down and you need to do some investigations. earendil.com/posts/pi-durable/ Read this post thoroughly and follow the tips on the bottom. Like you need to understand pi-durable and the concepts behind it like extremely well. because we want to build the ultimate coding agent. called Ultimate

It should be a local but as well online multipurpose agent that can do everything on the fly and test the context to do everything on the fly. What I mean by that is that we will start just with a local VIT version based or with VITe plus and using node just to keep things simple. But we will have UI for it and as...pi-durable already like supports and what we're going to do is It should also support different packets like again it has SQLite for locally. But it can also support cloudflare right.

We focus on the first version for just local, but you get the idea like we shouldn't close that door. And you can lean just like as a basic concept. Initially you can lean on BB a bit like for UI. We need to just have something super clean as well. Nothing major, not a lot of dependencies. Maybe using StyleX. consider leaning on github.com/HazAT/fabric/tree/main/apps/web for some basic architecture/boilerplate -

the basic premise is that first of all it can write and build its own UI. It knows the source code, it knows everything around it and we can live reload and the conversation keeps continuing going, the tools keep continuing going because everything runs in pi-durable - We can completely like build the agent itself while it builds itself. - we start with a private repo to go wild - Think about how cool this is and we just want to get the fundamentals going. So an input box log inflow but everything should be in web so it should look and feel nice.

But it's again basic pylog in provider select or API token or whatever model selection and then just like showing which extensions are loaded showing which skills are loaded showing the environment it runs in because it runs locally on this machine right so this is baked in already we can have the execute and persistence layer like we should always also show this what's active readily which machine is the code running on and what is the persitance layer

Also always like which model extra high context information very close to what the pay terminal provides you right like very nerdy but very good looking and everything is in web. consider leaning on www.shadcn.io/ai but I am not sure if we should drop stylex then - maybe we should and just lean on this - And again main focus is also that is the UI that we are building is also hot reloadable. This is a requirement that we should make and everything like when it comes to inspiration and how clean the coat is fully lean on pi. This is our role model and our state how we want to develop. And the purpose is also like minimal dependencies as much as possible but with hot reloading, right? This is now the Uber. You start a process, the process runs, you get a web URL, it opens up and then you just go for it and can build whatever you want. You have you start with this input box, right? Then you can say stuff like, okay, hey, move me in a small bar and start building a sidebar and keep my conversations there and then it builds it in front of you. You see the code, you see the diffs, you see the tool calls, you see everything. So we give the agent the default pi tools To be a completely full functional coding agent and then once we have the first version going we we built ultimate with ultimate if that makes sense like we just need a skeleton of an agent with all its information going and then we just We just keep iterating on it together and since everything is so nicely structured This this this will be awesome. I hope you get the idea. So do some investigations Let's riff a bit on this Ask me a couple of questions make sure everything is clear and then we implement this bad boy. This is going to be Our magnum opus
```
