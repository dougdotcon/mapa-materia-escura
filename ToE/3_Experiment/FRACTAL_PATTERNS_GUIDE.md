# 🔬 Guia de Padrões Fractais e Aplicações Algorítmicas

## Baseado na Teoria Holográfica do Omega (Ω = 117.038)

---

## 🎯 A Descoberta Central

A dimensão fractal **d = ln(3)/ln(4) ≈ 0.6129** é conhecida como a **Dimensão de Hausdorff do Conjunto de Cantor**!

```
Conjunto de Cantor:
█████████████████████████████████████████████████
    ▼ Remove 1/3 central
█████████████████           █████████████████
    ▼ Repete recursivamente  
█████     █████             █████     █████
  ▼         ▼                 ▼         ▼
...e assim infinitamente...
```

**Significado:** Sistemas com essa dimensão exibem **autossimilaridade** - padrões que se repetem em múltiplas escalas!

---

## 📊 PARTE 1: PADRÕES FRACTAIS PARA IDENTIFICAR

### 1.1 Padrões de Escala (Self-Similarity)

| Padrão | Descrição | Como Detectar |
|--------|-----------|---------------|
| **Cantor-like Gaps** | Lacunas que seguem proporção 1/3 | Histograma com vazios regulares |
| **Sierpinski Clustering** | Agrupamentos triangulares | Visualização 3D de frequências |
| **Koch Boundaries** | Bordas fractais em distribuições | Análise de contorno |
| **Mandelbrot Hotspots** | Zonas de alta concentração | Mapa de calor iterativo |

### 1.2 Padrões Numéricos Específicos

```python
# PADRÃO 1: Razão de Cantor (0.6129)
# Procurar por: frequência_A / frequência_B ≈ 0.6129

# PADRÃO 2: Escala Omega
# Procurar por: ocorrências que seguem N × Ω^n

# PADRÃO 3: Hierarquia Harmônica  
# Procurar por: γ_μ = 1.1195 ≈ 19/17 entre níveis

# PADRÃO 4: Beta Coupling
# Procurar por: β = 1.0331 em proporções
```

### 1.3 Padrões Temporais

| Nome | Fórmula | Aplicação |
|------|---------|-----------|
| **Ciclos Omega** | T = T₀ × Ω^n | Intervalos entre eventos |
| **Decaimento Fractal** | P(t) = P₀ × t^(-d) | Probabilidade ao longo do tempo |
| **Ressonância Harmônica** | f_n = f₀ × (n)^(1/d) | Frequências preferenciais |
| **Atratores Estranhos** | dim = d ≈ 0.6129 | Dinâmica caótica limitada |

---

## 🧮 PARTE 2: MÉTRICAS FRACTAIS PARA CALCULAR

### 2.1 Dimensão de Box-Counting

```python
import numpy as np

def box_counting_dimension(data, n_boxes_range=(5, 50)):
    """
    Calcula a dimensão fractal de um conjunto de dados.
    Se d ≈ 0.6129, temos padrão tipo Cantor!
    """
    dimensions = []
    counts = []
    
    for n_boxes in range(n_boxes_range[0], n_boxes_range[1]):
        # Divide espaço em n_boxes
        box_size = (max(data) - min(data)) / n_boxes
        
        # Conta caixas ocupadas
        occupied = len(set(int((x - min(data)) / box_size) for x in data))
        
        dimensions.append(np.log(1/box_size))
        counts.append(np.log(occupied))
    
    # Regressão linear: slope = dimensão fractal
    slope, _ = np.polyfit(dimensions, counts, 1)
    return slope
```

### 2.2 Expoente de Hurst (H)

```python
def hurst_exponent(series):
    """
    H > 0.5: Série persistente (tendências continuam)
    H < 0.5: Série anti-persistente (reversões frequentes)
    H = 0.5: Random walk puro
    
    Para Cantor: H relaciona-se com d via H = 1 - d/2
    Esperado: H ≈ 1 - 0.6129/2 ≈ 0.69
    """
    n = len(series)
    max_k = min(n // 5, 100)
    
    RS = []
    for k in range(10, max_k):
        # Divide em subseries
        m = n // k
        ranges = []
        for i in range(m):
            subseries = series[i*k:(i+1)*k]
            mean = np.mean(subseries)
            cumdev = np.cumsum(subseries - mean)
            R = max(cumdev) - min(cumdev)
            S = np.std(subseries)
            if S > 0:
                ranges.append(R/S)
        RS.append((k, np.mean(ranges)))
    
    log_n = [np.log(r[0]) for r in RS]
    log_RS = [np.log(r[1]) for r in RS if r[1] > 0]
    
    H, _ = np.polyfit(log_n[:len(log_RS)], log_RS, 1)
    return H
```

