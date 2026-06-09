"""Generates a realistic business PDF for RAG demo."""
from fpdf import FPDF
from fpdf.enums import XPos, YPos

FONT_DIR = "/usr/share/fonts/truetype/dejavu/"
INDENT = 8   # bullet indent in mm
W = 165      # usable width after 15mm margins on a 210mm page


class PDF(FPDF):
    def __init__(self):
        super().__init__()
        self.add_font("dv",  fname=FONT_DIR + "DejaVuSans.ttf")
        self.add_font("dv", style="B", fname=FONT_DIR + "DejaVuSans-Bold.ttf")

    def header(self):
        self.set_font("dv", "B", 8)
        self.set_text_color(110, 110, 110)
        self.set_x(15)
        self.multi_cell(W, 6, "CONFIDENTIAL — INTERNAL USE ONLY   |   Meridian Retail Group")
        self.set_draw_color(200, 200, 200)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(3)

    def footer(self):
        self.set_y(-14)
        self.set_font("dv", "", 8)
        self.set_text_color(150, 150, 150)
        self.set_x(15)
        self.multi_cell(W, 6,
            f"Page {self.page_no()} — Meridian Retail Group — AI Strategy Report 2026",
            align="C")

    def section_title(self, text):
        self.ln(5)
        self.set_font("dv", "B", 13)
        self.set_text_color(25, 55, 115)
        self.set_x(15)
        self.multi_cell(W, 8, text)
        self.set_draw_color(25, 55, 115)
        self.set_line_width(0.5)
        self.line(15, self.get_y(), 195, self.get_y())
        self.set_line_width(0.2)
        self.ln(3)
        self.set_text_color(30, 30, 30)

    def sub_title(self, text):
        self.ln(3)
        self.set_font("dv", "B", 10)
        self.set_text_color(40, 40, 40)
        self.set_x(15)
        self.multi_cell(W, 6, text)
        self.set_text_color(30, 30, 30)

    def body(self, text):
        self.set_font("dv", "", 9.5)
        self.set_x(15)
        self.multi_cell(W, 5.5, text)
        self.ln(1)

    def bullet(self, text):
        self.set_font("dv", "", 9.5)
        self.set_x(15 + INDENT)
        self.multi_cell(W - INDENT, 5.5, "•  " + text)

    def kv(self, key, val):
        y_before = self.get_y()
        self.set_font("dv", "B", 9.5)
        self.set_x(15)
        self.multi_cell(68, 5.8, key)
        y_after = self.get_y()
        self.set_xy(83, y_before)
        self.set_font("dv", "", 9.5)
        self.multi_cell(W - 68, 5.8, val)
        if self.get_y() < y_after:
            self.set_y(y_after)

    def table_row(self, col1, col2, col3, bold=False):
        style = "B" if bold else ""
        self.set_font("dv", style, 9)
        self.set_x(15)
        self.cell(85, 6, col1, border="B",
                  new_x=XPos.RIGHT, new_y=YPos.TOP)
        self.cell(50, 6, col2, border="B",
                  new_x=XPos.RIGHT, new_y=YPos.TOP)
        self.cell(30, 6, col3, border="B",
                  new_x=XPos.LMARGIN, new_y=YPos.NEXT)


pdf = PDF()
pdf.set_margins(15, 18, 15)
pdf.set_auto_page_break(auto=True, margin=18)
pdf.add_page()

# ── Cover block ───────────────────────────────────────────────────────────────
pdf.ln(6)
pdf.set_font("dv", "B", 21)
pdf.set_text_color(20, 45, 100)
pdf.set_x(15)
pdf.multi_cell(W, 11,
    "AI-Powered Customer Experience\nTransformation Report", align="C")
pdf.ln(2)
pdf.set_font("dv", "", 11)
pdf.set_text_color(80, 80, 80)
pdf.set_x(15)
pdf.multi_cell(W, 7, "Meridian Retail Group  |  Strategic Technology Division", align="C")
pdf.set_x(15)
pdf.multi_cell(W, 7,
    "Prepared by: Office of the Chief Digital Officer  |  June 2026", align="C")
pdf.ln(5)
pdf.set_draw_color(25, 55, 115)
pdf.set_line_width(0.8)
pdf.line(15, pdf.get_y(), 195, pdf.get_y())
pdf.set_line_width(0.2)
pdf.ln(6)

