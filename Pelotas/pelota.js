class Pelota {
  constructor() {
    this.radio = this.generarNumero(10, 25);
    this.posicion = {
      x: this.generarNumero(this.radio, ctx.canvas.width - this.radio),
      y: this.generarNumero(this.radio, ctx.canvas.height - this.radio),
    }
    this.velocidad = {
      x: this.generarNumero(-3, 3),
      y: this.generarNumero(-3, 3),
    }
    this.colorFondo = this.getRandomColor();
    this.masa = this.radio;
  }

  detectarColisionBordes() {
    if (this.posicion.x <= this.radio) {
        this.velocidad.x *= -1;
        this.posicion.x = this.radio;
    } else if (this.posicion.x >= ctx.canvas.width - this.radio) {
        this.velocidad.x *= -1;
        this.posicion.x = ctx.canvas.width - this.radio;
    }

    if (this.posicion.y <= this.radio) {
        this.velocidad.y *= -1;
        this.posicion.y = this.radio;
    } else if (this.posicion.y >= ctx.canvas.height - this.radio) {
        this.velocidad.y *= -1;
        this.posicion.y = ctx.canvas.height - this.radio;
        this.velocidad.y *= 0.8;
    }
  }

  checkCollisionWithOtherBall(otherBall) {
    const dx = otherBall.posicion.x - this.posicion.x;
    const dy = otherBall.posicion.y - this.posicion.y;
    const distance = Math.sqrt(dx * dx + dy * dy);

    if (distance <= this.radio + otherBall.radio) {
      const normalX = dx / distance;
      const normalY = dy / distance;
      const relativeVelocityX = otherBall.velocidad.x - this.velocidad.x;
      const relativeVelocityY = otherBall.velocidad.y - this.velocidad.y;
      const dotProduct = relativeVelocityX * normalX + relativeVelocityY * normalY;

      if (dotProduct < 0) {
        const impulse = (2 * dotProduct) / (this.masa + otherBall.masa);

        this.velocidad.x += impulse * normalX * otherBall.masa;
        this.velocidad.y += impulse * normalY * otherBall.masa;
        otherBall.velocidad.x -= impulse * normalX * this.masa;
        otherBall.velocidad.y -= impulse * normalY * this.masa;

        const overlap = (this.radio + otherBall.radio) - distance;
        const separation = overlap / 2;

        this.posicion.x -= separation * normalX;
        this.posicion.y -= separation * normalY;
        otherBall.posicion.x += separation * normalX;
        otherBall.posicion.y += separation * normalY;
      }
    }
  }

  dibujar() {
    ctx.beginPath();
    ctx.arc(this.posicion.x, this.posicion.y, this.radio, 0, Math.PI * 2);
    ctx.fillStyle = this.colorFondo;
    ctx.fill();
  }

  generarNumero(min, max) {
    let num = Math.floor(Math.random() * (max - min + 1) + min);
    return num;
  }

  getRandomColor() {
    return (
      "#" +
      Math.floor(Math.random() * 0xffffff)
        .toString(16)
        .padStart(6, "0")
    );
  }
}
