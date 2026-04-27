# 🎯 Living Decision Hub - Implementation Guide

Welcome! This document explains the new Decision & Knowledge Management System for Văn Hiến @ MoMo.

---

## WHAT IS THIS?

This is a **Living Knowledge Hub** designed to capture your strategic thinking about projects and decisions at MoMo. It transforms your knowledge base from **static documentation** into a **dynamic decision-making tool**.

**Goal**: Make faster, more informed decisions by capturing:
- ✅ Reasoning behind decisions (not just what, but why)
- ✅ Assumptions you're making (so you can test them)
- ✅ Team capabilities & bandwidth (so you know who to ask)
- ✅ Project status & blockers (so you see the full picture)
- ✅ Learnings & patterns (so decisions improve over time)

---

## THE 3 CORE SYSTEMS

### 1️⃣ DECISION LOG SYSTEM

**What**: Central repository of all strategic decisions you make

**Where**: [[Decision-Log-2026]]

**Why**: 6 months later when someone asks "Why did we choose X?", you have the answer documented. Plus you see patterns in your own decision-making.

**Format**: Context + Options + Decision + Reasoning
```
- Context: What was the situation?
- Options: What alternatives did you consider?
- Decision: What did you choose?
- Reasoning: Why that one? Why not the others?
```

**When to Use**:
- Major project pivots (Phạt Nguội shift to SEO)
- Resource allocation decisions (budget split between projects)
- Technology/tool selections
- Team structure changes
- Strategic prioritization calls

**Cycle**: 
- ⏰ Decision happens → Document in [[Decision-Log-2026]] (within 24h)
- 📊 Review quarterly in [[Quarterly-Reviews]]

---

### 2️⃣ TEAM INTELLIGENCE SYSTEM

**What**: Real-time understanding of who can do what and their current capacity

**Where**: [[Team-Capability-Matrix]]

**Why**: When you need to get something done, you can quickly see:
- Who has the right skill?
- Do they have bandwidth?
- How do they prefer to be approached?
- What constraints limit them?

