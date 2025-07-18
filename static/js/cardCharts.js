import { fetchAndRenderCharts } from './doughnutCharts.js';
import { fetchAndRenderMissedChart } from './barCharts.js';
import { fetchAndRenderPatientStatusCard } from './statusCard.js';

document.addEventListener('DOMContentLoaded', function () {
  const inputs = document.querySelectorAll("#Diagnosis, #ages, #start, #end");

  const getFilters = () => ({
    diagnosis: document.getElementById("Diagnosis")?.value || "all",
    age: document.getElementById("ages")?.value || "all",
    start: document.getElementById("start")?.value || "",
    end: document.getElementById("end")?.value || "",
  });

  const updateAll = () => {
    const filters = getFilters();
    fetchAndRenderCharts(filters);
    fetchAndRenderMissedChart(filters);
    fetchAndRenderPatientStatusCard(filters);
  };

  inputs.forEach(input => {
    input.addEventListener("change", updateAll);
  });

  updateAll();
});
