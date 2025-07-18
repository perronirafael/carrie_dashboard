async function openModal(modalId, actionUrl = null) {
    const modal = document.getElementById(modalId);
    if (!modal) return;

    if (modalId === 'patientFormModal' && actionUrl) {
        const res = await fetch(actionUrl);
        const html = await res.text();

        const parser = new DOMParser();
        const doc = parser.parseFromString(html, 'text/html');
        const form = doc.querySelector('#patientForm');

        const titleEl = modal.querySelector('#modalTitle');
        titleEl.textContent = actionUrl.includes('/edit/')
            ? 'Edit Patient'
            : 'Add Patient';

        const bodyEl = modal.querySelector('.modal-body');
        bodyEl.innerHTML = '';
        if (form) bodyEl.appendChild(form);
    }

    if (modalId === 'deleteConfirmModal' && actionUrl) {
        const delForm = modal.querySelector('#deleteForm');
        if (delForm) delForm.action = actionUrl;
    }

    modal.classList.remove('hidden');
}


function closeModal(modalId) {
    const modal = document.getElementById(modalId);
    if (!modal) return;
    modal.classList.add('hidden');
}


document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.open-modal').forEach(btn => {
        btn.addEventListener('click', () => {
            const target = btn.dataset.modal;
            const url = btn.dataset.url;
            openModal(target, url);
        });
    });
});
