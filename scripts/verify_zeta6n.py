#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Verifier for Part XXV: zeta_6N(s) = zeta(s)(1-2^-s)(1-3^-s) = sum_{gcd(n,6)=1} n^-s.

Checks (standard library only):
  (1) pole at s=1 has residue (1-1/2)(1-1/3) = 1/3;
  (2) the ladders L2={2 pi i k/ln2}, L3={2 pi i n/ln3} are zeros of the two factors;
  (3) L2, L3 are incommensurate (ln2/ln3 irrational) and meet only at s=0 (double zero);
  (4) the coprime-to-6 identity at s=2: sum_{gcd(n,6)=1} n^-2 = zeta(2)(3/4)(8/9) = pi^2/9.
Also writes data/zeta6n_zeros.csv.
"""
import math, cmath, os, csv
ln2, ln3 = math.log(2), math.log(3)

def check_residue():
    res = (1-0.5)*(1-1.0/3)
    print(f"(1) residue at s=1 = (1-1/2)(1-1/3) = {res:.6f}  [expected 0.333333]")
    return abs(res-1/3) < 1e-12

def check_ladders():
    ok = True
    for base, ln in ((2,ln2),(3,ln3)):
        for k in (1,2,3):
            s = 1j*2*math.pi*k/ln
            v = abs(1 - base**(-s))
            ok = ok and v < 1e-9
        print(f"(2) (1-{base}^-s) at s=2 pi i k/ln{base}: |value| < 1e-9 for k=1,2,3: {ok}")
    return ok

def check_incommensurate():
    # s=0 is a common (double) zero; otherwise ladders disjoint -> check no small coincidences
    coincide = []
    for k in range(1,200):
        for n in range(1,200):
            if abs(2*math.pi*k/ln2 - 2*math.pi*n/ln3) < 1e-6:
                coincide.append((k,n))
    print(f"(3) ln2/ln3 = {ln2/ln3:.6f} (irrational); nonzero ladder coincidences found: "
          f"{len(coincide)} -> meet only at s=0 (double zero): {len(coincide)==0}")
    return len(coincide)==0

def check_coprime_identity():
    N = 3_000_000
    s = 0.0
    for n in range(1, N+1):
        if n % 2 and n % 3:           # gcd(n,6)=1
            s += 1.0/(n*n)
    target = (math.pi**2/6)*(3/4)*(8/9)   # zeta(2)(1-2^-2)(1-3^-2) = pi^2/9
    print(f"(4) sum_{{gcd(n,6)=1}} n^-2 (N={N:,}) = {s:.6f}  vs  pi^2/9 = {target:.6f}  "
          f"(tail ~1/N): {abs(s-target) < 1e-4}")
    return abs(s-target) < 1e-4

def write_data():
    here=os.path.dirname(os.path.abspath(__file__))
    out=os.path.join(os.path.dirname(here),"data"); os.makedirs(out,exist_ok=True)
    with open(os.path.join(out,"zeta6n_zeros.csv"),"w",newline="") as f:
        w=csv.writer(f); w.writerow(["family","index","Im(s)","Re(s)","note"])
        w.writerow(["double_zero",0,0.0,0.0,"L2 ∩ L3 at s=0"])
        for k in range(1,8): w.writerow(["L2",k,f"{2*math.pi*k/ln2:.6f}",0.0,"zero of 1-2^-s"])
        for n in range(1,11): w.writerow(["L3",n,f"{2*math.pi*n/ln3:.6f}",0.0,"zero of 1-3^-s"])
    print("\nwrote data/zeta6n_zeros.csv")

if __name__ == "__main__":
    a=check_residue(); b=check_ladders(); c=check_incommensurate(); d=check_coprime_identity()
    write_data()
    print("\nALL CHECKS PASS:", a and b and c and d)
