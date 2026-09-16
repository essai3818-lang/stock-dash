from __future__ import annotations

import html
import streamlit as st


def apply_theme():
    st.markdown("""
<style>
:root{--navy:#0b1f3a;--blue:#2563eb;--bg:#f6f9fd;--line:#e5eaf2;--text:#0f172a;--muted:#64748b}
html,body,[class*="css"]{font-family:Pretendard,"Noto Sans KR","Apple SD Gothic Neo",sans-serif}
.stApp{background:var(--bg);color:var(--text)}
.block-container{max-width:1500px;padding:1.25rem 1.6rem 4rem}
header[data-testid="stHeader"]{background:rgba(246,249,253,.9);backdrop-filter:blur(12px)}
section[data-testid="stSidebar"]{background:linear-gradient(180deg,#0b1f3a 0%,#102746 100%);border-right:0}
section[data-testid="stSidebar"]>div{padding:.9rem .85rem}
[data-testid="stSidebar"] .stRadio>label{display:none}
[data-testid="stSidebar"] .stRadio div[role="radiogroup"]{gap:7px}
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label{border-radius:10px;padding:10px 12px;color:#d9e5f5;transition:.15s}
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label:hover{background:rgba(255,255,255,.08)}
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label:has(input:checked){background:linear-gradient(90deg,#215db8,#2c68c8);color:#fff;font-weight:750;box-shadow:0 5px 18px rgba(0,0,0,.16)}
[data-testid="stSidebar"] [data-testid="stCaptionContainer"] p,[data-testid="stSidebar"] label{color:#a9bbd2}
[data-testid="stSidebar"] hr{border-color:rgba(255,255,255,.12)!important}
[data-testid="stSidebar"] .stButton button{background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.1);color:#fff}
h1,h2,h3,h4{color:var(--text);letter-spacing:-.035em}h1{font-weight:800}h2,h3{font-weight:760}
[data-testid="stMetric"]{background:#fff;border:1px solid var(--line);border-radius:14px;padding:15px 17px;box-shadow:0 6px 22px rgba(15,23,42,.035)}
[data-testid="stMetricLabel"]{color:var(--muted)}[data-testid="stMetricValue"]{font-weight:800;color:var(--text)}
[data-testid="stVerticalBlockBorderWrapper"]{border-color:var(--line)!important;border-radius:14px!important;background:#fff;box-shadow:0 6px 22px rgba(15,23,42,.03)}
.stButton>button,.stFormSubmitButton>button{border-radius:10px;min-height:2.6rem;font-weight:700}
.stButton>button[kind="primary"],.stFormSubmitButton>button[kind="primary"]{background:var(--blue);border-color:var(--blue)}
.stTextInput input,.stTextArea textarea,.stSelectbox div[data-baseweb="select"]>div{border-radius:11px!important}
.stDataFrame{border:1px solid var(--line);border-radius:12px;overflow:hidden}
.planx-brand{display:flex;align-items:center;gap:10px;margin:5px 0 26px}.planx-brand-mark{width:36px;height:36px;border-radius:10px;display:flex;align-items:center;justify-content:center;background:linear-gradient(145deg,#3b82f6,#60a5fa);color:#fff;font-size:20px;font-weight:800;box-shadow:0 5px 14px rgba(37,99,235,.25)}
.planx-brand-title{font-size:19px;line-height:1.15;font-weight:800;color:#fff}.planx-brand-sub{font-size:10px;color:#8fa7c5;margin-top:3px}
.planx-hero{background:linear-gradient(135deg,#fff 0%,#f8fbff 65%,#edf5ff 100%);border:1px solid #e1e8f2;border-radius:18px;padding:24px 27px;margin-bottom:15px;box-shadow:0 10px 30px rgba(15,23,42,.04)}
.planx-eyebrow{color:var(--blue);font-size:11px;font-weight:800;letter-spacing:.1em;text-transform:uppercase;margin-bottom:6px}.planx-hero h1{margin:0;font-size:32px;line-height:1.2}.planx-hero p{margin:8px 0 0;color:#64748b;font-size:14px}
.planx-card{background:#fff;border:1px solid var(--line);border-radius:14px;padding:17px 18px;min-height:112px;box-shadow:0 6px 20px rgba(15,23,42,.025)}
.planx-card-title{font-size:12px;color:#64748b;margin-bottom:7px;font-weight:700}.planx-card-value{font-size:23px;color:#0f172a;font-weight:800;letter-spacing:-.035em}.planx-card-note{margin-top:6px;font-size:11px;color:#94a3b8}
.planx-empty{background:#fff;border:1px dashed #cbd5e1;border-radius:14px;padding:20px;color:#64748b}.planx-source{display:inline-flex;align-items:center;gap:5px;color:#64748b;background:#f8fafc;border:1px solid #e2e8f0;padding:4px 8px;border-radius:999px;font-size:10px}.planx-status-ok{color:#047857;background:#ecfdf5;border-color:#a7f3d0}.planx-status-wait{color:#92400e;background:#fffbeb;border-color:#fde68a}.planx-status-bad{color:#b91c1c;background:#fef2f2;border-color:#fecaca}
.dashboard-greeting{display:flex;align-items:center;justify-content:space-between;gap:20px;margin:4px 0 20px}.dashboard-greeting h1{margin:0;font-size:30px}.dashboard-greeting p{margin:5px 0 0;color:#64748b}.dashboard-search{background:#fff;border:1px solid var(--line);border-radius:999px;padding:10px 16px;color:#94a3b8;min-width:280px;text-align:center}
.dash-section{font-size:19px;font-weight:800;margin:20px 0 10px}.dash-title{font-size:17px;font-weight:800;margin-bottom:10px}.dash-muted{font-size:12px;color:#94a3b8}.dash-up{color:#ef3340}.dash-down{color:#16835b}.dash-pill{display:inline-block;padding:4px 8px;border-radius:999px;background:#eff6ff;color:#2563eb;font-size:11px;font-weight:700}
@media(max-width:900px){.block-container{padding-left:1rem;padding-right:1rem}.dashboard-greeting{align-items:flex-start;flex-direction:column}.dashboard-search{width:100%;min-width:0}.planx-hero h1{font-size:27px}}
</style>
""",unsafe_allow_html=True)


