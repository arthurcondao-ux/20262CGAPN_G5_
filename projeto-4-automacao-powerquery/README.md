# Projeto 4 – Painel do Censo Escolar 2024 (Projeto 2 revisado)

Objetivo: Este projeto monta, no Excel, um painel dinâmico com os dados do Censo Escolar 2024 (INEP) das 467 escolas de Osasco (SP). Por meio de tabelas dinâmicas, gráficos e segmentações, o painel mostra o perfil das escolas por dependência administrativa, porte e situação de funcionamento, além da infraestrutura de esgoto e coleta de lixo e das matrículas por sexo. O intuito é permitir que as diferenças entre esses grupos sejam vistas de forma clara e interativa.

Como usar: Abrir o arquivo `Projeto_2-_2nda_entrega_github.xlsx` no Excel. A aba Controle reúne as duas tabelas dinâmicas e as três segmentações (filtros clicáveis): Dependência, Situação de funcionamento e Porte da escola. Ao clicar nos botões da segmentação, as tabelas se atualizam. A aba Microdados é a base tratada, e as abas Dependencia, Localizacao, LocDiferenciada e Situacao são tabelas de apoio que traduzem códigos em texto.

Prints do resultado:

Imagem 1: Gráficos do painel
<img width="1025" height="514" alt="Screenshot 2026-09-08 at 22 54 21" src="https://github.com/user-attachments/assets/67a8a61f-ae20-4a73-9d32-dd4c4f725d8e" />

## Uso de Inteligência Artificial

Ferramenta utilizada: Claude

Para que foi usada: Para buscar informações e pensar em formas diferentes e adequadas de ilustrar os gráficos do painel.

Exemplo de prompt utilizado: "Como fazer os dados de distribuição de raça por modalidade escolar ser mais visualmente agradável"

O que foi ajustado manualmente: Títulos dos gráficos e outros ajustes pequenos de formatação.

## Fonte de Dados

Fonte oficial: Censo Escolar 2024 (INEP)

Link oficial: https://censobasico.inep.gov.br/censobasico_2024/

O que os dados representam: O Censo Escolar é a principal pesquisa estatística sobre a educação básica no Brasil, realizada pelo INEP com informações declaradas pelas escolas. Cada linha da base é uma escola de Osasco e descreve onde ela fica, quem a administra, se está ativa, sua infraestrutura (água, energia, esgoto e lixo) e suas matrículas por etapa de ensino, sexo, raça/cor e faixa etária.

Estrutura: A base (aba Microdados) tem 467 linhas e 69 colunas. As principais são:
- NO_MUNICIPIO, SG_UF, NO_ENTIDADE e CO_ENTIDADE: município, estado, nome e código da escola.
- TP_DEPENDENCIA: código da dependência administrativa, traduzido para Federal, Estadual, Municipal ou Privada na coluna Dependencia.DEPENDENCIA.
- TP_LOCALIZACAO e TP_LOCALIZACAO_DIFERENCIADA: localização (urbana ou rural) e localização diferenciada (assentamento, terra indígena, comunidade quilombola etc.), traduzidas pelas abas de apoio.
- TP_SITUACAO_FUNCIONAMENTO: código de funcionamento, traduzido para Ativa ou Inativa em Situacao.SITUACAO.
- TAM_ESCOLA: porte da escola (Micro, Pequena, Média, Grande, Muito Grande ou Sem Dados).
- Agua, Energia, Esgoto e Lixo: colunas calculadas a partir dos indicadores IN_AGUA_*, IN_ENERGIA_*, IN_ESGOTO_* e IN_LIXO_* (por exemplo, "Rede Publica" ou "Coleta").
- QT_MAT_BAS, QT_MAT_INF, QT_MAT_FUND, QT_MAT_MED, QT_MAT_PROF, QT_MAT_EJA e QT_MAT_ESP: matrículas totais e por modalidade de ensino.
- QT_MAT_BAS_FEM e QT_MAT_BAS_MASC: matrículas por sexo.
- QT_MAT_BAS_BRANCA, _PRETA, _PARDA, _AMARELA e _INDIGENA: matrículas por raça/cor.
- QT_MAT_BAS_0_3 até QT_MAT_BAS_18_MAIS: matrículas por faixa etária.

## Participação do Grupo

O que aprendemos com este projeto: Ao trabalhar diretamente com os dados nacionais do Censo Escolar, aprendemos a tratar uma base grande, a traduzir códigos em categorias com tabelas de apoio, a montar tabelas dinâmicas com segmentações e a escolher a melhor forma de comunicar os resultados usando o Excel como ferramenta.

Papel de cada integrante:
- Arthur: Responsável pelo upload do projeto no GitHub e pelos gráficos no Dash.
- Kauã: Auxiliou no desenvolvimento da planilha.
- Roger: Auxiliou no desenvolvimento das fórmulas e dos gráficos no Excel.
- João Pedro: Auxiliou no desenvolvimento da comunicação visual das informações no Excel.
- Thiago: Auxiliou no desenvolvimento da planilha e do projeto, incluindo a representação visual.
- Tomás: Auxiliou no desenvolvimento das fórmulas e dos gráficos no Excel.
