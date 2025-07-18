function updateSaveButtonState(form) {
    const fields = Array.from(form.querySelectorAll('input, select'))
        .filter(el => el.type !== 'hidden' && el.type !== 'submit');
    const allFilled = fields.every(el => el.value.trim() !== '');
    const btn = form.querySelector('#patientFormSubmit');

    if (allFilled && form.checkValidity()) {
        btn.disabled = false;
        btn.classList.remove('btn-disabled');
    } else {
        btn.disabled = true;
        btn.classList.add('btn-disabled');
    }
}


function openModal(modalId, url, triggerBtn) {
    const modal = document.getElementById(modalId);
    modal.classList.remove('hidden');

    if (modalId === 'patientFormModal') {
        const title = modal.querySelector('.modal-title');
        const form = modal.querySelector('#patientForm');

        form.action = url;
        const isCreate = url.endsWith('/new/') || /\/patients\/create/.test(url);
        title.textContent = isCreate ? 'Add Patient' : 'Edit Patient';

        if (isCreate) {
            form.reset();
        } else {
            const d = triggerBtn.dataset;
            form.querySelector('[name="first_name"]').value = d.firstName;
            form.querySelector('[name="last_name"]').value = d.lastName;
            form.querySelector('[name="mrn"]').value = d.mrn;
            form.querySelector('[name="age"]').value = d.age;
            form.querySelector('[name="provider"]').value = d.provider;
            form.querySelector('[name="diagnosis"]').value = d.diagnosis;
            form.querySelector('[name="status"]').value = d.status;
            form.querySelector('[name="last_session_date"]').value = d.lastSessionDate;
        }

        updateSaveButtonState(form);
        form.querySelectorAll('input, select').forEach(el => {
            el.addEventListener('input', () => updateSaveButtonState(form));
        });
    }
    else if (modalId === 'deleteConfirmModal') {
        const delForm = modal.querySelector('#deleteForm');
        if (delForm) delForm.action = url;
    }
}


function closeModal(modalId) {
    document.getElementById(modalId).classList.add('hidden');
}

document.querySelectorAll('.open-modal').forEach(btn => {
    btn.addEventListener('click', () => {
        const modalId = btn.dataset.modal;
        const url = btn.dataset.url;
        openModal(modalId, url, btn);
    });
});
