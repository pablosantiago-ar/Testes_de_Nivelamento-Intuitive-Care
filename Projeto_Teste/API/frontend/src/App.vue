<template>
  <div class="container">
    <h1>Buscar Operadoras</h1>
    <input v-model="query" @input="buscar" placeholder="Digite para buscar..." />
    <ul>
      <li v-for="resultado in resultados" :key="resultado.dados.Registro_ANS">
      <strong>{{ resultado.dados.Razao_Social }}</strong> - CNPJ: {{ resultado.dados.CNPJ }} - Relevância: {{ resultado.relevancia }}
      </li>

    </ul>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      query: "",
      resultados: [],
    };
  },
  methods: {
    async buscar() {
      if (this.query.length < 2) {
        this.resultados = [];
        return;
      }
      const response = await axios.get(`http://localhost:5000/buscar?q=${this.query}`);
      this.resultados = response.data;
    },
  },
};
</script>

<style>
.container {
  max-width: 600px;
  margin: auto;
  text-align: center;
}
input {
  width: 100%;
  padding: 10px;
  margin: 10px 0;
}
ul {
  list-style: none;
  padding: 0;
}
li {
  background: #f3f3f3;
  margin: 5px 0;
  padding: 10px;
}
</style>
