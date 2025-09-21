<template>
  <div class="container my-5">
    <h1 class="mb-4">Useful Data Analysis Formulas</h1>
    <div v-for="formula in formulas" :key="formula.id" class="mb-5 border-bottom pb-4">
      <h4>{{ formula.title }}</h4>
      <p><strong>📊 Excel:</strong> <code>{{ formula.excel_formula }}</code></p>
      <p><strong>🐍 Python (Colab):</strong></p>
      <pre><code>{{ getPythonCode(formula.python_script) }}</code></pre>
      <p><strong>📚 Explanation:</strong> {{ formula.explanation }}</p>
      <div>
        <strong>🔢 Example:</strong>
        <pre><code>{{ formatExample(formula.example) }}</code></pre>
      </div>
    </div>
  </div>
</template>

<script>
import formulas from "../data/formulas.json";

// simulazione codice Python (in realtà andrebbe importato o letto dinamicamente)
const mockPythonScripts = {
  "python/conteggio_condizioni.py": `import pandas as pd
df = pd.read_excel("file.xlsx")
counts = df.groupby(["sito_id", "tipo_analisi"]).size().reset_index(name="conteggio")`
};

export default {
  name: "FormulasComponent",
  data() {
    return {
      formulas
    };
  },
  methods: {
    getPythonCode(path) {
      return mockPythonScripts[path] || "Python code not available.";
    },
    formatExample(example) {
      return JSON.stringify(example, null, 2);
    }
  }
};
</script>

<style scoped>
code {
  background: #f4f4f4;
  padding: 0.2rem 0.4rem;
  border-radius: 4px;
}
pre {
  background: #f9f9f9;
  padding: 1rem;
  border-left: 4px solid #b7f60c;
  overflow-x: auto;
}
</style>
