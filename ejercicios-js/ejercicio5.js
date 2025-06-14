// Generar un número aleatorio entre 1 y 10
const numero = Math.floor(Math.random() * 10) + 1;

// Calcular el factorial del número
let factorial = 1;
for (let i = 1; i <= numero; i++) {
    factorial *= i;
}

// Imprimir el resultado
console.log(`El factorial de ${numero} es ${factorial}`);