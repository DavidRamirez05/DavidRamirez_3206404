/** 
* Controlador principal de la silumacion de pelota * 
*/
let canvas = null;
let ctx = null;
let pelotas = [];
let gravedad = 0.3;
const numPelotas = 20;

window.onload = function () {
  canvas = document.getElementById("canvas");
  ctx = canvas.getContext("2d");

  document.body.style.padding = "20px";
  ctx.canvas.width = window.innerWidth - 100;
  ctx.canvas.height = window.innerHeight - 100;

  cargarInicio();
};

function cargarInicio() {
  for (let i = 0; i < numPelotas; i++) {
    pelotas.push(new Pelota());
  }
  animar();
}

function animar() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  ctx.strokeStyle = 'black';
  ctx.lineWidth = 2;
  ctx.strokeRect(0, 0, canvas.width, canvas.height);

  for (let i = 0; i < pelotas.length; i++) {
    let pelota = pelotas[i];
    pelota.velocidad.y += gravedad;
    pelota.posicion.x += pelota.velocidad.x;
    pelota.posicion.y += pelota.velocidad.y;
    pelota.detectarColisionBordes();
  }

  for (let i = 0; i < pelotas.length; i++) {
    for (let j = i + 1; j < pelotas.length; j++) {
      pelotas[i].checkCollisionWithOtherBall(pelotas[j]);
    }
  }

  for (let i = 0; i < pelotas.length; i++) {
    pelotas[i].dibujar();
  }

  requestAnimationFrame(animar);
}
