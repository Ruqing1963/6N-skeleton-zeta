#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Residue-resolved von Mangoldt energy on the 6N skeleton + the 5-vs-1 race."""
import math, numpy as np

X = 10_000_000
# sieve primes up to X
sieve = bytearray([1])*(X+1); sieve[0]=sieve[1]=0
for i in range(2,int(X**0.5)+1):
    if sieve[i]:
        sieve[i*i::i] = bytearray(len(sieve[i*i::i]))
primes = [i for i in range(2,X+1) if sieve[i]]

# prime powers p^k <= X, weight ln p, residue mod 6
E = {r:0.0 for r in range(6)}      # Lambda-energy by residue
pk_list = []                        # (n, lnp, residue) for the race
for p in primes:
    lp = math.log(p); n = p
    while n <= X:
        r = n % 6
        E[r] += lp
        pk_list.append((n, lp, r))
        n *= p
total = sum(E.values())
print(f"X = {X:,}   total Lambda-energy sum_{{n<=X}} Lambda(n) = psi(X) = {total:,.1f}  (~X={X:,})")
print("residue r mod 6 :   Lambda-energy E_r     share")
for r in range(6):
    print(f"   r={r} : {E[r]:16,.1f}   {100*E[r]/total:6.3f}%")
fault = (E[1]+E[5])/total
print(f"\nfault-line fraction (r in {{1,5}} = 6N+-1): {100*fault:.4f}%   "
      f"off-skeleton (r in {{2,3,4}}): {100*(1-fault):.4f}%, r=0: {E[0]}")
print(f"E_1/E_5 = {E[1]/E[5]:.6f}  (PNT in AP predicts ->1; deficit = Chebyshev bias toward 5)")

# 5-vs-1 race: psi(x;6,5) - psi(x;6,1) on a log grid
pk_list.sort()
ns = np.array([n for n,_,_ in pk_list])
sgn = np.array([(1.0 if r==5 else (-1.0 if r==1 else 0.0)) for _,_,r in pk_list])
w  = np.array([lp for _,lp,_ in pk_list])
race = np.cumsum(sgn*w)
xs = np.logspace(1, math.log10(X), 400)
idx = np.searchsorted(ns, xs, side="right")-1; idx[idx<0]=0
race_x = race[idx]
frac_pos = float(np.mean(race[ns>=100] > 0))
print(f"\n5-vs-1 race psi(x;6,5)-psi(x;6,1): fraction of x>=100 with lead to 5 = {100*frac_pos:.1f}%")
np.save("race_x.npy", np.vstack([xs, race_x]))
np.save("Evals.npy", np.array([E[r] for r in range(6)]))
print("saved race_x.npy, Evals.npy")
