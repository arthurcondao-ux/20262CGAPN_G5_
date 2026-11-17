# Simulador PNAE – Grupo 5

Portfólio do Grupo 5 na disciplina Análise de Dados para Pesquisas em Políticas Públicas. Este repositório reúne dois projetos, cada um na sua pasta.

## Portfólio

| Projeto | O que é | Pasta |
|---|---|---|
| Projeto 1: Simulador PNAE | Simulador em HTML do repasse do PNAE, montado a partir de uma planilha Excel | [/projeto-1-simulador-pnae](./projeto-1-simulador-pnae) |
| Projeto 2: Dashboard da Educação | Dashboard em Excel com dados do Censo Escolar 2024 | [/projeto-2-dashboard-educacao](./projeto-2-dashboard-educacao) |

### Estrutura do Projeto 1
- /projeto-1-simulador-pnae/Projeto_1_-_Simulador.xlsx: a planilha com os dados e os cálculos que deram origem ao simulador.
- /projeto-1-simulador-pnae/simulador_pnae_v2.html: o simulador interativo (abra no navegador).
- /projeto-1-simulador-pnae/README.md: este documento.

## Projeto 1: Simulador PNAE

### Objetivo
Este projeto usa uma base de dados do bairro Quiataúna, em Osasco (SP). Ele simula o repasse do PNAE, o Programa Nacional de Alimentação Escolar, para uma escola específica. O valor muda conforme o número de alunos, a modalidade de matrícula e um fator de ajuste em porcentagem.

### Como usar
1. Abra o arquivo simulador_pnae_v2.html no navegador.
2. Informe o número de alunos de cada modalidade.
3. Se quiser, mude o Fator de Ajuste (%).
4. Veja o valor do repasse calculado na tela.

A planilha Projeto_1_-_Simulador.xlsx traz os dados e as fórmulas usados como base. Foi com ela que montamos o simulador em HTML.

### Prints do resultado
Imagem 1: ajustando pelo número de alunos
<img width="951" height="562" alt="Ajuste por número de alunos" src="https://github.com/user-attachments/assets/1c6b20e8-2484-46c4-bcc0-12a83b33f161" />

Imagem 2: ajustando pelo Fator de Ajuste (%)
<img width="874" height="509" alt="Ajuste por fator de ajuste"
