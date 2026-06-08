#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Figure for Part XXV: zero map of zeta_6N (structural ladders at beta=0 vs zeta
zeros at beta=1/2) and the log-periodic power-staircases the ladders encode."""
import math, numpy as np
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt

ln2, ln3 = math.log(2), math.log(3)
# first nontrivial zeta zero ordinates
gam = [14.134725,21.022040,25.010858,30.424876,32.935062,
       37.586178,40.918719,43.327073,48.005151,49.773832]

fig,(a,b)=plt.subplots(1,2,figsize=(13.5,5.6))
fig.suptitle(r"$\zeta_{6N}(s)=\zeta(s)(1-2^{-s})(1-3^{-s})$: structural ladders ($\beta=0$) "
             r"and $\zeta$ zeros ($\beta=\frac{1}{2}$)", fontsize=12.5, fontweight="bold")

# Panel A: zero map
gmax=52
L2=[2*math.pi*k/ln2 for k in range(1,int(gmax*ln2/(2*math.pi))+1)]
L3=[2*math.pi*n/ln3 for n in range(1,int(gmax*ln3/(2*math.pi))+1)]
a.scatter([0]*len(L2), L2, marker="s", s=55, c="#1f4e79", label=r"$L_2:\ 2\pi i k/\ln 2$ (spacing 9.06)")
a.scatter([0]*len(L3), L3, marker="^", s=55, c="#2e7d32", label=r"$L_3:\ 2\pi i n/\ln 3$ (spacing 5.72)")
a.scatter([0],[0], marker="o", s=90, facecolors="none", edgecolors="k", label="double zero at $s=0$")
a.scatter([0.5]*len(gam), gam, marker="x", s=55, c="#b4341f", label=r"$\zeta$ zeros $\frac{1}{2}+i\gamma$")
a.scatter([1],[0], marker="*", s=160, c="orange", edgecolors="k", label="pole $s=1$ (res $1/3$)")
a.axvline(0, color="#1f4e79", lw=.6, ls=":"); a.axvline(0.5, color="#b4341f", lw=.6, ls=":")
a.set_xlim(-0.25,1.15); a.set_ylim(0,gmax)
a.set_xlabel(r"$\beta=\mathrm{Re}(s)$"); a.set_ylabel(r"$\gamma=\mathrm{Im}(s)$")
a.set_title("(A) zero map (upper half-plane)")
a.legend(fontsize=7.5, loc="upper right"); a.grid(alpha=.25)

# Panel B: the log-periodic power staircases that the ladders Fourier-encode
xx=np.logspace(0.05, 3, 2000)
psi2=np.array([ln2*math.floor(math.log(x,2)) for x in xx])
psi3=np.array([ln3*math.floor(math.log(x,3)) for x in xx])
b.semilogx(xx, psi2, color="#1f4e79", lw=1.6, label=r"$\psi_2(x)=\ln2\,\lfloor\log_2 x\rfloor$ (period $\ln2$)")
b.semilogx(xx, psi3, color="#2e7d32", lw=1.6, label=r"$\psi_3(x)=\ln3\,\lfloor\log_3 x\rfloor$ (period $\ln3$)")
b.set_xlabel("$x$"); b.set_ylabel("removed power-staircase")
b.set_title(r"(B) the 2- and 3-power staircases stripped from $\psi$; "+"\n"+r"their Fourier modes $=L_2,L_3$")
b.legend(fontsize=8, loc="upper left"); b.grid(alpha=.3, which="both")
fig.tight_layout(rect=[0,0,1,0.93])
fig.savefig("fig_zeta6n.png", dpi=200); fig.savefig("fig_zeta6n.pdf")
print("wrote fig_zeta6n.{png,pdf}")
