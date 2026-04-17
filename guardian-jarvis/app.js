let liveInterval = null;

// START LIVE MODE
window.startLiveDashboard = function () {
  console.log("LIVE STARTED");

  setInterval(async () => {
    const res = await fetch(`${API}/scan`);
    const data = await res.json();

    document.getElementById("threat").innerText = data.threat_level;
    document.getElementById("score").innerText = data.risk_score;

    if (document.getElementById("insight")) {
      document.getElementById("insight").innerText = data.insight || "";
    }

  }, 2000);
};

// UPDATE UI
function updateUI(data) {
  document.getElementById("threat").innerText = data.threat_level;
  document.getElementById("score").innerText = data.risk_score;

  // ALERT COLORING
  const box = document.getElementById("statusBox");

  if (data.risk_score < 25) box.style.color = "#00ff88";
  else if (data.risk_score < 50) box.style.color = "#ffcc00";
  else if (data.risk_score < 75) box.style.color = "#ff8800";
  else box.style.color = "#ff0033";

  // optional insight display
  if (document.getElementById("insight")) {
    document.getElementById("insight").innerText = data.insight;
  }
}

// MANUAL SCAN BUTTON
async function runScan() {
  const res = await fetch(`${API}/scan`);
  const data = await res.json();
  updateUI(data);
}