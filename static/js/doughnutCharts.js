const chartInstances = {};

export function renderChartOrMessage(containerId, legendId, labels, data, colors, fieldName) {
  const container = document.getElementById(containerId);
  const legend = document.getElementById(legendId);

  legend.innerHTML = "";
  container.parentElement.querySelector('.no-data')?.remove();

  if (data.length === 0 || labels.length === 0 || data.every(val => val === 0)) {
    const msg = document.createElement("p");
    msg.className = "no-data";
    msg.textContent = `Any avaiable data for ${fieldName}.`;
    msg.style.textAlign = "center";
    msg.style.marginTop = "1rem";
    container.style.display = "none";
    container.parentElement.appendChild(msg);
  } else {
    container.style.display = "block";
    makeDoughnut(containerId, legendId, labels, data, colors);
  }
}

export function fetchAndRenderCharts() {
  const diagnosis = document.getElementById("Diagnosis").value;
  const age = document.getElementById("ages").value;
  const start = document.getElementById("start").value;
  const end = document.getElementById("end").value;

  fetch(`/chart-data/?diagnosis=${diagnosis}&age=${age}&start=${start}&end=${end}`)
    .then((res) => res.json())
    .then((data) => {
      document.getElementById("legend-medChart").innerHTML = "";
      document.getElementById("legend-dietChart").innerHTML = "";
      document.getElementById("legend-exeChart").innerHTML = "";

      renderChartOrMessage(
        "medChart",
        "legend-medChart",
        data.medication.map(i => i.medication),
        data.medication.map(i => i.total),
        ['#c7d2fe', '#1e293b', '#f9a8d4'],
        "medicação"
      );

      renderChartOrMessage(
        "dietChart",
        "legend-dietChart",
        data.diet.map(i => i.diet),
        data.diet.map(i => i.total),
        ['#c7d2fe', '#1e293b', '#f9a8d4'],
        "dieta"
      );

      renderChartOrMessage(
        "exChart",
        "legend-exeChart",
        data.exercise.map(i => i.exercise),
        data.exercise.map(i => i.total),
        ['#c7d2fe', '#1e293b', '#f9a8d4'],
        "exercício"
      );
    });
}

export function makeDoughnut(canvasId, legendId, labels, data, colors) {
  if (chartInstances[canvasId]) {
    chartInstances[canvasId].destroy();
  }

  const ctx = document.getElementById(canvasId).getContext('2d');

  const chart = new Chart(ctx, {
    type: 'doughnut',
    data: {
      labels: labels,
      datasets: [{
        data: data,
        backgroundColor: colors,
        borderWidth: 0,
      }]
    },
    options: {
      responsive: true,
      plugins: {
        legend: {
          display: false
        }
      }
    }
  });

  chartInstances[canvasId] = chart;

  const legend = document.getElementById(legendId);
  legend.innerHTML = labels.map((label, i) => {
    const color = colors[i % colors.length];
    return `
            <div style="display:inline-flex;align-items:center;margin-right:1rem;">
                <span style="display:inline-block;width:12px;height:12px;background-color:${color};margin-right:4px;border-radius:2px;"></span>
                ${label}: ${data[i]}
            </div>
        `;
  }).join('');
}

export function fetchAndRenderChartsWithOutFilter() {
  fetch(`/chart-data/`)
    .then((res) => res.json())
    .then((data) => {
      document.getElementById("legend-medChart").innerHTML = "";
      document.getElementById("legend-dietChart").innerHTML = "";
      document.getElementById("legend-exeChart").innerHTML = "";

      renderChartOrMessage(
        "medChart",
        "legend-medChart",
        data.medication.map(i => i.medication),
        data.medication.map(i => i.total),
        ['#c7d2fe', '#1e293b', '#f9a8d4'],
        "medicação"
      );

      renderChartOrMessage(
        "dietChart",
        "legend-dietChart",
        data.diet.map(i => i.diet),
        data.diet.map(i => i.total),
        ['#c7d2fe', '#1e293b', '#f9a8d4'],
        "dieta"
      );

      renderChartOrMessage(
        "exChart",
        "legend-exeChart",
        data.exercise.map(i => i.exercise),
        data.exercise.map(i => i.total),
        ['#c7d2fe', '#1e293b', '#f9a8d4'],
        "exercício"
      );
    });
}