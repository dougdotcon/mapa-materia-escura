"""
Fractal Analysis Toolkit - Based on Omega Theory
================================================
d = ln(3)/ln(4) ≈ 0.6129 (Cantor Set Dimension)

Use this to analyze any dataset for fractal patterns!
"""

import numpy as np
from collections import Counter
from math import factorial
import warnings
warnings.filterwarnings('ignore')

# ==============================================================================
# CONSTANTS FROM OMEGA THEORY
# ==============================================================================
OMEGA = 117.038           # Universal compression factor
CANTOR_DIM = np.log(3) / np.log(4)  # ≈ 0.6129
GAMMA_MU = 1.1195         # Muon exponent ≈ 19/17
BETA = 1.0331             # Fine structure exponent
ALPHA_E = 40.233777       # Electron mass exponent

print(f"""
╔══════════════════════════════════════════════════════════════╗
║     FRACTAL ANALYSIS TOOLKIT - OMEGA THEORY                  ║
╠══════════════════════════════════════════════════════════════╣
║  Ω = {OMEGA:<10}  (Compression Factor)                     ║
║  d = {CANTOR_DIM:.6f}      (Cantor Dimension)                      ║
║  γ = {GAMMA_MU:<10}  (Harmonic Ratio)                       ║
╚══════════════════════════════════════════════════════════════╝
""")


# ==============================================================================
# FRACTAL METRICS
# ==============================================================================

def box_counting_dimension(data, min_boxes=5, max_boxes=50):
    """
    Calculate the box-counting (Minkowski) fractal dimension.
    
    If result ≈ 0.6129, data has Cantor-like structure!
    
    Returns: (dimension, r_squared)
    """
    data = np.array(data)
    data = (data - data.min()) / (data.max() - data.min() + 1e-10)  # Normalize
    
    log_sizes = []
    log_counts = []
    
    for n_boxes in range(min_boxes, max_boxes):
        box_size = 1.0 / n_boxes
        # Count occupied boxes
        boxes = set(int(x / box_size) for x in data if 0 <= x <= 1)
        count = len(boxes)
        
        if count > 0:
            log_sizes.append(np.log(1 / box_size))
            log_counts.append(np.log(count))
    
    if len(log_sizes) < 3:
        return 0.0, 0.0
    
    # Linear regression
    slope, intercept = np.polyfit(log_sizes, log_counts, 1)
    
    # R-squared
    y_pred = np.array(log_sizes) * slope + intercept
    ss_res = np.sum((np.array(log_counts) - y_pred) ** 2)
    ss_tot = np.sum((np.array(log_counts) - np.mean(log_counts)) ** 2)
    r_squared = 1 - ss_res / ss_tot if ss_tot > 0 else 0
    
    return slope, r_squared