# ── 1. Executive Summary ──────────────────────────────────────────────────────
pdf.section_title("1. Executive Summary")
pdf.body(
    "Meridian Retail Group (MRG) operates 214 retail outlets across 18 states and processes "
    "approximately 2.3 million customer transactions per month through its digital and in-store "
    "channels. Following a 12% year-over-year decline in customer satisfaction scores (CSAT) "
    "and a 19% increase in support ticket volume in FY 2025, the board of directors approved "
    "a $4.2 million AI Transformation Initiative in Q1 2026."
)
pdf.body(
    "This report outlines the recommended architecture, vendor selections, cost projections, "
    "risk assessment, and 18-month implementation roadmap for deploying AI across three core "
    "business functions: Customer Support Automation, Personalised Marketing, and Supply Chain "
    "Demand Forecasting."
)
pdf.body(
    "Key projected outcomes at 18-month mark: 42% reduction in average support resolution "
    "time, 28% improvement in CSAT scores, $1.8M annual savings in customer operations, "
    "and a projected 11% uplift in repeat-purchase revenue. 3-year NPV: $9.4M. "
    "Break-even modelled at month 17."
)

# ── 2. Problem Statement ──────────────────────────────────────────────────────
pdf.section_title("2. Problem Statement & Business Context")
pdf.sub_title("2.1 Current Operational Pain Points")
pdf.bullet("Support team handles 47,000 tickets/month; 61% are repetitive (order status, returns, billing).")
pdf.bullet("Average first-response time is 6.4 hours; industry benchmark is 1.2 hours.")
pdf.bullet("Customer churn rate increased from 8.1% to 11.4% between Q3 2024 and Q1 2026.")
pdf.bullet("Marketing email open rates dropped to 14.2%, below the 21% industry average.")
pdf.bullet("Stockout events cost an estimated $3.1M in lost revenue in FY 2025.")
pdf.ln(2)

pdf.sub_title("2.2 Strategic Objectives & KPIs")
pdf.body(
    "The initiative directly supports Pillar 3 (Digital-First Customer Experience) and "
    "Pillar 5 (Operational Efficiency) of MRG's five-year strategic plan. "
    "The CDO office has set these non-negotiable KPIs:"
)
pdf.bullet("CSAT score: improve from 3.1/5 to 4.0/5 by December 2026.")
pdf.bullet("Support cost per ticket: reduce from $18.40 to under $9.00.")
pdf.bullet("First-contact resolution rate: increase from 34% to 65%.")
pdf.bullet("Marketing email conversion rate: improve by at least 15% via personalisation.")
pdf.bullet("Stockout incidents: reduce from 142/month to fewer than 57/month.")

# ── 3. Recommended Architecture ───────────────────────────────────────────────
pdf.section_title("3. Recommended AI Architecture")
pdf.sub_title("3.1 Pillar A — Intelligent Customer Support")
pdf.body(
    "We recommend a RAG-based (Retrieval-Augmented Generation) support assistant built on "
    "Google Gemini 2.5 Flash as the primary LLM, with LangChain as the orchestration layer. "
    "Customer queries are routed through an intent classifier before reaching the RAG pipeline. "
    "Tier-1 queries (order status, FAQs) are resolved autonomously; Tier-2 (complaints, "
    "refunds) are escalated to human agents with an AI-generated summary and suggested reply."
)
pdf.body(
    "Vector store: Pinecone (us-east-1 cluster) indexed against MRG's 1,200-page product "
    "knowledge base, return policies, and 480,000 historical resolved tickets. "
    "Estimated index size: 2.1M vectors at 768 dimensions."
)

pdf.sub_title("3.2 Pillar B — Personalised Marketing Engine")
pdf.body(
    "A collaborative filtering model trained on 14 months of purchase history (3.8M "
    "transactions) will power product recommendations in email campaigns and the mobile app. "
    "LLM-generated personalised copy replaces static email templates. Expected to reduce "
    "unsubscribe rates by 22% and increase average order value (AOV) by $12.50."
)

