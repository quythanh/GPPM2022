document.querySelector('#status7').addEventListener('click', () => {
    document.querySelector('.symptoms').classList.toggle('hide');
    document.querySelectorAll('.symptoms input').forEach(e => e.checked = false);
})