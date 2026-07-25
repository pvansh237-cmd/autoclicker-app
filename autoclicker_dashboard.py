import streamlit as st
from streamlit_autorefresh import st_autorefresh
import time

st.set_page_config(page_title="AutoClicker Dashboard", page_icon="🖱️", layout="centered")

# ---------------- Custom styling ----------------
st.markdown("""
<style>
.main { padding-top: 1.5rem; }
.dashboard-header {
    text-align: center;
    padding: 1.5rem 0 0.5rem;
}
.dashboard-header h1 {
    font-size: 2.2rem;
    margin-bottom: 0.2rem;
}
.dashboard-header p {
    color: #888;
    font-size: 0.95rem;
}
.status-card {
    padding: 1.2rem;
    border-radius: 14px;
    text-align: center;
    font-weight: 600;
    font-size: 1.1rem;
    margin: 1rem 0;
}
.status-running { background: rgba(46, 204, 113, 0.15); color: #2ecc71; border: 1px solid #2ecc71; }
.status-stopped { background: rgba(150, 150, 150, 0.15); color: #999; border: 1px solid #666; }
div.stButton > button {
    height: 3rem;
    font-size: 1.05rem;
    font-weight: 600;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- Session state ----------------
if "click_count" not in st.session_state:
    st.session_state.click_count = 0
if "running" not in st.session_state:
    st.session_state.running = False
if "start_time" not in st.session_state:
    st.session_state.start_time = None

# ---------------- Header ----------------
st.markdown("""
<div class="dashboard-header">
    <h1>🖱️ AutoClicker Dashboard</h1>
    <p>Control panel — start, stop aur live stats ek jagah</p>
</div>
""", unsafe_allow_html=True)

# ---------------- Metrics row ----------------
m1, m2, m3 = st.columns(3)
elapsed = (time.time() - st.session_state.start_time) if st.session_state.start_time and st.session_state.running else 0
cps = (st.session_state.click_count / elapsed) if elapsed > 0 else 0

with m1:
    st.metric("Total clicks", st.session_state.click_count)
with m2:
    st.metric("Elapsed (s)", f"{elapsed:.1f}")
with m3:
    st.metric("Clicks / sec", f"{cps:.2f}")

st.divider()

# ---------------- Settings ----------------
interval_ms = st.slider("Click interval (ms)", min_value=100, max_value=5000, value=1000, step=100)

# ---------------- Big control buttons ----------------
c1, c2, c3 = st.columns(3)
with c1:
    if st.button("▶  Start", use_container_width=True, disabled=st.session_state.running, type="primary"):
        st.session_state.running = True
        st.session_state.start_time = time.time()
        st.rerun()
with c2:
    if st.button("⏹  Stop", use_container_width=True, disabled=not st.session_state.running):
        st.session_state.running = False
        st.rerun()
with c3:
    if st.button("🔄  Reset", use_container_width=True):
        st.session_state.click_count = 0
        st.session_state.running = False
        st.session_state.start_time = None
        st.rerun()

# ---------------- Status card ----------------
if st.session_state.running:
    st.markdown('<div class="status-card status-running">Status: Running ✅</div>', unsafe_allow_html=True)
    st_autorefresh(interval=interval_ms, key="autoclick_refresh")
    st.session_state.click_count += 1
else:
    st.markdown('<div class="status-card status-stopped">Status: Stopped ⏸</div>', unsafe_allow_html=True)

st.caption("Browser-based apps sirf apne page ke andar hi click simulate kar sakte hain — "
           "OS ya doosre apps par real click nahi bhej sakte (security restriction).")