def hurst_exponent(series, min_window=10, max_window=None):
    """
    Calculate Hurst exponent using R/S analysis.
    
    H > 0.5: Persistent (trends continue)
    H < 0.5: Anti-persistent (mean-reverting)
    H = 0.5: Random walk
    
    For Cantor: H ≈ 1 - d/2 ≈ 0.69
    """
    series = np.array(series)
    n = len(series)
    
    if max_window is None:
        max_window = min(n // 4, 100)
    
    if max_window <= min_window:
        return 0.5
    
    log_n = []
    log_rs = []
    
    for window in range(min_window, max_window):
        m = n // window
        if m < 2:
            continue
            
        rs_values = []
        for i in range(m):
            subseries = series[i * window:(i + 1) * window]
            mean = np.mean(subseries)
            cumdev = np.cumsum(subseries - mean)
            R = np.max(cumdev) - np.min(cumdev)
            S = np.std(subseries)
            
            if S > 0:
                rs_values.append(R / S)
        
        if rs_values:
            log_n.append(np.log(window))
            log_rs.append(np.log(np.mean(rs_values)))
    
    if len(log_n) < 3:
        return 0.5
    
    H, _ = np.polyfit(log_n, log_rs, 1)
    return max(0, min(1, H))  # Clamp to [0, 1]


def permutation_entropy(series, order=3, delay=1, normalize=True):
    """
    Calculate permutation entropy.
    
    Returns value in [0, 1] if normalized:
    - 0: Completely deterministic
    - 1: Completely random
    - 0.6-0.8: Complex but structured (fractal-like)
    """
    series = np.array(series)
    n = len(series)
    
    if n < order:
        return 0.5
    
    permutations = []
    for i in range(n - (order - 1) * delay):
        window = [series[i + j * delay] for j in range(order)]
        # Rank the values
        perm = tuple(np.argsort(window))
        permutations.append(perm)
    
    counter = Counter(permutations)
    total = len(permutations)
    
    if total == 0:
        return 0.5
    
    entropy = 0
    for count in counter.values():
        p = count / total
        if p > 0:
            entropy -= p * np.log2(p)
    
    if normalize:
        max_entropy = np.log2(factorial(order))
        return entropy / max_entropy if max_entropy > 0 else 0
    
    return entropy


def cantor_gap_analysis(data):
    """
    Analyze data for Cantor-like gap structure.
    
    Cantor set has gaps at 1/3, 1/9, 1/27... positions.
    """
    data = np.array(sorted(data))
    gaps = np.diff(data)
    
    if len(gaps) == 0:
        return {}
    
    mean_gap = np.mean(gaps)
    large_gaps = gaps[gaps > 2 * mean_gap]
    
    # Check if large gaps follow power-law
    gap_ratio = np.mean(large_gaps) / mean_gap if mean_gap > 0 else 0
    
    return {
        'mean_gap': mean_gap,
        'max_gap': np.max(gaps),
        'n_large_gaps': len(large_gaps),
        'gap_ratio': gap_ratio,
        'cantor_like': 2.5 < gap_ratio < 4.5  # ~1/d ratio
    }


def omega_scale_analysis(data):
    """
    Analyze data in terms of Omega scaling.
    
    Find if values cluster at Omega^n levels.
    """
    data = np.array([x for x in data if x > 0])
    
    if len(data) == 0:
        return {}
    
    # Project onto Omega scale
    log_omega = np.log(data) / np.log(OMEGA)
    
    # Find clustering
    levels = np.round(log_omega)
    residues = log_omega - levels
    
    return {
        'mean_level': np.mean(levels),
        'level_spread': np.std(levels),
        'mean_residue': np.mean(np.abs(residues)),
        'clustered_at_omega': np.mean(np.abs(residues)) < 0.3
    }


# ==============================================================================
# COMPLETE ANALYSIS
# ==============================================================================

def full_fractal_analysis(data, name="Data"):
    """
    Run complete fractal analysis on a dataset.
    """
    data = np.array(data)
    
    print(f"\n{'='*60}")
    print(f"📊 FRACTAL ANALYSIS: {name}")
    print(f"{'='*60}")
    print(f"   Samples: {len(data)}")
    print(f"   Range: [{min(data):.2f}, {max(data):.2f}]")
    print(f"   Mean: {np.mean(data):.4f}")
    print(f"   Std: {np.std(data):.4f}")
    
    # 1. Box-counting dimension
    d, r2 = box_counting_dimension(data)
    d_match = "✅ CANTOR!" if abs(d - CANTOR_DIM) < 0.15 else "❌"
    print(f"\n📐 Box-Counting Dimension:")
    print(f"   d = {d:.4f} (R² = {r2:.3f})")
    print(f"   Target (Cantor): {CANTOR_DIM:.4f} {d_match}")
    
    # 2. Hurst exponent
    H = hurst_exponent(data)
    expected_H = 1 - CANTOR_DIM / 2
    h_match = "✅" if abs(H - expected_H) < 0.15 else "❌"
    print(f"\n📈 Hurst Exponent:")
    print(f"   H = {H:.4f}")
    print(f"   Expected (from d): {expected_H:.4f} {h_match}")
    print(f"   Interpretation: {'Persistent' if H > 0.5 else 'Anti-persistent'}")
    
    # 3. Permutation entropy
    PE = permutation_entropy(data)
    pe_ok = "✅ Structured" if 0.4 < PE < 0.9 else "⚠️"
    print(f"\n🎲 Permutation Entropy:")
    print(f"   PE = {PE:.4f}")
    print(f"   {pe_ok} (0=deterministic, 1=random)")
    
    # 4. Cantor gaps
    gaps = cantor_gap_analysis(data)
    print(f"\n🕳️ Gap Analysis:")
    print(f"   Mean gap: {gaps.get('mean_gap', 0):.4f}")
    print(f"   Gap ratio: {gaps.get('gap_ratio', 0):.4f}")
    print(f"   Cantor-like: {'✅ Yes' if gaps.get('cantor_like') else '❌ No'}")
    
    # 5. Omega scale
    omega = omega_scale_analysis(data)
    print(f"\n🌀 Omega Scale:")
    print(f"   Mean level: {omega.get('mean_level', 0):.2f}")
    print(f"   Clustered: {'✅ Yes' if omega.get('clustered_at_omega') else '❌ No'}")
    
    # Overall score
    score = sum([
        abs(d - CANTOR_DIM) < 0.15,
        abs(H - expected_H) < 0.15,
        0.4 < PE < 0.9,
        gaps.get('cantor_like', False),
    ])
    
    print(f"\n{'='*60}")
    print(f"🎯 FRACTAL SCORE: {score}/4")
    if score >= 3:
        print(f"   ⭐ STRONG FRACTAL STRUCTURE DETECTED!")
    elif score >= 2:
        print(f"   📊 Moderate fractal characteristics")
    else:
        print(f"   🎲 Appears mostly random")
    print(f"{'='*60}")
    
    return {
        'dimension': d,
        'dimension_r2': r2,
        'hurst': H,
        'permutation_entropy': PE,
        'gaps': gaps,
        'omega': omega,
        'fractal_score': score
    }


# ==============================================================================
# DEMO / TEST
# ==============================================================================

if __name__ == "__main__":
    
    print("\n" + "="*60)
    print("🧪 TESTING WITH SAMPLE DATA")
    print("="*60)
    
    # Test 1: Pure Cantor-like set
    print("\n\n📌 TEST 1: Simulated Cantor-like Distribution")
    cantor_data = []
    for i in range(1000):
        # Generate numbers avoiding "middle third"
        x = np.random.random()
        while 0.33 < (x * 3) % 1 < 0.66:
            x = np.random.random()
        cantor_data.append(x)
    
    full_fractal_analysis(cantor_data, "Cantor-like Distribution")
    
    # Test 2: Pure random
    print("\n\n📌 TEST 2: Pure Random (Uniform)")
    random_data = np.random.uniform(0, 100, 1000)
    full_fractal_analysis(random_data, "Uniform Random")
    
    # Test 3: Simulated Lotofácil frequencies
    print("\n\n📌 TEST 3: Simulated Lotofácil Frequencies")
    # Simulate 2000 draws, 15 numbers each from 1-25
    lotofacil_freq = np.zeros(25)
    for _ in range(2000):
        draw = np.random.choice(range(25), size=15, replace=False)
        for n in draw:
            lotofacil_freq[n] += 1
    
    full_fractal_analysis(lotofacil_freq, "Lotofácil Frequencies")
    
    # Test 4: Bitcoin-like price series (random walk with drift)
    print("\n\n📌 TEST 4: Simulated Price Series (GARCH-like)")
    price = [100]
    volatility = 0.02
    for _ in range(999):
        ret = np.random.normal(0.0001, volatility)
        volatility = 0.02 + 0.1 * abs(ret)  # Volatility clustering
        price.append(price[-1] * (1 + ret))
    
    full_fractal_analysis(price, "Simulated Price Series")
    
    print("\n\n" + "="*60)
    print("✅ TOOLKIT READY! Use full_fractal_analysis(your_data) on any dataset.")
    print("="*60)
