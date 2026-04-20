import math
import random
import time

# --- EARTH PHYSICAL CONSTANTS (THE "GUARANTEE" LAYER) ---
G_EARTH = 9.80665        # m/s^2 (Standard Gravity)
B_FIELD = 3.1e-5         # Tesla (Geomagnetic Flux)
SALINITY = 35.0          # g/L (Archean Ocean salt content)
VISCOSITY_H2O = 0.00089  # Pa·s (Dynamic viscosity of water at 25°C)
PH = 8.1                 # Archean pH balance
PHI = 1.61803398875      # Unified Fractal Constant

# Simulation Parameters
CYCLES = 500000
NUCLEOTIDES = ['A', 'C', 'G', 'U']

def load_space_cargo(filename="saturn_genesis_results.fasta"):
    """
    Loads the 'Input Library' from space/gas giant simulations.
    """
    seeds = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                if not line.startswith(">") and line.strip():
                    seeds.append(line.strip())
    except FileNotFoundError:
        print("⚠️ Space Seed file not found. Initializing with singular pairs.")
        seeds = ["".join(random.choices(NUCLEOTIDES, k=2)) for _ in range(50)]
    return seeds

def calculate_terrestrial_stability(sequence):
    """
    The 'Earth Filter': Calculates survival based on Gravity, Magnetism, and Ions.
    """
    L = len(sequence)
    if L == 0: return False

    # 1. IONIC SHIELDING (Debye-Hückel approximation)
    # Sodium/Magnesium ions stabilize the negative phosphate backbone.
    ionic_strength = math.sqrt(SALINITY) / PHI
    bond_stability = (sequence.count('G') + sequence.count('C')) * 3
    bond_stability += (sequence.count('A') + sequence.count('U')) * 2
    shielded_stability = (bond_stability / L) * ionic_strength

    # 2. MAGNETOSPHERIC PROTECTION
    # Protects the sequence from UV/Cosmic radiation mutation.
    protection_factor = 1.0 - (1.0 / (B_FIELD * 1e6))

    # 3. GRAVITATIONAL SEDIMENTATION (Stoke's Law application)
    # Large chains 'sink' or 'clump' too fast if not balanced by viscosity.
    mol_weight = L * 330 # Average Dalton mass per nucleotide
    sedimentation_drag = (mol_weight * G_EARTH) / (6 * math.pi * VISCOSITY_H2O)
    drag_penalty = sedimentation_drag * 1e-15 # Scaled for molecular level

    # Final Earth Result
    terrestrial_index = (shielded_stability * protection_factor) - drag_penalty
    return terrestrial_index > 0.45 # Threshold for terrestrial viability

def run_earth_sim():
    print(f"🌍 Initializing EarthSim.py | Archean Ocean Model")
    print(f"Constants: G={G_EARTH} | B={B_FIELD}T | Salinity={SALINITY}g/L")

    soup = load_space_cargo()
    start_time = time.time()

    for cycle in range(CYCLES):
        if len(soup) < 2: break

        # Brownian Motion selection
        idx1, idx2 = random.sample(range(len(soup)), 2)
        s1, s2 = soup[idx1], soup[idx2]

        # Attempt concatenation
        candidate = s1 + s2

        if calculate_terrestrial_stability(candidate):
            if len(candidate) < 300: # Limit to realistic early gene size
                soup.append(candidate)
                # Population management
                if len(soup) > 600:
                    soup.sort(key=len, reverse=True)
                    soup.pop(random.randint(400, 599))

        if cycle % 100000 == 0:
            print(f"Cycle {cycle}: Complexity at {len(max(soup, key=len))} nodes...")

    end_time = time.time()
    print(f"✅ Earth Sim Complete in {round(end_time - start_time, 2)}s")
    return list(set(soup))

def export_to_fasta(data, filename="earth_terrestrial_results.fasta"):
    with open(filename, "w") as f:
        for i, seq in enumerate(data):
            if len(seq) >= 20: # Filtering for functional genomic units
                f.write(f">Earth_Genome_{i+1}_Nodes_{len(seq)}\n")
                f.write(f"{seq}\n")
    print(f"📁 Terrestrial Data Archived: {filename}")

if __name__ == "__main__":
    final_life = run_earth_sim()
    export_to_fasta(final_life)
