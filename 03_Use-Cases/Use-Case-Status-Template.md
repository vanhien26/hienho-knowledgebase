# Use-Case Status Template

> Add this "Live Status Section" at the TOP of each Use-Case file to maintain current metrics, decisions, and blockers

---

## COPY THIS TO EACH USE-CASE FILE

```markdown
---

# [PROJECT NAME] - Live Status

**Status**: 🟢 On Track / 🟡 At Risk / 🔴 Blocked
**Last Updated**: [DD-MM-2026]
**Owner**: [Your name]

## CURRENT METRICS (As of [DATE])

| Metric | Target | Current | % of Goal | Trend |
|--------|--------|---------|-----------|-------|
| Traffic (monthly) | X | Y | Z% | ↗️/→/↘️ |
| Conversion | X% | Y% | - | ↗️/→/↘️ |
| KPI 1 | X | Y | - | ↗️/→/↘️ |
| KPI 2 | X | Y | - | ↗️/→/↘️ |

### Interpretation
- **On track**: [What's working? Why ahead/on target?]
- **At risk**: [What could derail us?]
- **Blockers**: [What's actively blocking progress?]

## KEY DECISIONS THIS QUARTER

### Decision 1: [Name]
- **What**: [What was decided]
- **When**: [When it was made]
- **Status**: [Pending/In-Progress/Completed]
- **Impact**: [Expected or actual result]
- **Link**: [[Decision-Log-2026#decision-name]]

### Decision 2: [Name]
- [Same structure]

## CURRENT BLOCKERS

### Blocker 1: [Name]
- **What**: [What's blocking]
- **Impact**: [How does it affect timeline/metrics?]
- **Owner**: [Who will resolve]
- **Status**: [Pending/In-progress/Resolved]
- **ETA**: [When it will be resolved]

### Blocker 2: [Name]
- [Same structure]

**None identified**: [If no blockers]

## DEPENDENCIES

**Waiting On**:
- [What]: From [Whom] → Due [When] → Status [Pending/In-progress/Done]
- [What]: From [Whom] → Due [When] → Status [Pending/In-progress/Done]

**This Project Affects**:
- [[Other-Project-A]]: How it affects
- [[Other-Project-B]]: How it affects

## NEXT 30 DAYS

- [ ] [Milestone 1] - Due [DD-MM] - Owner [Person]
- [ ] [Milestone 2] - Due [DD-MM] - Owner [Person]
- [ ] [Milestone 3] - Due [DD-MM] - Owner [Person]

## RISK REGISTER

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|-----------|
| [Risk] | Low/Med/High | Low/Med/High | [What we're doing] |

---

# [ORIGINAL PROJECT CONTENT BELOW]

[Rest of your BRD/project documentation...]

```

---

## WHAT TO UPDATE & WHEN

### Weekly (Friday Afternoon)
- **Metrics**: Any new data available? Update current performance
- **Blockers**: Any new blockers? Any resolved?
- **Status**: Do we need to change 🟢/🟡/🔴?

### After Meetings
- **Key Decisions**: Any new decisions made? Link to [[Decision-Log-2026]]
- **Dependencies**: Any new dependencies identified?
- **Blockers**: Any blockers surfaced?

### Monthly (End of Month)
- **Next 30 Days**: Update milestones for next month
- **Risk Register**: Any new risks or risk status changes?
- **Interpretation**: Update brief commentary on what's happening

---

## EXAMPLE: FULLY FILLED OUT

