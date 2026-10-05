# Projeto 4 – Painel do Censo Escolar 2024 (2ª entrega do Projeto 2)

Objetivo: Este projeto reúne, em um painel dinâmico no Excel, dados do Censo Escolar 2024 (INEP) sobre as escolas da rede estadual de Osasco (SP). O painel compara a distribuição de matrículas por raça/cor e por modalidade de ensino e a infraestrutura de esgoto das escolas. O intuito é permitir que essas diferenças sejam vistas de forma clara e interativa, por meio de tabelas dinâmicas, gráfico dinâmico e segmentação.

Como usar: Abrir o arquivo `Projeto_2-_2nda_entrega_github.xlsx` no Excel. As abas de dados são a Microdados (base tratada) e a Sheet2; as abas Dependencia, Localizacao, LocDiferenciada e Situacao são tabelas de apoio, usadas para traduzir os códigos em texto. As tabelas dinâmicas e o gráfico dinâmico estão ligados à base, e as segmentações (filtros clicáveis) permitem filtrar o painel por município e por outras categorias. Basta clicar nos botões da segmentação para o painel se atualizar.

Prints do resultado:

Imagem 1: Gráficos do painel
<img width="1025" height="514" alt="Screenshot 2026-09-08 at 22 54 21" src="https://github.com/user-attachments/assets/67a8a61f-ae20-4a73-9d32-dd4c4f725d8e" />

## Uso de Inteligência Artificial

Ferramenta utilizada: Claude

Para que foi usada: Para buscar informações e sugestões de formas adequadas de ilustrar os gráficos do painel.

Exemplo de prompt utilizado: "Como fazer os dados de distribuição de raça por modalidade escolar ser mais visualmente agradável"

O que foi ajustado manualmente: Títulos dos gráficos e outros ajustes pequenos de formatação.

## Fonte de Dados

Fonte oficial: Censo Escolar 2024 (INEP)

Link oficial: https://censobasico.inep.gov.br/censobasico_2024/

O que os dados representam: O Censo Escolar é a principal pesquisa estatística sobre a educação básica no Brasil, realizada pelo INEP com informações declaradas pelas escolas. Os dados descrevem cada escola: onde fica, quem a administra, sua infraestrutura (água, energia, esgoto e lixo) e o número de matrículas por etapa de ensino, sexo, raça/cor e faixa etária.

Estrutura: Cada linha da base é uma escola. As principais colunas usadas são:
- NO_MUNICIPIO e SG_UF: município e estado onde a escola fica.
- NO_ENTIDADE: nome da escola.
- TP_DEPENDENCIA: código da dependência administrativa (federal, estadual, municipal ou privada), traduzido na coluna Dependencia.DEPENDENCIA.
- TP_LOCALIZACAO: código de localização (urbana ou rural), traduzido na coluna Localizacao.LOCALIZACAO.
- TAM_ESCOLA: porte da escola (micro, pequena, média, grande ou muito grande).
- IN_ESGOTO_*: indicadores do tipo de esgotamento sanitário (rede pública, fossa séptica, fossa comum etc.).
- QT_MAT_INF, QT_MAT_FUND, QT_MAT_MED, QT_MAT_EJA, QT_MAT_PROF e QT_MAT_ESP: matrículas por modalidade (infantil, fundamental, médio, EJA, profissional e especial).
- QT_MAT_BAS_BRANCA, _PRETA, _PARDA, _AMARELA e _INDIGENA: matrículas da educação básica por raça/cor.

## Participação do Grupo

O que aprendemos com este projeto: Ao trabalhar diretamente com os dados nacionais do Censo Escolar, aprendemos a manipular e tratar uma base grande, a interpretar os resultados e a escolher a melhor forma de comunicá-los usando o Excel como ferramenta.

Papel de cada integrante:
- Arthur: Responsável pelo upload do projeto no GitHub e pelos gráficos no Dash.
- Kauã: Auxiliou no desenvolvimento da planilha.
- Roger: Auxiliou no desenvolvimento das fórmulas e dos gráficos no Excel.
- João Pedro: Auxiliou no desenvolvimento da comunicação visual das informações no Excel.
- Thiago: Auxiliou no desenvolvimento da planilha e do projeto, incluindo a representação visual.
- Tomás: Auxiliou no desenvolvimento das fórmulas e dos gráficos no Excel.
