
# Painel Censo Escolar
Objetivo:
Este painel é uma página interativa que permite explorar as 3.110 escolas em atividade de 30 municípios de quatro regiões do estado de São Paulo: Região Metropolitana de SP (Osasco, Guarulhos e Carapicuíba), Baixada Santista, Litoral Norte e Vale do Ribeira. Os dados vêm do Censo Escolar 2024 (INEP), a pesquisa anual que reúne informações sobre todas as escolas de educação básica do Brasil. 

Como usar: 
### 1. O que você vai precisar
- O **Python 3** instalado. Se ainda não tiver, baixe em [python.org/downloads](https://www.python.org/downloads/). No Windows, marque a opção **"Add Python to PATH"** durante a instalação.
- Dois arquivos desta pasta, salvos **juntos na mesma pasta** do seu computador:
  - `painel.py`: o programa do painel;
  - `escolas_sp_regioes_2024_geo.csv`: a base de dados. Use a versão com **`_geo`** no nome, porque é ela que traz a latitude e a longitude usadas no mapa.

### 2. Instalar os pacotes (só na primeira vez)

O painel usa dois pacotes do Python: o **pandas**, que lê e organiza a base, e o **streamlit**, que transforma o programa numa página interativa no navegador.

Abra o **Terminal** (no Mac: `Cmd + Espaço`, digite "Terminal" e aperte Enter; no Windows: abra o "Prompt de Comando") e digite:

python -m pip install pandas streamlit

A instalação terminou quando aparecer uma mensagem começando com `Successfully installed`.

### 3. Rodar o painel

Primeiro, entre na pasta onde estão os dois arquivos: digite `cd` seguido de um espaço, **arraste a pasta** para dentro da janela do Terminal e aperte Enter. Depois, digite:

```
python -m streamlit run painel.py
```
### 4. Usar os filtros

No topo do painel há dois filtros, que funcionam juntos:

- **Escolha a Região:** mostra só as escolas de uma das quatro regiões, ou de **Todas**.
- **Localização diferenciada:** mostra só as escolas em terra indígena, comunidade quilombola, comunidades tradicionais ou assentamento. **Todas as diferenciadas** junta esses quatro tipos, e **Não** mostra as escolas comuns.

Ao mudar um filtro, os indicadores, os gráficos, o mapa e a lista passam a mostrar só as escolas selecionadas. No gráfico de **serviços públicos básicos**, quanto mais escolas nas barras da esquerda, pior a infraestrutura da seleção.

**Sugestão:** compare *Região Metropolitana de SP* com *Vale do Ribeira* e depois escolha *Todas as diferenciadas*.

Capturas de tela:
<img width="1046" height="1148" alt="image" src="https://github.com/user-attachments/assets/f44aa9eb-1f8a-4bb2-a31b-9f84fbf6aa2f" />
Captura 1. Filtro de localização diferenciada aberto, com a opção Todas as diferenciadas, que reúne as escolas em terras indígenas, comunidades quilombolas, comunidades tradicionais e assentamentos.

<img width="1280" height="832" alt="Screenshot 2026-11-19 at 12 43 27" src="https://github.com/user-attachments/assets/7ef21429-8a75-4753-832e-3614b5723d13" />
Captura 2. Com os filtros Baixada Santista e Terra indígena, o painel mostra as duas escolas indígenas de Bertioga, que somam 194 matrículas, são de porte pequeno e recebem 3 dos 4 serviços públicos básicos.

