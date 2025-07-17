export function renderMissedBarChart(canvasId, data) {
  new Chart(document.getElementById(canvasId).getContext('2d'), {
    type: 'bar',
    data: {
      labels: data.map(i => new Date(i.day).toLocaleDateString('en-US', {
        month: 'short',
        day: 'numeric'
      })),
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
