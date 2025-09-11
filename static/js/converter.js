document.getElementById('swap-btn').addEventListener('click', function() {
    const fromSelect = document.getElementById('from_currency');
    const toSelect = document.getElementById('to_currency');
    const temp = fromSelect.value;
    fromSelect.value = toSelect.value;
    toSelect.value = temp;
});