def brand():
    st.markdown('<div class="planx-brand"><div class="planx-brand-mark">↗</div><div><div class="planx-brand-title">나의 주식대시보드</div><div class="planx-brand-sub">오늘도, 더 나은 투자를 위해</div></div></div>',unsafe_allow_html=True)


def hero(title: str, subtitle: str, eyebrow: str = "PLANX INVESTMENT OS"):
    st.markdown(f'<div class="planx-hero"><div class="planx-eyebrow">{html.escape(eyebrow)}</div><h1>{html.escape(title)}</h1><p>{html.escape(subtitle)}</p></div>',unsafe_allow_html=True)


def card(title: str, value: str, note: str = "", status: str = ""):
    extra=f'<div class="planx-card-note">{html.escape(status)}</div>' if status else ''
    st.markdown(f'<div class="planx-card"><div class="planx-card-title">{html.escape(title)}</div><div class="planx-card-value">{html.escape(value)}</div><div class="planx-card-note">{html.escape(note)}</div>{extra}</div>',unsafe_allow_html=True)


def empty_state(title: str, message: str):
    st.markdown(f'<div class="planx-empty"><strong style="color:#334155">{html.escape(title)}</strong><br><span>{html.escape(message)}</span></div>',unsafe_allow_html=True)


def source_badge(label: str, state: str = "wait"):
    cls={"ok":"planx-status-ok","bad":"planx-status-bad"}.get(state,"planx-status-wait")
    st.markdown(f'<span class="planx-source {cls}">{html.escape(label)}</span>',unsafe_allow_html=True)
