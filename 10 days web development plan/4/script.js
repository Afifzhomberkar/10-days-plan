// Real-time validation
document.getElementById('username').addEventListener('input', function () {
    const name = this.value;
    const error = document.getElementById('nameError');
    if (name.length < 3) {
        error.textContent = 'Username must be at least 3 characters.';
    } else {
        error.textContent = '';
    }
});

// Character Counter
document.getElementById('textArea').addEventListener('input', function () {
    document.getElementById('charCount').textContent = this.value.length;
});

// Calculator
function calculate(op) {
    const n1 = parseFloat(document.getElementById('num1').value);
    const n2 = parseFloat(document.getElementById('num2').value);
    let result = 0;

    switch (op) {
        case '+': result = n1 + n2; break;
        case '-': result = n1 - n2; break;
        case '*': result = n1 * n2; break;
        case '/': result = n2 !== 0 ? n1 / n2 : 'Error'; break;
    }

    document.getElementById('calcResult').textContent = result;
}

// Toggle Dark/Light Mode
document.getElementById('toggleMode').addEventListener('click', function () {
    document.body.classList.toggle('dark-mode');
});
