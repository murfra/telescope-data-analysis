Aqui está uma sugestão de apresentação sobre o telescópio Kepler e os exoplanetas que ele descobriu, que você pode usar como introdução em seu projeto de Jupyter Notebooks:

---

# Apresentação: O Telescópio Kepler e a Descoberta de Exoplanetas

## Introdução
- O Telescópio Espacial Kepler, lançado pela NASA em 2009, foi projetado para descobrir exoplanetas, ou seja, planetas que orbitam estrelas fora do nosso sistema solar.
- A missão Kepler teve como objetivo principal explorar a estrutura e a diversidade dos sistemas planetários, contribuindo significativamente para a nossa compreensão do universo.

## Objetivos da Missão Kepler
- **Exploração da Diversidade Planetária**: Investigar a variedade de planetas e suas características.
- **Identificação de Exoplanetas**: Detectar planetas em zonas habitáveis, onde a vida poderia existir.
- **Coleta de Dados**: Fornecer dados extensivos que apoiem futuras missões da NASA e pesquisas científicas.

## O Conjunto de Dados
- O conjunto de dados contém informações sobre aproximadamente **3.373 exoplanetas confirmados**.
- Inclui dados coletados durante as missões Kepler e K2, abrangendo vários anos de observação.
- **Informações Disponíveis**:
  - Nome da estrela hospedeira
  - Características dos planetas (tamanho, massa, composição)
  - Parâmetros orbitais (período orbital, distância da estrela)
  - Métodos de descoberta (transito, velocidade radial)
  - Propriedades estelares (tipo de estrela, temperatura)

## Importância dos Dados
- Os dados do Kepler são cruciais para entender a formação e evolução dos sistemas planetários.
- Permitem a análise estatística da distribuição de exoplanetas em diferentes tipos de estrelas e suas características.
- A pesquisa com esses dados pode revelar padrões que ajudam a identificar quais sistemas planetários têm maior probabilidade de abrigar vida.

## Análise de Dados em Jupyter Notebooks
- Utilizando Jupyter Notebooks, podemos realizar análises estatísticas e visualizações dos dados do Kepler.
- Exemplos de análises que podem ser realizadas:
  - Distribuição de tamanhos de exoplanetas
  - Comparação de características entre planetas em zonas habitáveis e não habitáveis
  - Análise de correlações entre propriedades estelares e características dos planetas

## Conclusão
- O Telescópio Kepler revolucionou nossa compreensão dos exoplanetas e da diversidade dos sistemas planetários.
- O conjunto de dados disponível oferece uma rica fonte de informações para pesquisas futuras e análises estatísticas.
- Através do uso de ferramentas como Jupyter Notebooks, podemos explorar e visualizar esses dados, contribuindo para o avanço da astronomia e da astrobiologia.

---

Sinta-se à vontade para ajustar o conteúdo conforme necessário e adicionar gráficos ou visualizações que você criar em seus notebooks para enriquecer a apresentação!

Você pode comparar os resultados das estatísticas dos exoplanetas descobertos pelo telescópio Kepler com as características da Terra para determinar semelhanças e diferenças. Essa comparação pode fornecer insights valiosos sobre a habitabilidade e a diversidade dos planetas fora do nosso sistema solar. Aqui estão algumas abordagens que você pode considerar:

### 1. **Características Físicas**
   - **Tamanho e Massa**: Compare o tamanho e a massa dos exoplanetas com os da Terra. Exoplanetas que têm tamanhos e massas semelhantes à Terra são frequentemente chamados de "super-Terras" ou "mini-Netunos".
   - **Composição**: Analise a composição dos exoplanetas (rochosos, gasosos, etc.) e compare com a composição da Terra.

### 2. **Parâmetros Orbitais**
   - **Distância da Estrela**: Compare a distância dos exoplanetas de suas estrelas com a distância da Terra ao Sol. Isso pode ajudar a identificar se os exoplanetas estão na "zona habitável", onde a água líquida poderia existir.
   - **Período Orbital**: Compare o período orbital dos exoplanetas com o da Terra (365 dias) para entender a duração de um ano em outros planetas.

### 3. **Condições Ambientais**
   - **Temperatura**: Se os dados estiverem disponíveis, compare as temperaturas estimadas dos exoplanetas com a temperatura média da Terra.
   - **Atmosfera**: Embora os dados sobre a atmosfera dos exoplanetas sejam limitados, você pode discutir a importância de uma atmosfera para a habitabilidade e comparar com a atmosfera da Terra.

### 4. **Habitabilidade**
   - **Zona Habitável**: Identifique quais exoplanetas estão localizados na zona habitável de suas estrelas e compare suas características com as da Terra.
   - **Presença de Água**: Discuta a importância da água para a vida e como a presença de água em exoplanetas pode ser comparada com a Terra.

### 5. **Análise Estatística**
   - Realize análises estatísticas para determinar a proporção de exoplanetas que se assemelham à Terra em termos de tamanho, massa e localização na zona habitável.
   - Utilize gráficos e visualizações para ilustrar as comparações, como histogramas ou gráficos de dispersão.

