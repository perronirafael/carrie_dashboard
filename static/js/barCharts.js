let missedChartInstance = null; 

export function renderMissedChartOrMessage(containerId, data) {
  const container = document.getElementById(containerId);
  container.parentElement.querySelector('.no-data')?.remove();

  if (!data || data.length === 0 || data.every(i => i.total === 0)) {
    const msg = document.createElement("p");
    msg.className = "no-data";
    msg.textContent = "Any available data for missed check-ins.";
    msg.style.textAlign = "center";
    msg.style.marginTop = "1rem";
    container.style.display = "none";
    container.parentElement.appendChild(msg);
  } else {
    container.style.display = "block";
    renderMissedBarChart(containerId, data);
  }
}

export function fetchAndRenderMissedChart() {
  const diagnosis = document.getElementById("Diagnosis").value;
  const age = document.getElementById("ages").value;
  const start = document.getElementById("start").value;
  const end = document.getElementById("end").value;

  const url = `/missed-checkins-data/?diagnosis=${diagnosis}&age=${age}&start=${start}&end=${end}`;

  fetch(url)
    .then((res) => res.json())
    .then((data) => {
      renderMissedChartOrMessage('missedChart', data);
    })
    .catch((err) => {
      console.error("Erro ao buscar dados de missed check-ins:", err);
    });
}

export function renderMissedBarChart(canvasId, data) {
  const ctx = document.getElementById(canvasId).getContext('2d');

  if (missedChartInstance) {
    missedChartInstance.destroy();
  }

  const labels = data.map(item => {
  const [year, month, day] = item.day.split('-');
  return new Date(year, month - 1, day).toLocaleDateString('en-US', {
    month: 'short',
    day: 'numeric'
  });
});

  missedChartInstance = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: labels,
      datasets: [{
        label: 'Missed Check-Ins',
        data: data.map(i => i.total),
        backgroundColor: '#6b7280'
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: true,
      scales: {
        y: {
          beginAtZero: true,
          ticks: { stepSize: 1 },
          grid: { color: '#e5e7eb' }
        },
        x: {
          grid: { display: false }
        }
      },
      plugins: { legend: { display: false } }
    }
  });
}
