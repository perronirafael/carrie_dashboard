export function makeDoughnut(ctxId, legendId, labels, data, colors) {
  const ctx = document.getElementById(ctxId).getContext('2d');
  new Chart(ctx, {
    type: 'doughnut',
    data: {
      labels: labels,
      datasets: [{ data: data, backgroundColor: colors }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: true,
      cutout: '60%',
      plugins: { legend: { display: false } }
    }
  });

  const legendContainer = document.getElementById(legendId);
  legendContainer.innerHTML = '';
  labels.forEach((label, i) => {
    const item = document.createElement('div');
    item.className = 'chart-legend-item';
    const box = document.createElement('span');
    box.className = 'chart-legend-box';
    box.style.backgroundColor = colors[i];
    item.appendChild(box);
    item.appendChild(document.createTextNode(label));
    legendContainer.appendChild(item);
  });
}
