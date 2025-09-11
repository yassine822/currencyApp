// Drawing setup
const canvas = document.getElementById("drawCanvas");
const ctx = canvas.getContext("2d");
const penColor = document.getElementById("penColor");
const penSize = document.getElementById("penSize");
let drawing = false;

function resizeCanvas() {
    canvas.width = canvas.offsetWidth;
    canvas.height = canvas.offsetHeight;
}
window.addEventListener("resize", resizeCanvas);
resizeCanvas();

canvas.addEventListener("mousedown", () => drawing = true);
canvas.addEventListener("mouseup", () => {
    drawing = false;
    ctx.beginPath();
});
canvas.addEventListener("mouseleave", () => {
    drawing = false;
    ctx.beginPath();
});
canvas.addEventListener("mousemove", draw);

function draw(e) {
    if (!drawing) return;
    ctx.strokeStyle = penColor.value;
    ctx.lineWidth = penSize.value;
    ctx.lineCap = "round";

    ctx.lineTo(e.offsetX, e.offsetY);
    ctx.stroke();
    ctx.beginPath();
    ctx.moveTo(e.offsetX, e.offsetY);
}

// Clear canvas
function clearCanvas() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
}

// Save drawing as PNG
function saveDrawing() {
    const link = document.createElement("a");
    link.download = "drawing.png";
    link.href = canvas.toDataURL();
    link.click();
}

// Save text as TXT
function saveText() {
    const text = document.getElementById("noteText").value;
    const blob = new Blob([text], { type: "text/plain;charset=utf-8" });
    const link = document.createElement("a");
    link.download = "notes.txt";
    link.href = URL.createObjectURL(blob);
    link.click();
}
