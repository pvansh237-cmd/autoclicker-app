import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="AutoClicker Dashboard", page_icon="🖱️", layout="centered")

st.markdown("""
<style>
.main { padding-top: 1.5rem; }
.dashboard-header { text-align: center; padding: 1rem 0 0.5rem; }
.dashboard-header h1 { font-size: 2.2rem; margin-bottom: 0.2rem; }
.dashboard-header p { color: #888; font-size: 0.95rem; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="dashboard-header">
    <h1>🖱️ AutoClicker Dashboard</h1>
    <p>Ye button asli click event se click hota hai — Start dabao aur dekho</p>
</div>
""", unsafe_allow_html=True)

components.html("""
<div style="font-family: sans-serif; text-align:center; padding: 1rem;">

  <div id="target"
       style="display:inline-block; width:220px; padding:28px 0; margin:20px auto;
              background:#e74c3c; color:white; font-size:22px; font-weight:bold;
              border-radius:16px; cursor:pointer; user-select:none;
              transition: transform 0.08s ease, background 0.08s ease;">
    CLICK ME
  </div>

  <div style="font-size:15px; color:#555; margin-bottom:12px;">
    Real clicks fired on this button: <b id="count" style="font-size:20px; color:#111;">0</b>
  </div>

  <div>
    <input type="number" id="interval" value="500" min="50" step="50"
           style="width:90px; padding:6px; border-radius:8px; border:1px solid #ccc; text-align:center;">
    <label style="font-size:13px; color:#777;">ms interval</label>
  </div>

  <div style="margin-top:14px;">
    <button id="startBtn" style="padding:10px 24px; font-size:15px; font-weight:bold;
            background:#2ecc71; color:white; border:none; border-radius:8px; cursor:pointer; margin-right:8px;">
      Start
    </button>
    <button id="stopBtn" style="padding:10px 24px; font-size:15px; font-weight:bold;
            background:#7f8c8d; color:white; border:none; border-radius:8px; cursor:pointer;">
      Stop
    </button>
  </div>

  <div id="status" style="margin-top:14px; font-weight:bold; color:#999;">Status: Stopped</div>

</div>

<script>
  const target = document.getElementById("target");
  const countEl = document.getElementById("count");
  const statusEl = document.getElementById("status");
  const intervalInput = document.getElementById("interval");
  let count = 0;
  let timer = null;

  target.addEventListener("click", function() {
    count++;
    countEl.innerText = count;
    target.style.transform = "scale(0.92)";
    target.style.background = "#c0392b";
    setTimeout(() => {
      target.style.transform = "scale(1)";
      target.style.background = "#e74c3c";
    }, 80);
  });

  document.getElementById("startBtn").addEventListener("click", function() {
    if (timer) return;
    const ms = parseInt(intervalInput.value) || 500;
    statusEl.innerText = "Status: Running";
    statusEl.style.color = "#2ecc71";
    timer = setInterval(() => {
      target.click();
    }, ms);
  });

  document.getElementById("stopBtn").addEventListener("click", function() {
    clearInterval(timer);
    timer = null;
    statusEl.innerText = "Status: Stopped";
    statusEl.style.color = "#999";
  });
</script>
""", height=420)

st.caption("Ye button asli DOM click event se click hota hai (button.click() se), page ke andar hi — "
           "isliye press animation aur counter dono real click ke response mein badalte hain.")