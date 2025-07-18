export async function fetchAndRenderPatientStatusCard(filters = {}) {
    const { diagnosis = "all", age = "all", start = "", end = "" } = filters;
    const params = new URLSearchParams({ diagnosis, age, start, end });

    const res = await fetch(`/patient-status-data/?${params.toString()}`);
    const data = await res.json();

    const statusList = document.getElementById("patientStatusList");
    const alertDiv = document.getElementById("alertSummary");
    const noData = document.getElementById("noStatusData");

    statusList.innerHTML = "";

    if (data.status_counts.length === 0) {
        noData.style.display = "block";
        alertDiv.style.display = "none";
    } else {
        noData.style.display = "none";

        data.status_counts.forEach(item => {
            const div = document.createElement("div");
            div.className = `status-item status-${slugify(item.status)}`;
            div.innerHTML = `
        <span class="status-label">${capitalize(item.status)}</span>
        <span class="status-badge">${item.total}</span>
      `;
            statusList.appendChild(div);
        });

        if (data.alert_count > 0) {
            alertDiv.style.display = "block";
            alertDiv.textContent = `${data.alert_count} Patient Alert Needs Review`;
        } else {
            alertDiv.style.display = "none";
        }
    }
}

function slugify(text) {
    return text.toString().toLowerCase().replace(/\s+/g, '-');
}

function capitalize(text) {
    return text.charAt(0).toUpperCase() + text.slice(1);
}
