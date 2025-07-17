import { makeDoughnut } from './doughnutCharts.js';
import { renderMissedBarChart } from './barCharts.js';

document.addEventListener('DOMContentLoaded', function () {
    const missedCounts = JSON.parse(document.getElementById('missedCounts').textContent);
    renderMissedBarChart('missedChart', missedCounts);

    const medCounts = JSON.parse(document.getElementById('medCounts').textContent);
    makeDoughnut('medChart', 'legend-medChart', medCounts.map(i => i.medication), medCounts.map(i => i.total), ['#c7d2fe', '#1e293b', '#f9a8d4']);

    const dietCounts = JSON.parse(document.getElementById('dietCounts').textContent);
    makeDoughnut('dietChart', 'legend-dietChart', dietCounts.map(i => i.diet), dietCounts.map(i => i.total), ['#c7d2fe', '#1e293b', '#f9a8d4']);

    const exCounts = JSON.parse(document.getElementById('exCounts').textContent);
    makeDoughnut('exChart', 'legend-exeChart', exCounts.map(i => i.exercise), exCounts.map(i => i.total), ['#c7d2fe', '#1e293b', '#f9a8d4']);


});
