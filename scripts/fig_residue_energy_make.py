#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np, matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
E = np.load("Evals.npy"); xs, race = np.load("race_x.npy")
total = E.sum(); fault = (E[1]+E[5])/total
fig,(a,b)=plt.subplots(1,2,figsize=(13.5,5.2))
fig.suptitle("Residue-resolved von Mangoldt energy on the 6N skeleton "
             "(X=10^7): a check recovering classical facts",fontsize=12,fontweight="bold")
cols=["#9e9e9e","#1f4e79","#c0a000","#2e7d32","#c0a000","#b4341f"]
a.bar(range(6),[max(e,0.3) for e in E],color=cols,edgecolor="black")
a.set_yscale("log"); a.set_ylim(0.2,1e7)
labs=["0\n(6N)","1\n(6N+1)","2\n(2^k)","3\n(3^k)","4\n(2^k)","5\n(6N-1)"]
a.set_xticks(range(6)); a.set_xticklabels(labs)
a.set_xlabel("residue n mod 6"); a.set_ylabel("sum of Lambda(n) over n = r mod 6  (log)")
a.set_title(f"(A) energy on fault lines 6N+-1 = {100*fault:.4f}%")
for r in range(6):
    a.text(r, max(E[r],0.3)*1.5, (f"{E[r]:.0f}" if E[r]>100 else f"{E[r]:.1f}"),
           ha="center",fontsize=8)
b.semilogx(xs,race,color="#1f4e79",lw=1.3)
b.axhline(0,color="red",ls="--",lw=1)
b.set_xlabel("x"); b.set_ylabel("psi(x;6,5) - psi(x;6,1)")
b.set_title("(B) the 6N-1 vs 6N+1 race (prime squares p^2=1 mod6 tilt to r=1)")
b.grid(alpha=.3,which="both")
fig.tight_layout(rect=[0,0,1,0.94])
fig.savefig("fig_residue_energy.png",dpi=200); fig.savefig("fig_residue_energy.pdf")
print("wrote fig_residue_energy.{png,pdf}; fault fraction =",round(100*fault,4),"%")
