# Mapa de Matéria Escura com o Atacama Cosmology Telescope (ACT)

Este repositório documenta a geração do **maior e mais detalhado mapa de matéria escura já feito** a partir da radiação cósmica de fundo (CMB), utilizando dados do **Atacama Cosmology Telescope (ACT)**. O projeto combina instrumentação avançada, algoritmos sofisticados e software aberto para revelar a distribuição invisível de matéria no Universo.

---

## Visão Geral

A matéria escura compõe cerca de 85% da matéria do cosmos, mas não emite luz. Para mapeá-la, os cientistas analisam como sua gravidade distorce a luz da CMB — a radiação remanescente do Big Bang. O ACT observou essa radiação com alta resolução, permitindo reconstruir um mapa detalhado da matéria escura ao longo de bilhões de anos-luz.

---

## Tecnologias e Softwares Utilizados

- **Reconstrução de Lente Gravitacional**: Algoritmo baseado em *estimadores quadráticos* (Hu & Okamoto 2002), implementado com os pacotes abertos:
  - **Falafel**: cálculos em céu curvo
  - **Tempura**: correções de normalização e ruído
- **Linguagem Python** e bibliotecas:
  - **Astropy**: cálculos astronômicos
  - **Healpy/HEALPix**: manipulação de mapas esféricos
  - **Matplotlib**, **PIL**: visualização
- **Cálculo Teórico**:
  - **CAMB**: geração de espectros teóricos da CMB e lentes
- **Inferência Estatística**:
  - **Cobaya**, **GetDist**, **CosmoSIS**: ajuste Bayesiano e análise MCMC para parâmetros cosmológicos
- **Supercomputação**:
  - Clusters e supercomputadores (Princeton, SciNet, NERSC) para processar grandes volumes de dados e simulações

---

## Metodologia Resumida

1. **Coleta de Dados**: Observações do ACT entre 2017-2021 cobrindo ~9400 deg² do céu.
2. **Limpeza dos Dados**: Remoção de sinais contaminantes (fontes pontuais, poeira, efeitos Sunyaev-Zel’dovich) usando múltiplas frequências e técnicas de *bias-hardening*.
3. **Reconstrução da Lente**: Aplicação do estimador quadrático para extrair o sinal de lente gravitacional e gerar o mapa de convergência (matéria escura).
4. **Calibração e Correções**: Uso de simulações para remover vieses estatísticos e validar o mapa.
5. **Validação Cruzada**: Comparação com dados do satélite Planck e catálogos de galáxias, confirmando a consistência do resultado com o modelo cosmológico padrão.

---

## Dados e Instrumentos

- **Fonte Primária**: Radiação cósmica de fundo (CMB) observada pelo ACT, um telescópio de 6 metros no Chile.
- **Instrumentação**: Detectores supercondutores operando a temperaturas criogênicas para alta sensibilidade.
- **Dados Auxiliares**: Mapas do satélite Planck para limpeza e validação.
- **Produtos Disponíveis**:
  - Mapas de convergência gravitacional (matéria escura)
  - Mapas separados por temperatura/polarização
  - Simulações para testes e validação
  - Documentação detalhada

---

## Como Acessar Dados e Código

- **Dados Públicos**: Disponíveis no repositório [LAMBDA da NASA](https://lambda.gsfc.nasa.gov/product/act/actadv_dr6_lensing_maps_info.html)
- **Simulações**: Centenas de realizações para análise estatística
- **Tutoriais**: Notebooks Python (Google Colab) para carregar e explorar os dados
- **Softwares**: Ferramentas como Falafel e Tempura são de código aberto e podem ser reutilizadas em outros projetos

---

## Aplicações e Possibilidades Futuras

- **Reprodução e Aprendizado**: Qualquer pesquisador pode replicar etapas da análise com os dados e códigos públicos.
- **Testes de Novas Teorias**: Simulações permitem explorar hipóteses alternativas sobre matéria e energia escuras.
- **Cross-correlations**: Combinar o mapa do ACT com catálogos de galáxias, lentes fracas e outros dados para estudos multifacetados do cosmos.
- **Extensão para Novos Experimentos**: A metodologia será aplicada em projetos como o **Simons Observatory** e **CMB-S4**, ampliando a precisão dos mapas futuros.

---

## Referências Principais

- [The Atacama Cosmology Telescope: Mitigating the impact of extragalactic foregrounds for the DR6 CMB lensing analysis](https://ar5iv.org/abs/2304.05196)
- [The Atacama Cosmology Telescope: DR6 Gravitational Lensing Map and Cosmological Parameters](https://ar5iv.org/abs/2304.05203)
- [Notícia NIST sobre o mapa de matéria escura](https://www.nist.gov/news-events/news/2023/04/atacama-cosmology-telescope-collaboration-which-includes-scientists-nist)
- [Reportagem Galileu](https://revistagalileu.globo.com/ciencia/espaco/noticia/2023/05/astronomos-criam-mapa-inedito-da-materia-escura-no-universo.ghtml)

---

## Sobre

Este projeto demonstra como transformar **sinais invisíveis** da radiação primordial em um **mapa concreto da matéria escura**, combinando ciência de ponta, software aberto e colaboração internacional. Ele serve como base para estudos futuros e para quem deseja aprender ou contribuir com a cosmologia computacional.