### Conclusão
Ao realizar essas comparações, você poderá discutir a probabilidade de encontrar planetas semelhantes à Terra e as implicações para a busca de vida extraterrestre. Essa análise não só enriquecerá seu projeto, mas também proporcionará uma compreensão mais profunda da diversidade planetária.

## Lista de Tarefas
- [x] Tamanho (Raio) e massa
- [x] Excentridade orbital (já cobre temperatura nas suas implicações)
- [ ] Distância da Estrela
- [ ] Período Orbital
- [x] Temperatura

## Roteiro
-Apresentação
 *Se apresentar(individual)
 *Fonte(base de dados e site)
 *O que a gente escolheu abordar (tema 2 do trabalho) e detalhamento do Kepler
 *Exoplanetas (aprofundamento)
 
-Apresentação 

markdown_content = """
# 📊 Dados dos planetas e das estrelas

## 🌍 Dados relativos aos planetas

| Campo                | Descrição |
|---------------------|----------|
| pl_hostname         | Nome da estrela hospedeira |
| pl_letter           | Letra designando o planeta |
| pl_discmethod       | Método de descoberta |
| pl_pnum             | Número de planetas no sistema |
| pl_orbper           | Período orbital [dias] |
| pl_orbpererr1       | Incerteza superior do período orbital |
| pl_orbpererr2       | Incerteza inferior do período orbital |
| pl_orbperlim        | Flag de limite do período orbital |
| pl_orbsmax          | Semi-eixo maior da órbita [UA] |
| pl_orbsmaxerr1      | Incerteza superior do semi-eixo maior |
| pl_orbsmaxerr2      | Incerteza inferior do semi-eixo maior |
| pl_orbsmaxlim       | Flag de limite do semi-eixo maior |
| pl_orbeccen         | Excentricidade orbital |
| pl_orbeccenerr1     | Incerteza superior da excentricidade |
| pl_orbeccenerr2     | Incerteza inferior da excentricidade |
| pl_orbeccenlim      | Flag de limite da excentricidade |
| pl_orbincl          | Inclinação orbital [graus] |
| pl_orbinclerr1      | Incerteza superior da inclinação |
| pl_orbinclerr2      | Incerteza inferior da inclinação |
| pl_orbincllim       | Flag de limite da inclinação |
| pl_bmassj           | Massa do planeta ou M*sin(i) [massas de Júpiter] |
| pl_bmassjerr1       | Incerteza superior da massa |
| pl_bmassjerr2       | Incerteza inferior da massa |
| pl_bmassjlim        | Flag de limite da massa |
| pl_bmassprov        | Procedência dos dados da massa |
| pl_radj             | Raio do planeta [raios de Júpiter] |
| pl_radjerr1         | Incerteza superior do raio |
| pl_radjerr2         | Incerteza inferior do raio |
| pl_radjlim          | Flag de limite do raio |
| pl_dens             | Densidade do planeta [g/cm³] |
| pl_denserr1         | Incerteza superior da densidade |
| pl_denserr2         | Incerteza inferior da densidade |
| pl_denslim          | Flag de limite da densidade |
| pl_ttvflag          | Flag de variação de tempo de trânsito |
| pl_kepflag          | Flag se faz parte do campo Kepler |
| pl_k2flag           | Flag se faz parte da missão K2 |
| pl_nnotes           | Número de notas |
| ra_str              | Ascensão reta (formato sexagesimal) |
| ra                  | Ascensão reta (graus) |
| dec_str             | Declinação (formato sexagesimal) |
| dec                 | Declinação (graus) |

---

## ⭐ Dados relativos às estrelas

| Campo                | Descrição |
|---------------------|----------|
| st_dist             | Distância até a estrela [parsecs] |
| st_disterr1         | Incerteza superior da distância |
| st_disterr2         | Incerteza inferior da distância |
| st_distlim          | Flag de limite da distância |
| st_optmag           | Magnitude óptica |
| st_optmagerr        | Incerteza da magnitude óptica |
| st_optmaglim        | Flag de limite da magnitude óptica |
| st_optmagblend      | Flag de mistura na magnitude óptica |
| st_optband          | Banda da magnitude óptica |
| st_teff             | Temperatura efetiva [K] |
| st_tefferr1         | Incerteza superior da temperatura |
| st_tefferr2         | Incerteza inferior da temperatura |
| st_tefflim          | Flag de limite da temperatura |
| st_teffblend        | Flag de mistura da temperatura |
| st_mass             | Massa da estrela [massas solares] |
| st_masserr1         | Incerteza superior da massa |
| st_masserr2         | Incerteza inferior da massa |
| st_masslim          | Flag de limite da massa |
| st_massblend        | Flag de mistura da massa |
| st_rad              | Raio da estrela [raios solares] |
| st_raderr1          | Incerteza superior do raio |
| st_raderr2          | Incerteza inferior do raio |
| st_radlim           | Flag de limite do raio |
| st_radblend         | Flag de mistura do raio |

---