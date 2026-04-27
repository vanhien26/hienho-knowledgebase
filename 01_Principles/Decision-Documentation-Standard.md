# Decision Documentation Standard

> Standard format để capture strategic decisions - giúp preserve reasoning và enable future learning

---

## WHY DOCUMENT DECISIONS?

1. **Decision Memory** - 6 months later, "Why did we choose this?" answered by reading docs, not by asking people
2. **Learning Loop** - Assess assumptions, learn what worked/didn't work
3. **Knowledge Transfer** - New team members understand not just WHAT we do, but WHY
4. **Faster Future Decisions** - Similar problems reference past decisions + learnings
5. **Stakeholder Trust** - Transparent reasoning builds confidence

---

## DECISION STRUCTURE: Context + Options + Decision + Reasoning

### 1. CONTEXT (Answer: What's the situation?)

**Purpose**: Set the stage so future readers understand why this decision mattered

**Include**:

```markdown
### Context
- **Background**: What happened before this decision? Previous attempts? Market/org changes?
- **Current State**: What is the situation NOW? What's working? What's not?
- **Trigger**: What prompted this decision RIGHT NOW? (Not "we need to do something" but "this specific thing happened")
- **Constraints**: What limits our options?
  - Time constraints (deadline, urgency)
  - Budget/resources (limited bandwidth, cost limits)
  - Dependencies (waiting on other teams, tool limitations)
  - Organizational (policy, alignment needs)
- **Stakeholders**: Who cares about this decision? Who will be affected?
```

**Good Context Example:**
```
- Background: Traffic Fines mini-app launched 3 months ago with ads strategy. Low conversion despite high CTR.
- Current State: Spending $5K/month on ads, getting 2% conversion (industry standard 5%). CAC is $50, LTV unclear.
- Trigger: Web Platform just became available for Q2 projects. Market data shows search volume for "how to pay traffic fines". Competitor using content + app approach.
- Constraints: Web Platform busy again Q3 (MoSpark). CMS transition happening May-June. Content team has 2 people.
- Stakeholders: Klaus (strategy owner), Web Platf (execution), Content (execution), CFO (budget), Product (metrics).
```

**Bad Context Example:**
```
- We need to improve traffic fines app performance
[Too vague. Why now? What's the specific problem? What's changed?]
```

---

### 2. OPTIONS CONSIDERED (Answer: What were the alternatives?)

**Purpose**: Show you thought it through. Help future readers understand trade-offs.

**Include for Each Option**:
```markdown
#### Option [A/B/C]: [Name]
- **How it works**: [Describe the approach]
- **Pros**: [What are the benefits?]
- **Cons**: [What are the downsides?]
- **Effort**: [Time/resources required - Low/Medium/High]
- **Risk**: [What could go wrong?]
```

**Good Options Example:**
```
#### Option A: Increase Direct Ads
- How: Boost ad spend from $5K to $8K/mo, refine targeting
- Pros: Quick learnings, proven channel, easy to scale up/down
- Cons: High CAC observed already, diminishing returns typical in ads
- Effort: Low (ongoing optimization)
- Risk: Budget burn without ROI improvement

#### Option B: Utilities-Led SEO Content Hub (CHOSEN)
- How: Build content about "how to pay traffic fines", then promote app in content
- Pros: Better user intent match, lower CAC over time, aligns with company GEO strategy
- Cons: Longer timeline (3-4mo), dependent on Web Platform availability
- Effort: High (strategy + content building + tracking)
- Risk: Content performance uncertainty

#### Option C: Cross-Promote from Other Products
- How: Bundle with Credit, Insurance, Payment products
- Pros: Uses existing traffic, integrated offer
- Cons: Dependent on other roadmaps, timing risk
- Effort: Medium (coordination)
- Risk: Can't control execution timing
```

**Why This Matters**: Future readers see you compared approaches, not just picked one randomly. When someone asks "Why didn't we try X?", you can point to Options section.

---

### 3. DECISION (Answer: What did you choose and why?)

**Purpose**: Be explicit about what you decided

**Format**:
```markdown
### Decision: [Option X - Full Name]

[1-2 sentences explaining the choice]
```

**Good Decision Example:**
```
### Decision: Option B - Utilities-Led SEO Approach

We're shifting Traffic Fines from direct ads to a content-driven approach. Instead of pushing "download the app", we'll create content answering "how to pay a traffic fine", then position the mini-app as the solution within that content.
```

---

### 4. REASONING (Answer: Why this decision? Why not the others?)

**Purpose**: Explain the thinking. This is the most important part.

**Include**:
```markdown
### Reasoning

- **Why this option**: [Primary reason - the core logic]
- **Why not Option A**: [Specific reason this one didn't work]
- **Why not Option B**: [Specific reason this one didn't work]
- **Trade-offs accepted**: [What we're giving up]
- **Assumptions**: [What must be true for this to work]
```

**Good Reasoning Example:**
```
### Reasoning

- **Why Option B**: Traffic fines is fundamentally a utility search. Users don't search "download traffic fines app" - they search "how do I pay a traffic fine online". If we match user intent first, the app becomes the natural solution. This aligns with MoMo's GEO strength (being cited in Google AI/ChatGPT for finance questions).

- **Why not Option A (More Ads)**: We already see diminishing returns on ads (CAC rising despite spend increase). Ad efficiency is already below industry standard. Throwing more budget won't fix the fundamental problem: user intent mismatch.

- **Why not Option C (Cross-Promote)**: Credit and Insurance have their own roadmaps. We can't control their launch timing or feature prioritization. We'd be dependent on external teams, which slows execution and makes it harder to measure our impact.

- **Trade-offs**: Content approach takes longer (3-4 months vs ads weeks). Higher execution risk (content performance unknown). Dependent on Web Platform staying available (risky given Q3 capacity crunch).

- **Assumptions**: 
  1. Search volume exists for "how to pay traffic fines" utility
  2. Web Platform can execute content hub in Q2
  3. Content-to-app conversion will be >5%
  4. Users searching traffic fines utilities are high LTV segment
```