```markdown
# Traffic Fines (Phạt Nguội) Mini-App - Live Status

**Status**: 🟡 At Risk
**Last Updated**: 2026-04-27
**Owner**: Văn Hiến

## CURRENT METRICS (As of 2026-04-27)

| Metric | Target | Current | % of Goal | Trend |
|--------|--------|---------|-----------|-------|
| Monthly Traffic | 10,000 | 2,500 | 25% | ↘️ |
| Conversion to App | 5% | 2% | 40% | ↘️ |
| Monthly Users | 500 | 50 | 10% | ↘️ |
| CAC from Ads | <$2 | $50 | - | ↗️ (worse) |

### Interpretation
- **Why at risk**: Ads approach hitting CAC ceiling. Low conversion despite high traffic spend. Current trajectory misses Q2 target by 8K traffic.
- **What we're doing**: Pivoting to utilities-led SEO (Decision 1, Q2). Will take 6-8 weeks to see impact.
- **Decision point**: By 2026-07-31, if organic traffic <500/mo and conversion <2%, we'll pivot back or try different approach.

## KEY DECISIONS THIS QUARTER

### Decision 1: Shift to Utilities-Led SEO Approach
- **What**: Stop direct app promotion via ads. Instead, build content hub around "how to pay traffic fines", mention app as solution.
- **When**: 2026-04-27
- **Status**: In-Progress (content strategy being finalized)
- **Impact**: Expected to 3x traffic and 2x conversion by 2026-08-31. Lower CAC from organic.
- **Link**: [[Decision-Log-2026#shift-traffic-fines-to-utilities-led-seo]]

## CURRENT BLOCKERS

### Blocker 1: Web Platform Capacity Dependency
- **What**: Content hub requires Web Platform to build templates/structure. Platform is busy with MoSpark until 2026-06-30.
- **Impact**: If Web Platform doesn't deliver by 2026-06-15, we won't have content hub live until Q3. Will delay impact by 4+ weeks.
- **Owner**: Văn Hiến (to align with platform, escalate if needed)
- **Status**: In-progress (content strategy done, waiting for platform eng sign-off)
- **ETA**: 2026-06-30 (when platform more available)

### Blocker 2: Content Team Bandwidth
- **What**: Content team has 2 people, already committed to Inbound blog. Traffic Fines content is 3rd priority.
- **Impact**: Content production slower than ideal (1 article/week vs 2/week needed). Delays content hub launch.
- **Owner**: Content Lead + Klaus (to negotiate priority)
- **Status**: Pending negotiation (scheduled for 2026-05-08 meeting)
- **ETA**: 2026-05-15 (when commitment is confirmed)

## DEPENDENCIES

**Waiting On**:
- Web Platform template + approval: From Bảo → Due 2026-06-15 → Status Pending
- Content creation (5 articles): From Content team → Due 2026-06-30 → Status Pending
- GA4 + GTM tracking setup: From Analytics → Due 2026-05-30 → Status Pending

**This Project Affects**:
- [[Insurance-Mini-App]]: May share content hub infrastructure if it works
- [[Credit-Ecosystem]]: Utilities approach could be template for other finance topics

## NEXT 30 DAYS

- [ ] Finalize content strategy & keyword target list - Due 2026-05-15 - Owner: Klaus
- [ ] Get Web Platform approval on content hub architecture - Due 2026-05-20 - Owner: Văn Hiến
- [ ] Start content creation (Article 1 of 5) - Due 2026-05-30 - Owner: Content team
- [ ] Set up GA4 + GTM tracking for content hub - Due 2026-05-30 - Owner: Analytics
- [ ] Content hub MVP live - Due 2026-06-30 - Owner: Web Platform + Content

## RISK REGISTER

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|-----------|
| Web Platform delays content hub | Medium | High | Weekly check-in on progress; escalate if at risk |
| Content quality insufficient for conversions | Medium | Medium | Review content strategy for user intent match; A/B test messaging |
| Users don't convert app link to install | Low | High | Test multiple CTA positions/messaging in content hub MVP |
| Search volume lower than expected | Low | High | Validate with GSC/keyword research before content production |

```

---

## TIPS FOR KEEPING STATUS CURRENT

**Make it a Ritual**:
- Friday 3pm: Spend 10 min updating metrics + status
- After important meetings: Add blockers/decisions immediately (while fresh)
- Monthly: Do full review (risk, next 30 days, interpretation)

**Minimum Viable Update**:
If you only have 5 minutes:
1. Update current metrics
2. Update status (🟢/🟡/🔴)
3. Update blockers (new, resolved)
4. Done ✓

**Use This For**:
- Weekly 1:1 with manager: Open this doc, they see full context
- Project kickoff: Show team the risks and dependencies
- Stakeholder updates: Copy metrics + status for quick brief
- Decision-making: "Should we allocate more budget?" → Look at metrics + blockers

**When to Escalate**:
- 🔴 Blocked: Escalate blocker immediately (don't wait for Friday update)
- Metrics trending 🔴: Escalate when trend becomes clear (don't wait for end of month)
- Risk likelihood increased: Update risk register + flag stakeholder

---

## DON'T OVERCOMPLICATE IT

This is a **status snapshot**, not a project management system. Goal is:
- ✅ Always know where we stand
- ✅ Know what's blocking us
- ✅ Know what's coming next
- ✅ Reference past decisions

It's not:
- ❌ Daily standup tool
- ❌ Time tracking system
- ❌ Detailed task breakdown
- ❌ Complete project history

If you want that level of detail, use a dedicated PM tool. This is the **knowledge base version** (strategic snapshot).

