<template>
  <div style="padding: 10px;">
    <div style="display: flex;">
      <!-- Campos de entrada para velocidad inicial y ángulo sin resistencia del viento -->
      <div style="flex: 1; padding: 10px;">
        <h3>Sin Resistencia del Viento</h3>
        <v-text-field v-model="velocidadInicial" label="Velocidad inicial (m/s)"></v-text-field>
        <v-text-field v-model="angulo" label="Ángulo de tiro (grados)"></v-text-field>
      </div>

      <!-- Campos de entrada para velocidad inicial, ángulo y coeficiente de rozamiento -->
      <div style="flex: 1; padding: 10px;">
        <h3>Con Coeficiente de Rozamiento</h3>
        <v-text-field v-model="velocidadInicialConRozamiento" label="Velocidad inicial (m/s)"></v-text-field>
        <v-text-field v-model="anguloConRozamiento" label="Ángulo de tiro (grados)"></v-text-field>
        <v-text-field v-model="coeficienteRozamiento" label="Coeficiente de rozamiento" type="number"></v-text-field>
      </div>
    </div>

    <!-- Botón para calcular ambas alturas -->
    <div style="text-align: center; margin-top: 20px;">
      <v-btn @click="calcularAlturas" color="primary">Calcular Alturas</v-btn>
    </div>

    <!-- Mostrar sparkline para sin resistencia del viento -->
    <h3>Gráfica Sin Resistencia del Viento</h3>
    <v-sparkline
      :auto-line-width="autoLineWidth"
      :fill="fill"
      :gradient="gradient"
      :gradient-direction="gradientDirection"
      :line-width="width"
      :model-value="parabolicData"
      :padding="padding"
      :smooth="radius || false"
      :stroke-linecap="lineCap"
      :type="type"
      auto-draw
    ></v-sparkline>

    <!-- Mostrar sparkline para con coeficiente de rozamiento -->
    <h3>Gráfica Con Coeficiente de Rozamiento</h3>
    <v-sparkline
      :auto-line-width="autoLineWidth"
      :fill="fill"
      :gradient="gradient"
      :gradient-direction="gradientDirection"
      :line-width="width"
      :model-value="parabolicDataConRozamiento"
      :padding="padding"
      :smooth="radius || false"
      :stroke-linecap="lineCap"
      :type="type"
      auto-draw
    ></v-sparkline>
  </div>
</template>

<script>
export default {
  data() {
    return {
      // Parámetros comunes
      width: 2,
      radius: 10,
      padding: 8,
      lineCap: 'round',
      gradient: ['#000'], // Cambiado a negro
      g: 9.8, // Aceleración debido a la gravedad
      autoLineWidth: false,
      fill: false,
      type: 'trend',
      gradientDirection: 'top',

      // Parámetros sin resistencia del viento
      velocidadInicial: 0,
      angulo: 0,
      parabolicData: [], // Almacenará los datos de la gráfica sin viento

      // Parámetros con coeficiente de rozamiento
      velocidadInicialConRozamiento: 0,
      anguloConRozamiento: 0,
      coeficienteRozamiento: 0, // Coeficiente de rozamiento
      parabolicDataConRozamiento: [], // Almacenará los datos de la gráfica con rozamiento
    };
  },
  methods: {
    calcularAlturas() {
      this.calcularAltura();
      this.calcularAlturaConRozamiento();
    },
    calcularAltura() {
      const radianes = (this.angulo * Math.PI) / 180;
      this.parabolicData = [];

      for (let t = 0; t < 30; t += 0.5) {
        const altura = this.velocidadInicial * Math.sin(radianes) * t - (0.5 * this.g * t ** 2);
        // Aproximar la altura a un número entero
        const alturaEntera = Math.round(altura);

        // Ajustar la altura a 0 si es negativa
        const alturaFinal = Math.max(0, alturaEntera);
        this.parabolicData.push(alturaFinal);
      }

      // Mostrar el array completo por consola
      console.log('Datos de altura:', this.parabolicData);
    },
    calcularAlturaConRozamiento() {
      const radianes = (this.anguloConRozamiento * Math.PI) / 180;
      this.parabolicDataConRozamiento = [];

      for (let t = 0; t < 30; t += 0.5) {
        const velocidadVertical = this.velocidadInicialConRozamiento * Math.sin(radianes) - (this.coeficienteRozamiento * t);
        const altura = velocidadVertical * t - (0.5 * this.g * t ** 2);
        // Aproximar la altura a un número entero
        const alturaEntera = Math.round(altura);

        // Ajustar la altura a 0 si es negativa
        const alturaFinal = Math.max(0, alturaEntera);
        this.parabolicDataConRozamiento.push(alturaFinal);
      }

      // Mostrar el array completo por consola
      console.log('Datos de altura con rozamiento:', this.parabolicDataConRozamiento);
    },
  },
};
</script>
