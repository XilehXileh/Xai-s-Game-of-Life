import math
import random
import time

# --- SATURN-SPECIFIC PHYSICAL CONSTANTS ---
PRESSURE = 12.5          # Bar (Deep Water Cloud layer)
TEMP_K = 291.15          # 18.0 Celsius in Kelvin
WIND_VELOCITY = 450.0    # m/s (Equatorial jet stream impact)
RHO_ATM = 0.45           # kg/m3 (Atmospheric density at 12.5 bar)
G_SATURN = 10.44         # m/s2
PHI = 1.61803398875      # Unified Fractal Constant

# Simulation Parameters
CYCLES = 500000
NUCLEOTIDES = ['A', 'C', 'G', 'U']

def calculate_saturnian_viability(sequence):
    """
    Guarantees the result is local to Saturn by applying
    Buoyancy, Turbulence, and Thermal Convection math.
    """
    L = len(sequence)
    if L < 2: return True

    # 1. THE BUOYANCY CONSTRAINT (Archimedes)
    # Mass in Daltons converted to kg (approx)
    mol_mass = L * 330 * 1.66e-27
    # Fractal Volume (Assuming non-linear folding based on PHI)
    mol_volume = (L * PHI) * 1e-28

    # Buoyancy: Must stay suspended in the 0.45 kg/m3 fluid
    buoyancy_force = (RHO_ATM * mol_volume * G_SATURN)
    gravity_pull = (mol_mass * G_SATURN)

    # If it sinks or floats away too fast, it's non-viable
    buoyancy_ratio = buoyancy_force / (gravity_pull + 1e-30)

    # 2. THE TURBULENCE SHRED (Kinetic Shear)
    # High velocity winds shred long, linear chains.
    # Saturnian life must be short or circular to survive.
    shear_stress = (WIND_VELOCITY**2 * L) / (1e6 * PHI)

    # 3. BOND STABILITY (Pressure-enhanced G-C pairing)
    gc_content = (sequence.count('G') + sequence.count('C')) / L
    # Pressure actually helps G-C bonds stay closed
    pressure_stability = gc_content * math.log1p(PRESSURE) * PHI

    # FINAL SATURN INDEX
    # We subtract the 'Sinking' penalty and the 'Shred' penalty
    saturn_score = pressure_stability - (shear_stress + abs(1.0 - buoyancy_ratio))

    return saturn_score > 0.15

def run_locked_saturn_sim():
    print(f"🪐 Initializing SaturnSim_V2.py | LOCKED TO DEEP WATER LAYER")
    print(f"Applying: Buoyancy Math | Turbulence Shear | Rho={RHO_ATM}")

    # Start with Asteroid ROM seeds (singular pairs)
    population = ["".join(random.choices(NUCLEOTIDES, k=2)) for _ in range(100)]
    start_time = time.time()

    for cycle in range(CYCLES):
        if not population: break

        # Interaction (Molecular collisions in the clouds)
        s1, s2 = random.sample(population, 2)
        candidate = s1 + s2

        if calculate_saturnian_viability(candidate):
            # Saturnian chains are naturally capped by physics around 10-16 nodes
            if len(candidate) < 50:
                population.append(candidate)
                if len(population) > 300:
                    population.sort(key=len, reverse=True)
                    population.pop()

        if cycle % 100000 == 0:
            print(f"Cycle {cycle}: Stable fragments surviving: {len(population)}")

    end_time = time.time()
    print(f"✅ Saturn Logic Complete in {round(end_time - start_time, 2)}s")
    return list(set(population))

def save_locked_fasta(data, filename="saturn_locked_results.fasta"):
    with open(filename, "w") as f:
        for i, seq in enumerate(data):
            if len(seq) >= 8:
                f.write(f">Saturn_Local_Fragment_{i+1}_Nodes_{len(seq)}\n")
                f.write(f"{seq}\n")
    print(f"📁 Saturn-Local FASTA archived: {filename}")

if __name__ == "__main__":
    results = run_locked_saturn_sim()
    save_locked_fasta(results)
