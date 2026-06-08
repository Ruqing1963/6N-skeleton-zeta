# Part XXV — The 6N-Skeleton Zeta Function and its Log-Periodic Zero-Ladders

*Volume III of the Arithmetic Geodynamics programme on the 6N skeleton.*

The 6N skeleton is built by stripping the primes 2 and 3, so every surviving prime
sits on a fault line 6N±1. This paper makes that stripping explicit at the level of
the zeta function:

> ζ_6N(s) := ζ(s)(1−2⁻ˢ)(1−3⁻ˢ) = ∏_{p≥5}(1−p⁻ˢ)⁻¹ = Σ_{gcd(n,6)=1} n⁻ˢ,

the Dirichlet series of the integers coprime to 6.

### Analytic structure

- **Pole:** simple, at s=1, residue (1−½)(1−⅓) = **1/3** (the density φ(6)/6).
- **Zeros split into two orthogonal families:**
  - the nontrivial zeros of ζ on the critical line **β = ½** (unchanged);
  - two **new ladders on the imaginary axis β = 0**:
    `L₂ = {2πik/ln2}` (spacing 9.0647) and `L₃ = {2πin/ln3}` (spacing 5.7192).
  - Since ln2/ln3 is irrational, L₂ and L₃ are **incommensurate**, meeting only at
    the **double zero s = 0**.
- **The ladders are Fourier modes of removed staircases.** L₂, L₃ are exactly the
  frequencies of the log-periodic staircases ψ₂, ψ₃ counting the powers of 2 and 3
  stripped from ψ. The skeleton count splits cleanly:
  `ψ_6N(x) = x − Σ_ρ xᵖ/ρ − (ψ₂+ψ₃) + …` — smooth term, fluctuating β=½ part, and a
  rigid log-periodic β=0 grid.

### Motivation (a check, not a new result)

At X=10⁷, **99.9997%** of the von Mangoldt energy sits on the fault lines 6N±1 —
the prime number theorem in arithmetic progressions mod 6, with the √x-scale 5-vs-1
race. Classical; used only to justify keeping the p≥5 factors.

## Layout

```
.
├── paper/    Chen_6N_Paper25.{tex,pdf} + figures
├── figures/  fig_zeta6n.{pdf,png} · fig_residue_energy.{pdf,png}
├── data/     zeta6n_zeros.csv · residue_energy.csv
├── code/
│   ├── fig_zeta6n_make.py         # zero map + log-periodic staircases
│   ├── fig_residue_energy_make.py # residue-energy + 5-vs-1 race figure
│   ├── exp_residue_energy.py      # the X=10^7 von Mangoldt experiment (writes .npy)
│   └── verify_zeta6n.py           # pole residue, ladders, incommensurability, coprime-6 identity
├── CITATION.cff · .zenodo.json · LICENSE (MIT)
```

## Reproducing

```bash
pip install numpy matplotlib
python code/verify_zeta6n.py        # all checks pass; writes data/zeta6n_zeros.csv
python code/exp_residue_energy.py   # regenerates Evals.npy / race_x.npy (sieve to 10^7)
python code/fig_zeta6n_make.py      # zero-map + staircase figure
python code/fig_residue_energy_make.py
```

Expected: residue at s=1 is 1/3; L₂,L₃ are zeros on β=0; ln2/ln3 irrational (meet
only at s=0); Σ_{gcd(n,6)=1} n⁻² = π²/9; fault-line energy 99.9997%.

## Scope

An elementary modification of ζ. The new zeros are a construction artifact of
removing two Euler factors — not discoveries — and nothing here bears on the Riemann
Hypothesis or the infinitude of any prime constellation. Continues Part XXIV
(doi:10.5281/zenodo.20587185).

## License

MIT — see `LICENSE`.