pdf.sub_title("3.3 Pillar C — Demand Forecasting")
pdf.body(
    "A Prophet + XGBoost ensemble model integrated into the ERP system will predict SKU-level "
    "demand 6 weeks in advance across all 214 stores. Training data: 5 years of sales history, "
    "weather data, and promotional calendar. Target: reduce stockouts by 60% and overstock "
    "write-offs by 35%."
)

# ── 4. Vendor Evaluation ──────────────────────────────────────────────────────
pdf.section_title("4. AI Vendor Evaluation & Selection")
pdf.body(
    "The evaluation committee assessed six platforms across five criteria: generation quality, "
    "cost at scale, data privacy compliance, ease of integration with Salesforce and SAP, "
    "and enterprise SLA availability."
)

pdf.sub_title("4.1 Selected Vendors")
pdf.kv("Primary LLM:", "Google Gemini 2.5 Flash — best cost/quality ratio at our query volume; "
       "1M token context window; GDPR compliant via Google Cloud EU region.")
pdf.kv("Embedding Model:", "Gemini Embedding-001 — 768-dim vectors; outperformed OpenAI "
       "text-embedding-3-small by 4.1% on our internal retrieval benchmark.")
pdf.kv("Vector Database:", "Pinecone (Production) / FAISS (Development) — Pinecone chosen "
       "for 99.99% uptime SLA; FAISS used in dev/staging to eliminate cost.")
pdf.kv("Orchestration:", "LangChain 1.x LCEL pipeline — avoids vendor lock-in.")
pdf.kv("MLOps:", "Google Vertex AI Pipelines — auto retraining on drift > 0.08.")
pdf.ln(1)

pdf.sub_title("4.2 Rejected Alternatives")
pdf.bullet("OpenAI GPT-4o: 2.3x higher cost at 180,000 queries/month; US-only data residency "
           "creates GDPR complications for EU customer data.")
pdf.bullet("AWS Bedrock (Claude 3): 14-week procurement vs 3 weeks for GCP; "
           "high integration complexity with non-AWS stack.")
pdf.bullet("Ollama (local models): Insufficient accuracy on intent classification; "
           "$220K GPU CapEx not approved in current budget cycle.")

# ── 5. Budget & Cost ──────────────────────────────────────────────────────────
pdf.section_title("5. Budget Allocation & Cost Analysis")
pdf.sub_title("5.1 Total Approved Budget: $4,200,000")
pdf.kv("Implementation & Integration (Year 1):", "$1,850,000")
pdf.kv("  LangChain/API development (internal):", "$620,000")
pdf.kv("  Pinecone enterprise contract (3-year):", "$180,000")
pdf.kv("  Google Cloud AI APIs (Year 1):", "$340,000")
pdf.kv("  Data engineering & ETL pipelines:", "$410,000")
pdf.kv("  Security audit & compliance:", "$300,000")
pdf.kv("Ongoing Annual Operating Cost (Year 2+):", "$890,000")
pdf.kv("  Gemini API calls ($0.0003/1K tokens):", "$216,000")
pdf.kv("  Pinecone annual renewal:", "$60,000")
pdf.kv("  Monitoring, maintenance, retraining:", "$190,000")
pdf.kv("  Human oversight team (3 FTE):", "$424,000")
pdf.ln(2)
pdf.body(
    "Projected ROI: $1.8M support savings + $2.1M personalisation uplift + $3.1M "
    "stockout reduction = projected 3-year NPV of $9.4M on a $6.87M total investment. "
    "Break-even at month 17."
)

# ── 6. Risk Assessment ────────────────────────────────────────────────────────
pdf.section_title("6. Risk Assessment & Mitigation Strategies")
risks = [
    ("LLM Hallucination in Support Responses", "HIGH", "MEDIUM",
     "RAG grounding mandatory; human-in-the-loop for Tier-2; "
     "judge model scores factuality before delivery."),
    ("Customer Data Privacy (GDPR/CCPA)", "HIGH", "LOW",
     "PII stripped before LLM calls; EU GCP data residency; "
     "DPA signed with Google Cloud; annual privacy audit."),
    ("Model Drift Over Time", "MEDIUM", "MEDIUM",
     "Automated drift detection; quarterly retraining; "
     "fallback to rule-based if accuracy drops below 78%."),
    ("Vendor Lock-in (Google Cloud)", "MEDIUM", "LOW",
     "LangChain abstraction enables swap-out; Anthropic Claude "
     "pre-evaluated as fallback vendor."),
    ("Staff Resistance", "MEDIUM", "LOW",
     "8-week change management; AI framed as augmentation; "
     "$85,000 reskilling budget allocated."),
    ("SAP ERP Integration Failures", "LOW", "HIGH",
     "3-month dedicated integration sprint; SAP consultant "
     "contracted at $120K for Pillar C."),
]
for name, likelihood, impact, mitigation in risks:
    pdf.sub_title(f"Risk: {name}")
    pdf.kv("  Likelihood:", likelihood)
    pdf.kv("  Business Impact:", impact)
    pdf.kv("  Mitigation:", mitigation)
    pdf.ln(1)

