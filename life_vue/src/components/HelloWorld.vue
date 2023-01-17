<template>
  <div>
      <v-text-field
      v-model="lines"
      label="linhas"
      outlined
      clearable
    ></v-text-field>
    <v-text-field
      v-model="columns"
      label="colunas"
      outlined
      clearable
    ></v-text-field>
    <v-btn
    @click="criaGrid()"
    elevation="2"
    class="mb-8"
    >Criar tabela</v-btn>
    <v-btn
    @click="reiniciaJogo()"
    elevation="2"
    class="mb-8 ml-8"
    >Reiniciar Jogo</v-btn>
    <table>
      <tr v-for="(line, r) in grid" :key="`${line}-${r}`">
        <td
          v-for="(coluna, c) in line"
          :key="`${r}-${c}-${coluna}`"
          :class="classes(r, c)"
        ></td>
      </tr>
    </table>
  </div>
</template>

<script>
export default {
  data() {
    return {
      grid: [],
      lines:'',
      columns: '',
    };
  },
  methods: {
    reiniciaJogo(){
      this.grid = []
    },
    criaGrid(){
      for (let i = 0; i < this.lines; i++  ){
        let colunas = []
        for (let i = 0; i < this.columns; i++  ){
            colunas.push(Math.random() > 0.8)
            }
            this.grid.push(colunas)
          }
      const grid = () => {
      this.update();
      setTimeout(grid, 800);
    };
    grid();
      },
    update() {
      let new_matriz = JSON.parse(JSON.stringify(this.grid))
      for (let i = 0; i < this.lines; i++) {
        for (let j = 0; j < this.columns; j++) {
          let alives = this.vizinhos(i, j);
          if (this.grid[i][j] === 1) {
            if (alives < 2 || alives > 3) {
              new_matriz[i][j] = 0
            }
          } else {
            if (alives === 3) {
              new_matriz[i][j] = 1
            }
          }

        }
      }
      this.grid = new_matriz;
      return new_matriz
    },
    vizinhos(x, y) {
      let somatorio = 0;
      for (let linha_x of [-1, 0, 1]) {
        for (let coluna_y of [-1, 0, 1]) {
          const vizinho_x = x + linha_x;
          const vizinho_y = y + coluna_y;
          if (
            vizinho_x < 0 ||
            vizinho_y < 0 ||
            vizinho_x >= this.grid.length ||
            vizinho_y >= this.grid[0].length) continue
          if (vizinho_x == x && vizinho_y == y) continue
          somatorio += this.grid[vizinho_x][vizinho_y]
        }
      }
      return somatorio;
    },
    classes(linha, coluna) {
      return {
        pintado: this.grid[linha][coluna],
      };
    },
  },
};
</script>

<style scoped>
table td {
  border: 1px solid #eee;
  width: 30px;
  height: 30px;
  background-color: white;
}
.pintado {
  background-color: black;
}
</style>