**What Tracks**:
- Capability map (what they're good at)
- Current capacity (🟢 Available / 🟡 Healthy / 🔴 Overloaded)
- Current focus (what they're working on)
- Communication preferences (how they like to be approached)
- Constraints (meetings, dependencies, limitations)

**Cycle**: 
- 📝 Update monthly (or after major org changes)
- When: End of month review + after major meetings

---

### 3️⃣ PROJECT STATUS SYSTEM

**What**: Live status for each project - metrics, decisions, blockers

**Where**: Each Use-Case file (see [[Use-Case-Status-Template]] for format)

**Why**: You always know:
- Are we on track or at risk?
- What metrics matter?
- What's blocking progress?
- What key decisions were made?
- What's coming next?

**What Tracks**:
- Current metrics vs target (traffic, conversion, KPIs)
- Status indicator (🟢/🟡/🔴)
- Key decisions made this quarter
- Active blockers & resolution status
- Dependencies on other teams/projects
- Next 30 days milestones

**Cycle**:
- 📊 Update weekly (Friday: spend 10 min updating)
- 🔴 Escalate immediately if status becomes blocked

---

## HOW TO USE: WEEKLY RITUAL

### Friday Afternoon (15 mins)

Spend 15 minutes on project status updates:

1. **Update Metrics** (5 min)
   - Pull latest data from GA4/dashboards
   - Update "Current" column in each project's Live Status

2. **Update Status** (3 min)
   - Is it 🟢/🟡/🔴? (Did status change?)
   - Add brief interpretation: "We're on track because..."

3. **Update Blockers** (4 min)
   - Any new blockers emerged this week?
   - Any blockers resolved?
   - Update status of existing blockers

4. **Note Key Decisions** (3 min)
   - Any decisions made this week? Add to [[Decision-Log-2026]]
   - Any learnings from this week? Jot them down for quarterly review

### After Important Meetings

- Record meeting using [[Meeting-Notes-Template]]
- Extract key decisions → [[Decision-Log-2026]]
- Extract blockers → Update project status
- Extract insights → File for quarterly review

### End of Month (30 mins)

- Review all decisions made that month
- Update [[Team-Capability-Matrix]] with any capacity shifts
- Note any new team intel or constraints discovered
- Prepare list of 3-5 decisions for quarterly review

### End of Quarter (1-2 hours)

- Complete [[Quarterly-Reviews]] document
- Review what worked/didn't work
- Capture learnings and patterns
- Share with manager/team for context

---

## THE DOCUMENTS CREATED FOR YOU

### New Templates

| File | Location | Purpose |
|------|----------|---------|
| [[Decision-Log-2026]] | Root | Central log of all 2026 strategic decisions |
| [[Decision-Documentation-Standard]] | 01_Principles/ | HOW to document decisions (frameworks, examples) |
| [[Team-Capability-Matrix]] | 00_About-me/ | Who can do what + current capacity |
| [[Meeting-Notes-Template]] | 04_Skills/ | Standard format for meeting notes |
| [[Use-Case-Status-Template]] | 03_Use-Cases/ | How to maintain live status for projects |
| [[Quarterly-Reviews/Q2-2026-Review]] | 00_About-me/Quarterly-Reviews/ | End-of-quarter strategic review |

### Enhanced Master Doc

[[Klaus-Master-Doc]] now includes:
- New "Decision Hub & Knowledge Management" section (top of doc)
- Links to all new resources
- Weekly maintenance rhythm
- How to use the hub for decision-making

### All Existing Docs

Your existing docs stay the same! These new resources just LAYER ON TOP:
- ✅ 01_Principles - Still there, now with Decision-Documentation-Standard
- ✅ 02_Frameworks - All unchanged
- ✅ 03_Use-Cases - Now with Live Status sections at the top of each file
- ✅ 04_Skills - Now with Meeting-Notes-Template

---

## GIT COMMIT CONVENTIONS

When you update the knowledge hub, use clear commit messages to describe what changed:

```
Format: [Type] [Project/Area]: [Description]

Types:
- decision: Major strategic decision captured
- insight: Learning or market insight
- metric: Project metrics update
- blocker: New blocker or blocker resolved
- team: Team capacity or org change

Examples:
git commit -m "decision phạt-nguội: shift to utilities-led SEO approach"
git commit -m "insight: AI engines ranking affects top 3 traffic sources"
git commit -m "metric: traffic-fines-app now at 65% of Q2 target"
git commit -m "blocker: Web Platform capacity constraint until Q3"
```

This way you can `git log --oneline` and see the history of decisions & updates at a glance.

---

## QUICK START: FIRST WEEK

### Day 1: Explore the System
- Read [[Decision-Log-2026]] - see example decision format
- Read [[Decision-Documentation-Standard]] - understand how decisions should be documented
- Read [[Team-Capability-Matrix]] - see how team intel is tracked

### Day 2-3: Document Recent Decisions
- Think back to major decisions made in last 2 weeks
- Write them up in [[Decision-Log-2026]] using the template format
- Gets you comfortable with the decision format

### Day 4-5: Update Project Status
- Go through your 19 projects
- Add "Live Status" section to each project using [[Use-Case-Status-Template]]
- Fill in current metrics, blockers, next 30 days

### Week 2: Use the System
- After your first meeting, use [[Meeting-Notes-Template]]
- Synthesize decisions from meeting into [[Decision-Log-2026]]
- Update blockers in project status
- By Friday, do your first weekly update ritual

---

## WHY THIS MATTERS

### Problem This Solves

1. **Decision Memory Loss**
   - Problem: 6 months later, "Why did we choose that?" → No one remembers
   - Solution: [[Decision-Log-2026]] preserves reasoning

2. **Assumption Blindness**
   - Problem: Make assumptions, never test them, find out months later they were wrong
   - Solution: Document assumptions → Review quarterly → Test them

3. **Context Switching Tax**
   - Problem: 19 projects + multiple stakeholders = high context switching cost
   - Solution: [[Team-Capability-Matrix]] + [[Use-Case-Status-Template]] = quick context recovery

4. **Stakeholder Trust Gap**
   - Problem: Decisions seem arbitrary to others (they don't see the reasoning)
   - Solution: Document reasoning → share with stakeholders → builds trust in decision-making

5. **Learning Loop Breaks**
   - Problem: Make decisions, execute, never review what worked/didn't
   - Solution: [[Quarterly-Reviews]] forces retrospective thinking

### How to Know It's Working

✅ **Success Indicators**:
- You can answer "Why did we decide X?" by pointing to docs (not people)
- You make 3-5 strategic decisions per month, all documented
- Team knows to ask you "What's in the decision log about Y?"
- Quarterly reviews show clear pattern learning
- New team members can read decision log to understand strategic thinking

---

## COMMON QUESTIONS

### Q: Won't this take forever?

**A**: No. The full cycle takes ~1-2 hours per week:
- Friday updates: 15 min
- Decision documentation: 20-30 min (happens when decision occurs, not separately)
- Meeting notes: 10-15 min per meeting (if you're taking them anyway)
- Quarterly review: 1-2 hours once per quarter

This is way less than the time saved in:
- Faster decision-making (not re-investigating same questions)
- Better team understanding (no need to explain decisions repeatedly)
- Pattern recognition (improving your decision quality)

### Q: What if I miss a week?

**A**: No problem. This isn't a daily system. If you miss a week:
- Just pick up the next Friday
- Catch decisions from the week you missed
- You haven't lost anything (not dependent on daily streaks)

### Q: Should every decision go in the log?

**A**: Not every decision. **Strategic decisions** yes:
- ✅ Major project pivots (budget, direction, timing)
- ✅ Resource allocation (who works on what)
- ✅ Tool/tech selections
- ✅ Organizational decisions

- ❌ Tactical decisions (which day to launch, which color button, which copy A vs B)
- ❌ Delegated decisions (decided by someone else, you're just executing)

If it affects 2+ people or commits resources for 1+ month, it's probably strategic.

### Q: What if I don't have data yet?

**A**: Document anyway with "TBD" or "unknown":
```
Decision: Launch content hub
Status: Pending execution
Impact: [TBD - waiting for performance data]
```

The value isn't just in the final answer, but in showing the thinking. You can update it later.

### Q: How do I review decisions?

**A**: Three ways:

1. **Ad-hoc**: When making similar decision, search [[Decision-Log-2026]] for related decisions
2. **Monthly**: End of month, review decisions from last month
3. **Quarterly**: [[Quarterly-Reviews]] systematically assesses what worked/didn't

---

## SUPPORT & ITERATION

This system will evolve! If something doesn't work:
- Try it for 2 weeks minimum (need time to build the habit)
- If still doesn't work, adapt it
- This is YOUR system - make it work for you

Suggested check-in points:
- **Week 2**: Does the format feel natural or clunky?
- **Week 4**: Am I actually using this for decisions or just documenting?
- **Month 2**: Is the time investment worth it?
- **Quarter 1**: Are quarterly reviews revealing patterns?

---

## NEXT STEPS

1. **Start here**: Read [[Klaus-Master-Doc]] Section 0 (Decision Hub)
2. **Understand the formats**: Read [[Decision-Documentation-Standard]] + [[Use-Case-Status-Template]]
3. **Document past decisions**: Add 3-5 decisions from last month to [[Decision-Log-2026]]
4. **Set up projects**: Add Live Status to 3-5 active projects using the template
5. **This Friday**: Do your first weekly update ritual (15 mins)

**Goal**: By end of Week 1, you should feel comfortable with:
- How to document a decision
- How to update project status
- The weekly ritual rhythm

---

## RESOURCES

- **Central Decision Hub**: [[Decision-Log-2026]]
- **How to Document**: [[Decision-Documentation-Standard]]
- **Team Intel**: [[Team-Capability-Matrix]]
- **Meeting Format**: [[Meeting-Notes-Template]] (04_Skills/)
- **Project Template**: [[Use-Case-Status-Template]] (03_Use-Cases/)
- **Quarterly Learning**: [[Quarterly-Reviews/Q2-2026-Review]]
- **Master Overview**: [[Klaus-Master-Doc]] (Section 0)

---

**Version**: 1.0 | **Created**: 2026-04-27 | **Last Updated**: 2026-04-27

---

## Questions?

This is YOUR knowledge hub. It should work for how you think, not the other way around.

If any part feels forced or unhelpful:
1. Try it for 2 weeks (habits need time)
2. Adapt it if needed (make it yours)
3. Remember: the goal is supporting better decisions, not adding busywork

Good luck! 🎯

