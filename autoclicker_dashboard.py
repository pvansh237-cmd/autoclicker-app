import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="AutoClicker", page_icon="🖱️", layout="wide")

st.markdown("<h2 style='text-align:center;'>🖱️ AutoClicker</h2>", unsafe_allow_html=True)
st.caption("Mouse ko is area ke andar kahi bhi rakho, Start dabao — wahi ka element real click hoga.")

components.html("""
<style>
  * { box-sizing: border-box; }
  html, body { margin: 0; font-family: Arial, sans-serif; background: #f4f4f4; }
  #panel {
    position: fixed; top: 16px; left: 16px;
    background: #1c1b1a; color: #f0eadc;
    padding: 14px 18px; border-radius: 12px;
    z-index: 999999; width: 220px;
    box-shadow: 0 4px 14px rgba(0,0,0,0.25);
  }
  #panel h3 { margin: 0 0 10px; font-size: 15px; }
  #panel label { font-size: 12px; color: #b0aca0; display:block; margin-bottom:4px; }
  #panel input {
    width: 100%; padding: 6px; margin-bottom: 10px;
    border-radius: 6px; border: 1px solid #444; background: #262421; color: #fff;
  }
  #panel button {
    width: 100%; padding: 9px; margin-bottom: 6px;
    border: none; border-radius: 6px; font-weight: bold; cursor: pointer;
  }
  #startBtn { background: #2ecc71; color: #111; }
  #stopBtn { background: #e74c3c; color: #fff; }
  #status, #count { font-size: 12px; text-align: center; color: #999; }

  .ripple {
    position: fixed; width: 24px; height: 24px; border-radius: 50%;
    border: 2px solid #2ecc71; transform: translate(-50%, -50%) scale(0.3);
    opacity: 0.9; pointer-events: none; z-index: 999998;
    animation: rip 0.35s ease-out forwards;
  }
  @keyframes rip { to { transform: translate(-50%, -50%) scale(1.8); opacity: 0; } }

  .demo-area { padding: 130px 40px 60px; max-width: 700px; margin: 0 auto; }
  .demo-btn {
    display: inline-block; padding: 14px 22px; margin: 8px;
    background: #378ADD; color: white; border-radius: 10px;
    cursor: pointer; font-weight: bold; user-select: none;
  }
</style>

<div id="panel">
  <h3>Controls</h3>
  <label>Interval (ms)</label>
  <input type="number" id="interval" value="500" min="50" step="50">
  <button id="startBtn">Start</button>
  <button id="stopBtn">Stop</button>
  <div id="status">Status: Stopped</div>
  <div id="count">Clicks: 0</div>
</div>

<div class="demo-area">
  <p>Test area — mouse ko in buttons ya kahi bhi is area mein rakh ke Start dabao.</p>
  <div class="demo-btn" onclick="this.innerText='Clicked!'">Test Button 1</div>
  <div class="demo-btn" onclick="this.innerText='Clicked!'">Test Button 2</div>
  <div class="demo-btn" onclick="this.innerText='Clicked!'">Test Button 3</div>
</div>

<script>
  let mouseX = window.innerWidth / 2;
  let mouseY = window.innerHeight / 2;
  let timer = null;
  let clickCount = 0;

  document.addEventListener("mousemove", (e) => {
    mouseX = e.clientX;
    mouseY = e.clientY;
  });

  function showRipple(x, y) {
    const r = document.createElement("div");
    r.className = "ripple";
    r.style.left = x + "px";
    r.style.top = y + "px";
    document.body.appendChild(r);
    setTimeout(() => r.remove(), 350);
  }

  function doClick() {
    const el = document.elementFromPoint(mouseX, mouseY);
    if (el && !el.closest("#panel")) {
      el.click();
      clickCount++;
      document.getElementById("count").innerText = "Clicks: " + clickCount;
      showRipple(mouseX, mouseY);
    }
  }

  document.getElementById("startBtn").addEventListener("click", () => {
    if (timer) return;
    const ms = parseInt(document.getElementById("interval").value) || 500;
    document.getElementById("status").innerText = "Status: Running";
    document.getElementById("status").style.color = "#2ecc71";
    timer = setInterval(doClick, ms);
  });

  document.getElementById("stopBtn").addEventListener("click", () => {
    clearInterval(timer);
    timer = null;
    document.getElementById("status").innerText = "Status: Stopped";
    document.getElementById("status").style.color = "#999";
  });
</script>
""", height=900, scrolling=True)