---

### 5. EXECUTION (Answer: How will we make this happen?)

**Purpose**: Make the decision actionable

**Include**:
```markdown
### Execution
- **Owner**: [One person accountable]
- **Team**: [Who needs to help]
- **Timeline**: [When key milestones happen]
- **Success Criteria**: [How we know it worked]
```

**Good Execution Example:**
```
### Execution
- **Owner**: Klaus (strategy + content planning)
- **Team**: Web Platform (content hub building), Content team (content creation), GTM (tracking setup)
- **Timeline**:
  - Content strategy finalized: 2026-05-15
  - Content hub MVP live: 2026-06-30
  - First performance data: 2026-07-31
- **Success Criteria**:
  - 100+ ranked keywords for traffic fines utility queries
  - 5%+ conversion from content to mini-app install
  - CAC <$2 from organic (vs $50 from ads)
```

---

### 6. REVIEW DATE (Answer: When will we assess if this worked?)

**Purpose**: Decision isn't fire-and-forget. Build in review points.

**Include**:
```markdown
### Review Date
- **Check-in**: [When we'll review data and assess]
- **Kill-Switch**: [If this doesn't work by X date, we pivot back]
```

**Good Review Example:**
```
### Review Date
- **Check-in**: 2026-07-15 (after 6 weeks of live content, should have sufficient data)
- **Kill-Switch**: If by 2026-09-30 we have <500 monthly organic traffic or <2% conversion rate, we acknowledge this approach isn't working and pivot back to paid ads or try Option C
```

---

## COMMON PITFALLS TO AVOID

### ❌ DON'T: Omit Reasoning
```
"We chose Option B because it seemed like the best approach"
[Why? Best by what criteria? This teaches nothing.]
```

### ✅ DO: Be Specific
```
"We chose Option B because it matches user search behavior (utility intent) and leverages our GEO strength, unlike Option A which hits CAC ceiling, and Option C which has timing risk."
```

---

### ❌ DON'T: Only List the Chosen Option
```
Just describe how you'll execute, nothing else
[Future reader can't understand the trade-offs you made]
```

### ✅ DO: Show the Full Set of Options
```
Describe A, B, C, explain why each was/wasn't chosen
```

---

### ❌ DON'T: Make Assumptions Implicit
```
"Content approach will work because content converts"
[What content conversion rate are you assuming? Is that realistic?]
```

### ✅ DO: Surface Assumptions Explicitly
```
"Assumption: Users searching 'how to pay traffic fines' have >5% app install rate.
Basis: Similar behavior in Insurance mini-app (6% conversion). This is our biggest assumption risk."
```

---

### ❌ DON'T: Skip Kill-Switch Conditions
```
"We'll review in Q3"
[What does success look like? When do we admit it's not working?]
```

### ✅ DO: Define Success + Failure Upfront
```
"Success: 100+ keywords ranking + 5% conversion. Failure/Kill-switch: <500 organic traffic OR <2% conversion by Sept 30."
```

---

## TEMPLATE TO COPY

```markdown
## [Decision Title]

**Date**: [DD-MM-2026]
**Project**: [Project Name]
**Status**: [Pending/In-Progress/Completed/On-Hold]

### Context
- **Background**: 
- **Current State**: 
- **Trigger**: 
- **Constraints**: 
- **Stakeholders**: 

### Options Considered

#### Option A: [Title]
- **How it works**: 
- **Pros**: 
- **Cons**: 
- **Effort**: 
- **Risk**: 

#### Option B: [Title]
- [Same structure]

#### Option C: [Title]
- [Same structure]

### Decision: Option [X] - [Full Name]

[1-2 sentence explanation]

### Reasoning
- **Why this option**: 
- **Why not others**: 
- **Trade-offs accepted**: 
- **Assumptions**: 

### Execution
- **Owner**: 
- **Team**: 
- **Timeline**: 
- **Success Criteria**: 

### Review Date
- **Check-in**: 
- **Kill-Switch**: 

### Impact/Learnings
- **Status**: 
- **Early Result**: 
- **Insight**: 
```

---

## WHERE TO USE THIS STANDARD

1. **New Strategic Decisions** - All decisions in [[Decision-Log-2026]]
2. **Major Project Pivots** - Document in project file why you're changing direction
3. **Resource Allocation** - When choosing which project to prioritize
4. **Tool/Tech Selections** - When evaluating options (CMS, Analytics, etc.)
5. **Team Changes** - Why you're reorganizing or changing responsibilities

---

## WHY THIS FORMAT?

**Context** = Grounds the decision in reality (not abstract)
**Options** = Shows you thought critically (not impulsive)
**Reasoning** = Explains the thinking (enables learning + transfer)
**Execution** = Makes it actionable (not just philosophy)
**Review** = Ensures accountability (not wishful thinking)

This structure takes 30-45 minutes to fill out properly, but saves hours in:
- Future decision-making (reference past decisions)
- Onboarding (new people understand the why)
- Retrospectives (learn what worked/didn't)
- Stakeholder communication (shows thoughtful approach)