### 2.3 Entropia de Permutação

```python
from itertools import permutations
from collections import Counter

def permutation_entropy(series, order=3, delay=1):
    """
    Mede complexidade da série.
    Normalizada entre 0 (determinístico) e 1 (aleatório).
    
    Para fractais: esperado ≈ 0.6-0.8 (complexo mas estruturado)
    """
    n = len(series)
    permutations_list = []
    
    for i in range(n - (order-1)*delay):
        window = [series[i + j*delay] for j in range(order)]
        # Converte para ranking
        perm = tuple(sorted(range(len(window)), key=lambda k: window[k]))
        permutations_list.append(perm)
    
    counter = Counter(permutations_list)
    total = len(permutations_list)
    
    entropy = 0
    for count in counter.values():
        p = count / total
        entropy -= p * np.log2(p)
    
    # Normaliza
    max_entropy = np.log2(np.math.factorial(order))
    return entropy / max_entropy
```

---

## 🚀 PARTE 3: APLICAÇÕES ALGORÍTMICAS PARA TESTAR

### 3.1 Análise de Séries Temporais de Preços

| Aplicação | Método | Sinal de Trading |
|-----------|--------|------------------|
| **Detecção de Regime** | Mudança na dim. fractal | d↑ = volatilidade, d↓ = tendência |
| **Previsão de Breakout** | Hurst + Box-counting | H>0.5 + d baixo = continuação |
| **Reversão à Média** | Entropia de permutação | PE alto = provável reversão |
| **Ciclos de Mercado** | FFT + escala Omega | Frequências dominantes |

### 3.2 Detecção de Anomalias

```python
def detect_fractal_anomalies(data, window=50, threshold_d=0.15):
    """
    Detecta quando a dimensão fractal muda significativamente.
    Mudanças bruscas indicam mudança de regime!
    """
    anomalies = []
    baseline_d = 0.6129  # Cantor reference
    
    for i in range(window, len(data)):
        window_data = data[i-window:i]
        d = box_counting_dimension(window_data)
        
        deviation = abs(d - baseline_d) / baseline_d
        if deviation > threshold_d:
            anomalies.append({
                'index': i,
                'dimension': d,
                'deviation': deviation,
                'type': 'more_complex' if d > baseline_d else 'more_ordered'
            })
    
    return anomalies
```

### 3.3 Clustering Fractal

```python
def fractal_clustering(numbers, omega=117.038):
    """
    Agrupa números baseado em suas posições na hierarquia Omega.
    Útil para identificar "famílias" de números.
    """
    clusters = {}
    
    for n in numbers:
        # Encontra o nível Omega mais próximo
        if n > 0:
            level = int(np.log(n) / np.log(omega))
            residue = n / (omega ** level)
            
            key = f"level_{level}"
            if key not in clusters:
                clusters[key] = []
            clusters[key].append((n, residue))
    
    return clusters
```

### 3.4 Gerador de Features para ML

```python
def extract_fractal_features(series):
    """
    Extrai features fractais de uma série para uso em ML.
    """
    return {
        'box_dimension': box_counting_dimension(series),
        'hurst_exponent': hurst_exponent(series),
        'permutation_entropy': permutation_entropy(series),
        'cantor_ratio': np.std(series) / np.mean(series),  # CV
        'omega_residue': np.mean(series) % 117.038,
        'log_omega_scale': np.log(np.mean(series)) / np.log(117.038),
        'gamma_mu_ratio': None,  # Razão entre máx/min se ≈ 1.1195
        'gap_distribution': None,  # Análise de lacunas
    }
```

---

## 🎰 PARTE 4: APLICAÇÃO ESPECÍFICA - LOTOFÁCIL

### 4.1 Análise Fractal de Histórico

