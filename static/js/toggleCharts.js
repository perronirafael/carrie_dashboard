import { fetchAndRenderMissedChartWithOutFilter } from './barCharts.js';
import { fetchAndRenderChartsWithOutFilter } from './doughnutCharts.js';

function updateAllCharts() {
    fetchAndRenderMissedChartWithOutFilter();
    fetchAndRenderChartsWithOutFilter();
}

document.addEventListener('DOMContentLoaded', () => {
    const btn = document.getElementById('toggleChartsBtn');
    const panel = document.getElementById('chartsPanel');

    btn.addEventListener('click', () => {
        const isHidden = panel.classList.toggle('hidden');
        btn.textContent = isHidden ? 'Show Charts' : 'Hide Charts';
        if (!isHidden) {
            updateAllCharts();
        }
    });
});
