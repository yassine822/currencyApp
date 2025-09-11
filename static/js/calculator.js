const display = document.getElementById('display');
const historyList = document.getElementById('history-list');

function press(key) {
    if (display.value === "0") display.value = "";
    display.value += key;
}

function clearDisplay() {
    display.value = "";
}

function calculateResult() {
    try {
        const result = eval(display.value);
        addToHistory(display.value + " = " + result);
        display.value = result;
    } catch (e) {
        display.value = "Error";
    }
}

function addToHistory(entry) {
    const li = document.createElement('li');
    li.textContent = entry;
    historyList.prepend(li); // newest on top
}
