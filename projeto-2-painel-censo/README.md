# Painel Censo – Grupo 5

Portfólio do Grupo 5 na disciplina Análise de Dados para Pesquisas em Políticas Públicas. Este repositório reúne dois projetos, cada um na sua pasta.

## Portfólio

| Projeto | O que é | Pasta |
|---|---|---|
| Projeto 1: Simulador PNAE | Simulador em HTML do repasse do PNAE, montado a partir de uma planilha Excel | [/projeto-1-simulador-pnae](./projeto-1-simulador-pnae) |
| Projeto 2: Painel Censo | Dashboard em Excel com dados do Censo Escolar 2024 | [/projeto-2-painel-censo](./projeto-2-painel-censo) |

### Estrutura do Projeto 2
- /projeto-2-painel-censo/Projeto Excel.xlsx: o dashboard em Excel com os dados, as fórmulas e os gráficos.
- /projeto-2-painel-censo/prints: imagens do resultado.
- /projeto-2-painel-censo/README.md: este documento.

## Projeto 2: Painel Censo

### Objetivo
Este projeto apresenta um Dashboard da Educação feito em Excel, com base nos dados do Censo Escolar 2024 das escolas do município de São Paulo. O arquivo reúne informações sobre a distribuição de raça, a quantidade e a coleta de esgoto nas escolas e as modalidades escolares. O objetivo é visualizar essas distribuições de forma dinâmica, destacando as diferenças entre elas.

### Como usar
1. Abra o arquivo "Projeto Excel.xlsx" na pasta projeto-2-painel-censo.
2. Vá à aba "Dash da Educação" e use as tabelas dinâmicas e os filtros para mudar os gráficos.
3. As abas "Dinâmicas" e "microdados_ed_basica_2024" trazem as tabelas e a base de dados usadas.

### Prints do resultado
Imagem 1: alguns dos gráficos do dashboard
<img width="1502" height="1000" alt="PHOTO-2026-11-17-15-56-53" src="https://github.com/user-attachments/assets/178ab523-57fb-47a5-8ca9-b61e695986b5" />


## Uso de Inteligência Artificial
Ferramenta utilizada: Claude
Para que foi usada: coletar informações e pensar em formas diferentes e adequadas de ilustrar os gráficos.
Exemplo de prompt utilizado: "Como fazer os dados de distribuição de raça por modalidade escolar ser mais visualmente agradável"
O que foi ajustado manualmente: pequenos ajustes, como títulos e outros detalhes dos gráficos.

## Fonte de Dados
Fonte oficial: Censo Escolar 2024 (INEP)
Link oficial: https://censobasico.inep.gov.br/censobasico_2024/
O que os dados representam: o Censo Escolar é a principal pesquisa estatística da educação básica no Brasil, coletada anualmente pelo INEP junto às escolas. Usamos os microdados de 8.023 escolas do município de São Paulo. Eles descrevem a localização, a infraestrutura (água, energia, esgoto e lixo) e as matrículas por modalidade, cor/raça, sexo e faixa etária.
Estrutura (aba microdados_ed_basica_2024):
- NO_MUNICIPIO: município da escola (todas em São Paulo).
- NO_ENTIDADE: nome da escola.
- NO_BAIRRO: bairro da escola.
- TP_DEPENDENCIA e DEPENDENCIA: código e nome do ente responsável (Federal, Estadual, Municipal ou Privada).
- TP_LOCALIZACAO e LOCALIZAÇÃO: código e nome da zona (Urbana ou Rural).
- TP_SITUACAO_FUNCIONAMENTO e SITUAÇÃO: código e situação da escola (Ativa ou Inativa).
- TAM_ESCOLA: classificação por número de matrículas (Microescola, Pequena, Média, Grande, Muito Grande, Mega escola ou Inativa), calculada na aba Parâmetros.

Esgoto (1 = sim, 0 = não):
- REDE_PUBLICA, FOSSA_SEPTICA, FOSSA_COMUM, FOSSA e INEXISTENTE: tipo de esgotamento sanitário da escola.
- ESGOTO: coluna calculada que mostra o tipo de esgoto da escola.

Matrículas por modalidade:
- QT_MAT_BAS: total de matrículas da educação básica.
- QT_MAT_INF: educação infantil.
- QT_MAT_FUND: ensino fundamental.
- QT_MAT_MED: ensino médio.
- QT_MAT_PROF: educação profissional.
- QT_MAT_EJA: educação de jovens e adultos.
- QT_MAT_ESP: educação especial.

Matrículas por cor/raça:
- QT_MAT_BAS_BRANCA, QT_MAT_BAS_PRETA, QT_MAT_BAS_PARDA, QT_MAT_BAS_AMARELA e QT_MAT_BAS_INDIGENA: matrículas de cada cor/raça.
- QT_MAT_BAS_ND: matrículas sem declaração de cor/raça.

## Participação do Grupo
O que aprendemos com este projeto: na disciplina Análise de Dados para Pesquisas em Políticas Públicas, trabalhamos ativamente com os dados nacionais do Censo Escolar. Aprendemos a manipular e interpretar os dados e a escolher a melhor forma de comunicá-los com gráficos no Excel.

Papel de cada integrante:
- Arthur: subiu o projeto no GitHub e fez os gráficos no dashboard.
- Kauã: ajudou no desenvolvimento da planilha.
- Roger: ajudou nas fórmulas e nos gráficos do Excel.
- João Pedro: ajudou na comunicação visual das informações no Excel.
- Thiago: ajudou no desenvolvimento da planilha e do projeto, incluindo a representação visual.
- Tomás: ajudou nas fórmulas e nos gráficos do Excel.