# ── 7. Roadmap ────────────────────────────────────────────────────────────────
pdf.section_title("7. 18-Month Implementation Roadmap")
pdf.sub_title("Phase 1 — Foundation (July – September 2026)")
pdf.bullet("Deploy RAG FAQ assistant on web chat; target 30% Tier-1 ticket deflection.")
pdf.bullet("Index full 1,200-document knowledge base into Pinecone.")
pdf.bullet("Set up Grafana monitoring; establish CSAT baselines.")
pdf.bullet("Milestone: First live AI support response by 1 August 2026.")
pdf.ln(1)

pdf.sub_title("Phase 2 — Expansion (October – December 2026)")
pdf.bullet("Extend AI support to email and WhatsApp channels.")
pdf.bullet("Launch personalised recommendations for top 500K customers.")
pdf.bullet("Begin demand forecasting model training on 3 years of sales history.")
pdf.bullet("Milestone: CSAT reaches 3.6/5; cost per ticket below $14.")
pdf.ln(1)

pdf.sub_title("Phase 3 — Full Deployment (January – December 2027)")
pdf.bullet("Demand forecasting live across all 214 stores; ERP integration complete.")
pdf.bullet("AI recommendations active for all 2.1M registered customers.")
pdf.bullet("AI writes and A/B tests all promotional email campaigns.")
pdf.bullet("Milestone: All KPIs from Section 2.2 achieved by December 2027.")

# ── 8. Governance ─────────────────────────────────────────────────────────────
pdf.section_title("8. Governance & Success Metrics")
pdf.sub_title("8.1 Steering Committee")
pdf.kv("Executive Sponsor:", "Ms. Priya Nair, Chief Digital Officer")
pdf.kv("Programme Director:", "Mr. James Okafor, VP of Technology")
pdf.kv("AI Ethics Lead:", "Dr. Lena Hoffmann, Head of Data & Privacy")
pdf.kv("Delivery Partner:", "InnovateTech Consulting Ltd. (ref: MRG-2026-0042)")
pdf.ln(2)

pdf.sub_title("8.2 Quarterly Review Cadence")
pdf.body(
    "Steering committee convenes first Monday of each quarter. A go/no-go gate is "
    "scheduled 30 September 2026 before Phase 2 funding is released. "
    "Independent QA review by KPMG scheduled for Q2 2027."
)

pdf.sub_title("8.3 Monthly KPI Dashboard")
pdf.table_row("Metric", "Current Baseline", "Target", bold=True)
for row in [
    ("Tickets resolved autonomously", "0%", "55%"),
    ("Avg. first-response time", "6.4 hours", "< 45 min"),
    ("CSAT score", "3.1 / 5.0", "4.0 / 5.0"),
    ("Support cost per ticket", "$18.40", "< $9.00"),
    ("Email click-through rate", "3.8%", "6.5%"),
    ("Stockout incidents / month", "142", "< 57"),
    ("Repeat-purchase revenue uplift", "Baseline", "+ 11%"),
]:
    pdf.table_row(*row)

pdf.ln(4)
pdf.set_font("dv", "", 8.5)
pdf.set_text_color(110, 110, 110)
pdf.set_x(15)
pdf.multi_cell(W, 5,
    "CONFIDENTIAL — Document ref: MRG-CDO-2026-AI-001 | Version 2.1 | 5 June 2026. "
    "Reproduction outside Meridian Retail Group without CDO written approval is prohibited."
)

out = "sample_docs/meridian_retail_ai_strategy.pdf"
pdf.output(out)
print(f"Generated: {out}  ({pdf.page} pages)")
