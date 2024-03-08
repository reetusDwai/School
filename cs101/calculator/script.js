let input = "";
let display = document.getElementById("display");

function addInput(button) {
    input += button.value;
    display.innerText = input;
}

function equate() {
    let output = eval(input);
    display.innerText = output;
    input = "";
}

function clr() {
    input = "";
    display.innerText = "";
}