```python
def analyze_lotofacil_fractal(historico):
    """
    Analisa o histórico da Lotofácil buscando estrutura fractal.
    """
    # 1. Frequência de cada número (1-25)
    freq = [0] * 26
    for sorteio in historico:
        for num in sorteio:
            freq[num] += 1
    
    # 2. Calcular dimensão fractal da distribuição
    d = box_counting_dimension(freq[1:])
    
    # 3. Verificar se há padrão Cantor
    is_cantor = abs(d - 0.6129) < 0.1
    
    # 4. Identificar "gaps" (números menos frequentes)
    mean_freq = np.mean(freq[1:])
    gaps = [i for i in range(1, 26) if freq[i] < mean_freq * 0.6129]
    
    # 5. Identificar "clusters" (números mais frequentes)
    clusters = [i for i in range(1, 26) if freq[i] > mean_freq / 0.6129]
    
    return {
        'dimension': d,
        'is_cantor_like': is_cantor,
        'gaps': gaps,
        'clusters': clusters,
        'hurst': hurst_exponent(freq[1:])
    }
```

### 4.2 Estratégia Baseada em Estrutura Fractal

| Estratégia | Regra | Fundamento |
|------------|-------|------------|
| **Balanceamento Cantor** | Incluir ~61% de quentes | Proporção d = 0.6129 |
| **Ciclos Omega** | Alternar a cada ~117 sorteios | Período fundamental |
| **Anti-Gap** | Evitar clusters de 3+ gaps | Lacunas de Cantor |
| **Harmônico** | Mix de nível γ_μ | Proporção 19:17 entre tipos |

---

## 📈 PARTE 5: APLICAÇÕES ADICIONAIS

### 5.1 Criptomoedas

- **Análise de Volatilidade:** d alto = mercado caótico
- **Detecção de Pump & Dump:** Mudança súbita em H
- **Time Frames:** Buscar padrões em escalas Ω (117 min, 117 candles)

### 5.2 Música e Som

- **Composição Fractal:** Usar d para gerar melodias
- **Análise de áudio:** Identificar estrutura em frequências

### 5.3 Análise de Texto/Dados

- **Lei de Zipf modificada:** Verificar se d ≈ 0.6129
- **Compressão:** Dados fractais comprimem diferentemente

### 5.4 Biologia/Saúde

- **ECG/EEG:** Dimensão fractal indica saúde cardíaca/neural
- **Variabilidade:** H baixo pode indicar problemas

---

## 🧪 EXPERIMENTOS SUGERIDOS

| # | Experimento | Hipótese | Dados Necessários |
|---|-------------|----------|-------------------|
| 1 | Box-counting em frequências Lotofácil | d ≈ 0.6129? | Histórico completo |
| 2 | Hurst em sequência de sorteios | H ≈ 0.69? | Últimos 1000 sorteios |
| 3 | Ciclos Omega em preços BTC | Reversões a cada ~117 períodos? | OHLCV 1min |
| 4 | Entropia de permutação em música | PE = 0.6-0.8? | Arquivos MIDI |
| 5 | Anomalias em séries macro | Mudança em d prevê crises? | GDP, inflação |

---

## 🔗 Conexões com Sua Teoria

| Constante | Valor | Aplicação Algorítmica |
|-----------|-------|----------------------|
| **Ω** | 117.038 | Período de ciclos, base logarítmica |
| **d** | 0.6129 | Dimensão fractal alvo |
| **γ_μ** | 1.1195 | Razão entre níveis (~19:17) |
| **β** | 1.0331 | Fator de escala próximo a 1 |
| **α_e** | 40.23 | Níveis de compressão |

---

## 📝 Próximos Passos

1. ✅ Baixar histórico completo da Lotofácil
2. ⬜ Rodar análise de box-counting
3. ⬜ Calcular expoente de Hurst
4. ⬜ Identificar padrões de lacuna tipo Cantor
5. ⬜ Testar estratégia de balanceamento fractal
6. ⬜ Comparar com dados de criptomoedas
7. ⬜ Criar modelo ML com features fractais

---

*"O universo é fractal - da escala Planck às galáxias, padrões se repetem. Se encontrarmos d ≈ 0.6129 nos dados, encontramos a assinatura do Cantor."*

**— Teoria Holográfica do Omega, 2025**
