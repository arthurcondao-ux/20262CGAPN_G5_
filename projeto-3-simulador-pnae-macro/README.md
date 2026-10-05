# Projeto 3 — Simulador PNAE com Registro de Simulações

**Objetivo:** Este projeto dá continuidade ao simulador de repasse do PNAE (Projeto 1), acrescentando uma macro em VBA. Ao clicar no botão "Salvar Simulação", a planilha confere se os campos foram preenchidos e grava o cenário na aba Banco_de_Dados, com fator de ajuste, justificativa, matrículas ajustadas, repasse ajustado e usuário. Assim, o grupo mantém um histórico das simulações realizadas.

**Capturas de Tela**
<img width="835" height="787" alt="image" src="https://github.com/user-attachments/assets/44f21058-bc9e-47aa-8968-750fd821e1fb" />

<img width="1051" height="720" alt="image" src="https://github.com/user-attachments/assets/5854f2d6-e128-4f72-822f-2823da3a65d4" />

**Como usar:**
1. Baixe a planilha `.xlsm` desta pasta e abra no Excel instalado no computador 
2. Clique em "Habilitar Conteúdo" para ativar as macros.
3. Na aba `Simulador_Escola`, preencha Usuário, Racional da Taxa e Fator de Ajuste (ex.: 5% ou -10%).
4. Clique em "Salvar Simulação".
5. Confira o registro na aba `Banco_de_Dados`.

## Uso de Inteligência Artificial

**Ferramenta utilizada:** Claude (Anthropic)

**Para que foi usada:** apoio na redação deste README. A planilha e a macro em VBA não foram feitas com IA: o grupo implementou o campo usuário seguindo o passo a passo comentado no próprio código.

**Exemplo de prompt utilizado:** "Nosso grupo está realizando o seguinte trabalho no Github. Estou fazendo o Readme e gostaria de ajuda para estruturar o relatório e o objetivo"

**Estrutura:**
- `Parametros_PNAE`: valor per capita (R$/dia) por modalidade, dias letivos e faixas de porte.
- `Simulador_Escola`: matrículas por modalidade, fator de ajuste, matrículas ajustadas e repasse anual estimado.
- `Banco_de_Dados`: ID, Data/Hora, Fator de Ajuste, Racional da Taxa, Total de Matrículas Ajustadas, Repasse Ajustado (R$) e Usuário.

## Participação do Grupo

**O que aprendemos com este projeto:** Aprendemos a ler e adaptar um código em VBA, entendendo como declarar variáveis, capturar valores digitados nas células e gravá-los em outra aba. Ao implementar o campo usuário, vimos na prática como uma macro valida o preenchimento antes de salvar e como isso transforma uma planilha de cálculo em um registro organizado das simulações. Também percebemos a importância de guardar a justificativa de cada cenário, e não apenas o resultado, para que a análise possa ser entendida e revisada depois

**Papel de cada integrante**
- Arthur Condão: Responsável por upload do Github
- João Pedro Bersi: Responsável pelo Readme
- Kauã Olimar: Responsável pelo VBA
- Roger Alencar: Responsável pelo upload do Github
- Thiago Ramos Giacomo: Responsável pelo Readme
- Tomás Lenci Girard: Responsável pelo VBA
