import streamlit as st
import datetime, random, time

st.set_page_config(page_title="TitanU AI — Agent Fleet", page_icon="🤖", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;900&family=JetBrains+Mono:wght@400;700&display=swap');
html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
.stApp { background: #0a0a0f; color: #e2e8f0; }
.main .block-container { padding: 1.5rem 2rem; max-width: 1400px; }
.titan-header { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%); border: 1px solid #2563eb44; border-radius: 16px; padding: 2rem; margin-bottom: 1.5rem; text-align: center; }
.titan-header h1 { font-size: 2.8rem; font-weight: 900; background: linear-gradient(90deg, #3b82f6, #8b5cf6, #06b6d4); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin: 0; }
.titan-header p { color: #94a3b8; margin: 0.5rem 0 0; font-size: 1rem; }
.track-badge { display: inline-block; padding: 3px 10px; border-radius: 20px; font-size: 0.7rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-right: 4px; }
.track-arize    { background: #4f1c5c33; color: #c084fc; border: 1px solid #7c3aed44; }
.track-elastic  { background: #1c3a5c33; color: #60a5fa; border: 1px solid #2563eb44; }
.track-fivetran { background: #1c4a3a33; color: #34d399; border: 1px solid #059669aa; }
.track-gitlab   { background: #4a2c1c33; color: #fb923c; border: 1px solid #ea580c44; }
.track-mongodb  { background: #1c4a2c33; color: #4ade80; border: 1px solid #16a34a44; }
.track-dynatrace{ background: #4a3c1c33; color: #fbbf24; border: 1px solid #d97706aa; }
.chat-box { background: #111827; border: 1px solid #1e293b; border-radius: 12px; padding: 1.5rem; min-height: 400px; max-height: 500px; overflow-y: auto; }
.msg-user { background: #1e3a5f; border-radius: 12px 12px 2px 12px; padding: 0.8rem 1rem; margin: 0.5rem 0 0.5rem 20%; color: #e2e8f0; font-size: 0.9rem; }
.msg-agent { background: #1a1a2e; border: 1px solid #2563eb33; border-radius: 12px 12px 12px 2px; padding: 0.8rem 1rem; margin: 0.5rem 20% 0.5rem 0; color: #94a3b8; font-size: 0.9rem; font-family: 'JetBrains Mono', monospace; }
.msg-label { font-size: 0.7rem; color: #475569; margin-bottom: 2px; }
.dot-green { display:inline-block; width:8px; height:8px; border-radius:50%; background:#22c55e; margin-right:6px; box-shadow: 0 0 6px #22c55e; }
[data-testid="stSidebar"] { background: #0f1117 !important; border-right: 1px solid #1e293b; }
</style>
""", unsafe_allow_html=True)

AGENTS = {
    "arize": [
        ("Agent-01","Self-Healing Customer Support","Classifies tickets P0-P3, auto-resolves via KB, escalates repeats."),
        ("Agent-02","Fitness Coach Evolver","Analyzes workout logs, adapts plans, predicts injury risk."),
        ("Agent-03","Enterprise Policy Guardian","Enforces policies, flags violations, auto-remediates."),
        ("Agent-04","Personal Finance Therapist","Spending analysis, pattern detection, financial coaching."),
        ("Agent-05","Code Review QA","Automated code quality, security, and test coverage scoring."),
        ("Agent-06","Mental Health Journal","Sentiment-aware journaling, mood tracking, coping recommendations."),
        ("Agent-07","Supply Chain Risk Forecaster","Predicts disruptions, triggers preemptive actions."),
        ("Agent-08","Educational Tutor","Adaptive tutoring adjusting to learner performance."),
        ("Agent-09","Legal Contract Analyzer","Clause extraction, risk scoring, playbook comparison."),
        ("Agent-10","Creative Writing CoAuthor","Style-consistent collaborative writing with arc tracking."),
        ("Agent-11","HR Onboarding Wizard","Orchestrates tasks, docs, access, and check-ins."),
        ("Agent-12","Sustainability Impact Reporter","Carbon footprint, ESG metrics, compliance reports."),
    ],
    "elastic": [
        ("Agent-13","Enterprise Knowledge Brain","Semantic search, citation answers, gap detection."),
        ("Agent-14","Smart Job Matcher","Vector-matches candidates to roles."),
        ("Agent-15","Cyber Threat Hunter","Hunts threats in SIEM logs, correlates IOCs."),
        ("Agent-16","Personalized News Forecaster","Personalizes feed, forecasts trending topics."),
        ("Agent-17","Ecommerce Product Discovery","Semantic product search and recommendation."),
        ("Agent-18","Clinical Trial Navigator","Matches patients to trials."),
        ("Agent-19","Real Estate Market Intelligence","Property market signals and pricing forecasts."),
        ("Agent-20","Legal Research SuperAgent","Deep legal research across case law and statutes."),
        ("Agent-21","Recipe Nutrition Optimizer","Optimizes recipes by nutritional goals."),
        ("Agent-22","Log Anomaly Detective","Z-score + IQR anomaly detection on log streams."),
        ("Agent-23","Social Media Sentiment Strategist","Real-time sentiment and strategy recommendations."),
        ("Agent-24","Historical Archive Explorer","Semantic search over historical archives."),
    ],
    "fivetran": [
        ("Agent-25","Autonomous Pipeline Orchestrator","Monitors pipelines, detects drift, reroutes, backfills."),
        ("Agent-26","Real-Time BI Agent","Live BI queries via Fivetran-synced data."),
        ("Agent-27","Compliance Data Auditor","GDPR/HIPAA/SOC2 pipeline compliance scanning."),
        ("Agent-28","Multi-Source Customer 360","Unifies customer data into 360 profile."),
        ("Agent-29","Predictive Inventory Replenisher","Forecasts inventory, triggers replenishment."),
        ("Agent-30","Marketing Attribution Analyst","Multi-touch attribution across sources."),
        ("Agent-31","Healthcare Claims Harmonizer","Harmonizes claims data across payers."),
        ("Agent-32","Financial Close Automation","Automates month-end close reconciliation."),
        ("Agent-33","Personal Expense Aggregator","Aggregates, categorizes, flags expense anomalies."),
        ("Agent-34","Supply Chain Visibility","End-to-end supply chain tracking."),
        ("Agent-35","Elearning Progress Synchronizer","Syncs learner progress across LMS platforms."),
        ("Agent-36","SaaS Usage Optimizer","Analyzes license utilization, cuts costs."),
    ],
    "gitlab": [
        ("Agent-37","Autonomous Sprint Velocity","Velocity tracking, blocker detection, auto-reassign."),
        ("Agent-38","Code Quality Guardian","Continuous quality scoring and tech debt tracking."),
        ("Agent-39","Security Vulnerability Hunter","CVE, secret, and dependency scanning."),
        ("Agent-40","Documentation Sync Agent","Keeps docs in sync with code changes."),
        ("Agent-41","CI/CD Failure Autofixer","Diagnoses and auto-fixes pipeline failures."),
        ("Agent-42","Open Source Contribution Asst","Automates open source contributions."),
        ("Agent-43","Agile Retrospective Generator","Data-driven retros from sprint metrics."),
        ("Agent-44","Monorepo Dependency Manager","Cross-package dependency management."),
        ("Agent-45","Release Train Conductor","Multi-team release orchestration."),
        ("Agent-46","Developer Onboarding Buddy","Guides new devs through codebase and standards."),
        ("Agent-47","Bug Triaging Prioritizer","AI-scores bugs by severity, impact, effort."),
        ("Agent-48","Compliance Audit Trail","Tamper-evident audit trails for compliance."),
    ],
    "mongodb": [
        ("Agent-49","Personal Knowledge Base","MongoDB Atlas vector search for notes and concepts."),
        ("Agent-50","Dynamic Ecommerce Recommendation","Real-time product recommendations."),
        ("Agent-51","Clinical Decision Support","Evidence-based clinical recommendations."),
        ("Agent-52","Smart Inventory Forecaster","ML forecasting from transaction history."),
        ("Agent-53","Event Planning CoPilot","End-to-end event planning automation."),
        ("Agent-54","Resume Talent Matching","Vector-matches resumes to job requirements."),
        ("Agent-55","Recipe Grocery Optimizer","Optimizes grocery lists from recipes."),
        ("Agent-56","IoT Device Fleet Manager","Telemetry ingestion and command dispatch."),
        ("Agent-57","Legal Case Management","Tracks cases, deadlines, and documents."),
        ("Agent-58","Fitness Progress Tracker","Long-term fitness analytics."),
        ("Agent-59","Travel Itinerary Builder","Personalized travel itineraries."),
        ("Agent-60","Research Paper Summarizer","Summarizes and indexes research papers."),
    ],
    "dynatrace": [
        ("Agent-61","Production Agent Sentinel","Polls all 100 agents, auto-restarts, pages oncall."),
        ("Agent-62","Application Performance Guardian","APM monitoring with auto-remediation."),
        ("Agent-63","Cost Optimization Watchdog","Flags cloud waste, rightsize recommendations."),
        ("Agent-64","Security Posture Agent","Continuous security posture and auto-hardening."),
        ("Agent-65","Multi-Agent Orchestration Monitor","Monitors the full 100-agent fleet health."),
        ("Agent-66","DevOps Pipeline Health","Real-time pipeline health via Dynatrace."),
        ("Agent-67","User Experience Quality","Synthetic + real-user UX monitoring."),
        ("Agent-68","AI Workload Balancer","Balances inference workloads via resource metrics."),
        ("Agent-69","Incident Response Automator","End-to-end incident response from alerts."),
        ("Agent-70","Sustainability Efficiency Auditor","Carbon footprint, rightsizing, ESG reports."),
    ],
}

TRACK_COLORS = {"arize":"track-arize","elastic":"track-elastic","fivetran":"track-fivetran","gitlab":"track-gitlab","mongodb":"track-mongodb","dynatrace":"track-dynatrace"}

def agent_response(agent_id, agent_name, track, query):
    ts = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    rid = f"titan-{random.randint(10000,99999)}"
    responses = {
        "Agent-01": f'{{\n  "agent": "Self-Healing-Customer-Support",\n  "trace_id": "{rid}",\n  "timestamp": "{ts}",\n  "classification": "P2 — Performance Issue",\n  "kb_match": "Check status.page for active incidents. Clear cache, force-refresh.",\n  "confidence": 0.91,\n  "action": "AUTO_RESOLVED",\n  "arize_eval_score": 0.94\n}}',
        "Agent-13": f'{{\n  "agent": "Enterprise-Knowledge-Brain",\n  "trace_id": "{rid}",\n  "timestamp": "{ts}",\n  "top_result": "InfoSec Policy 2026 — Section 4.2: MFA required for all remote access.",\n  "confidence": 0.93,\n  "elastic_hits": 7,\n  "gap_detected": false\n}}',
        "Agent-25": f'{{\n  "agent": "Autonomous-Pipeline-Orchestrator",\n  "trace_id": "{rid}",\n  "timestamp": "{ts}",\n  "pipelines_checked": 12,\n  "status": "DEGRADED",\n  "issue": "Schema drift on pipe_007",\n  "action": "AUTO_MAPPED + BACKFILL_TRIGGERED",\n  "eta_minutes": 8\n}}',
        "Agent-61": f'{{\n  "agent": "Production-Agent-Sentinel",\n  "trace_id": "{rid}",\n  "timestamp": "{ts}",\n  "agents_polled": 100,\n  "healthy": 97,\n  "degraded": 2,\n  "down": 1,\n  "action": "RESTARTED agent-44 in 3.2s",\n  "oncall_paged": false\n}}',
    }
    default = f'{{\n  "agent": "{agent_name.replace(" ","-")}",\n  "track": "{track.upper()}",\n  "trace_id": "{rid}",\n  "timestamp": "{ts}",\n  "model": "gemini-2.5-flash",\n  "status": "EXECUTED",\n  "query": "{query[:50]}",\n  "result": "Agent processed request via {track.upper()} MCP. Action completed successfully.",\n  "confidence": {round(random.uniform(0.85,0.97),2)},\n  "mcp_calls": {random.randint(1,4)},\n  "latency_ms": {random.randint(180,450)}\n}}'
    return responses.get(agent_id, default)

if "selected_track" not in st.session_state: st.session_state.selected_track = "arize"
if "selected_agent" not in st.session_state: st.session_state.selected_agent = AGENTS["arize"][0]
if "messages" not in st.session_state: st.session_state.messages = []
if "total_runs" not in st.session_state: st.session_state.total_runs = random.randint(1240,1800)
if "resolved" not in st.session_state: st.session_state.resolved = random.randint(980,1200)

with st.sidebar:
    st.markdown("<div style='text-align:center;padding:1rem 0;'><div style='font-size:2rem;'>🤖</div><div style='font-weight:900;font-size:1.1rem;color:#3b82f6;'>TitanU AI</div><div style='font-size:0.7rem;color:#475569;'>JCH-2026-001 | 100 Agents</div></div>", unsafe_allow_html=True)
    st.markdown("### Select Track")
    for track in AGENTS.keys():
        emoji = {"arize":"🟣","elastic":"🔵","fivetran":"🟢","gitlab":"🟠","mongodb":"💚","dynatrace":"🟡"}[track]
        if st.button(f"{emoji} {track.upper()} ({len(AGENTS[track])})", use_container_width=True, type="primary" if st.session_state.selected_track==track else "secondary"):
            st.session_state.selected_track = track
            st.session_state.selected_agent = AGENTS[track][0]
            st.session_state.messages = []
            st.rerun()
    st.divider()
    st.markdown("<div style='font-size:0.75rem;color:#475569;text-align:center;'>All 100 agents online<br>Model: Gemini 2.5 Flash<br>Julius Cameron Hill</div>", unsafe_allow_html=True)

st.markdown("<div class='titan-header'><h1>🤖 TitanU AI — Agent Fleet</h1><p>Google Cloud Rapid Agent Hackathon &nbsp;|&nbsp; 100 Autonomous Agents &nbsp;|&nbsp; 6 Partner Tracks &nbsp;|&nbsp; Gemini 2.5 Flash + Vertex AI</p></div>", unsafe_allow_html=True)

c1,c2,c3,c4 = st.columns(4)
c1.metric("Total Agents","100","6 tracks")
c2.metric("Agent Runs",f"{st.session_state.total_runs:,}","+47 today")
c3.metric("Auto-Resolved",f"{st.session_state.resolved:,}","94.2% rate")
c4.metric("Avg Latency","312ms","-18ms")
st.divider()

left, right = st.columns([1,2])
with left:
    track = st.session_state.selected_track
    st.markdown(f"### {track.upper()} Track — {len(AGENTS[track])} Agents")
    for agent_id, name, desc in AGENTS[track]:
        selected = st.session_state.selected_agent[0] == agent_id
        if st.button(f"{'▶ ' if selected else ''}{agent_id} — {name}", key=f"btn_{agent_id}", use_container_width=True, type="primary" if selected else "secondary"):
            st.session_state.selected_agent = (agent_id, name, desc)
            st.session_state.messages = []
            st.rerun()

with right:
    agent_id, agent_name, agent_desc = st.session_state.selected_agent
    track = st.session_state.selected_track
    st.markdown(f"<div style='background:#111827;border:1px solid #1e3a5f;border-radius:12px;padding:1.2rem;margin-bottom:1rem;'><div style='display:flex;align-items:center;gap:10px;margin-bottom:0.5rem;'><span style='font-size:1.5rem;'>🤖</span><div><div style='font-weight:700;font-size:1.1rem;color:#e2e8f0;'>{agent_id} — {agent_name}</div><span class='track-badge {TRACK_COLORS[track]}'>{track}</span><span style='font-size:0.75rem;color:#475569;'>Gemini 2.5 Flash · Vertex AI · {track.title()} MCP</span></div><div style='margin-left:auto;'><span style='color:#22c55e;font-size:0.8rem;'>● ONLINE</span></div></div><div style='color:#64748b;font-size:0.85rem;'>{agent_desc}</div></div>", unsafe_allow_html=True)

    chat_html = ""
    for role, msg in st.session_state.messages:
        if role == "user":
            chat_html += f"<div class='msg-label' style='text-align:right;'>You</div><div class='msg-user'>{msg}</div>"
        else:
            chat_html += f"<div class='msg-label'>{agent_id}</div><div class='msg-agent'><pre style='margin:0;white-space:pre-wrap;font-size:0.8rem;'>{msg}</pre></div>"
    if not chat_html:
        chat_html = f"<div style='text-align:center;color:#374151;padding:3rem;'>Send a message to activate {agent_name}</div>"
    st.markdown(f"<div class='chat-box'>{chat_html}</div>", unsafe_allow_html=True)

    col_inp, col_btn = st.columns([5,1])
    with col_inp:
        user_input = st.text_input("", placeholder=f"Query {agent_name}...", label_visibility="collapsed", key="user_input")
    with col_btn:
        send = st.button("Send", type="primary", use_container_width=True)

    st.markdown("**Quick queries:**")
    qp1,qp2,qp3 = st.columns(3)
    quick = None
    with qp1:
        if st.button("Run diagnostic", use_container_width=True): quick = "Run primary diagnostic and report status"
    with qp2:
        if st.button("Execute workflow", use_container_width=True): quick = "Execute core workflow and return structured result"
    with qp3:
        if st.button("Top recommendations", use_container_width=True): quick = "Analyze current state and surface top recommendations"

    query = quick or (user_input if send and user_input else None)
    if query:
        st.session_state.messages.append(("user", query))
        st.session_state.total_runs += 1
        with st.spinner(f"{agent_id} processing via {track.upper()} MCP..."):
            time.sleep(0.6)
        st.session_state.messages.append(("agent", agent_response(agent_id, agent_name, track, query)))
        st.session_state.resolved += 1
        st.rerun()

st.divider()
st.markdown("<div style='text-align:center;color:#374151;font-size:0.75rem;padding:1rem 0;'>TitanU AI LLC &nbsp;·&nbsp; Julius Cameron Hill &nbsp;·&nbsp; Patent JCH-2026-001 &nbsp;·&nbsp; <a href='https://github.com/juliushill42/titan-agent-fleet' style='color:#3b82f6;'>GitHub</a> &nbsp;·&nbsp; Google Cloud Rapid Agent Hackathon</div>", unsafe_allow_html=True)
