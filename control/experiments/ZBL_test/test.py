# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 12:02:56 2017

@author: lab
"""
import matplotlib as mpl
mpl.use("Agg")
import irc
import Thorlabs

import numpy as np
import time as t

chat = irc.irc("ZBL_test")

pm = Thorlabs.PM100D()
pm.wavelength(wavelength=1550)

P = np.linspace(100, 5000, 50)

print("Turning on laser")
chat.write(">EDFA SMODE PC")

p_Ts = []
p_Ts_std = []

t.sleep(2)

for power in P:
    print("\nP = {:.3f} mW".format(power))
    M = ">EDFA SPC {:.3f}".format(np.log10(power)*10)
    print(M)
    chat.write(M)
    t.sleep(8)
    p_T, p_T_std = [n * 1000 for n in pm.power(N=100)]
    print("p_T = {:.3f} +/- {:.5f} mW".format(p_T, p_T_std))
    p_Ts.append(p_T)
    p_Ts_std.append(p_T_std)
    t.sleep(8)
        
print("Turning off laser")
chat.write(">EDFA SMODE OFF")

P *= 0.964
 
F = np.polyfit(P, p_Ts, 1, w=1/np.array(p_Ts_std))
print("F: {}".format(F))
m = F[0]
c = F[1]
from scipy.optimize import curve_fit
def f(x, m, c):
    return m*x+c
popt, pcov = curve_fit(f, P, p_Ts, p0 = F, sigma=p_Ts_std)
print("popt: {}\npcov: {}".format(popt, pcov))   

m,c = popt
sig_m, sig_c = np.sqrt(pcov.diagonal())
print([sig_m, sig_c])

import pylab as pl

np.savetxt("data.txt", np.array([P,p_Ts]))
d = np.array([np.min(P), np.max(P)])
pl.plot(d, m*d+c, "--", linewidth = 2, color="black", label="Linear fit (m={:.3f} $\pm$ {:1.2e})".format(m,sig_m**2))

pl.errorbar(P, p_Ts, xerr = 0.8, fmt=".", yerr=p_Ts_std, color="black")
pl.plot(P, p_Ts, "ro", label="Experimental data")


pl.xlabel("$P_{\mathrm{in}}\ [\mathrm{mW}]$")
pl.ylabel("$P_{\mathrm{T}}\ [\mathrm{mW}]$")
pl.title("ZBL transmission ($L=5\pm0.1$, $\lambda=1550\ \mathrm{nm}$)")
pl.grid(True)

pl.xlim(0,5050)
pl.ylim(0,5050)
pl.legend()
pl.annotate('$m = {} \pm {}$'.format(m, sig_m**2),
            xy=(3000, 1000), xycoords='figure points')
pl.tight_layout()
pl.savefig("plot.png")
pl.savefig("plot.pdf")
