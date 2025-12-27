# Mapa de Matéria Escura do ACT

Este repositório documenta a criação do **maior e mais detalhado mapa de matéria escura já produzido** a partir da radiação cósmica de fundo (CMB), utilizando dados do **Atacama Cosmology Telescope (ACT)**. O projeto combina instrumentação avançada, algoritmos sofisticados e software aberto para revelar a distribuição invisível de massa no Universo.

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

- **Dados Públicos**: Disponíveis no repositório [LAMBDA da NASA](https://lambda.gsfc.nasa.gov/product/act/actadv_dr6_lensing_maps_info.html).
- **Código Fonte**: Scripts e pipelines utilizados para o processamento estão disponíveis neste repositório.

---

## Começando

*Pré-requisitos: Python 3.8+, CAMB, Falafel, Tempura, Healpy.*

1. **Clonar o repositório:**
   bash
   git clone https://github.com/seuusuario/act-dark-matter-map.git
   cd act-dark-matter-map
   

2. **Instalar dependências:**
   bash
   pip install -r requirements.txt
   

3. **Executar o script de visualização:**
   bash
   python scripts/visualize_map.py
   

---

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.
