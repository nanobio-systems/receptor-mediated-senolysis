import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import sys
from pathlib import Path
sys.path.append(str(Path().resolve().parent))

from src.constants import *

def binding_ode_1(t, y, kon, koff, n, r):
    B = y[0]

    dBdt = kon * n * r - koff * B

    return [dBdt]

def binding_ode_2(t, y, kon, koff, n, r):
    B = y[0]

    dBdt = kon * n * (r - B) - koff * B

    return [dBdt]

def run_binding_model_1(receptor_density, duration):

    B0 = [0]
    T_END = duration

    t_span = (T_START, T_END)

    t_eval = np.linspace(
        T_START,
        T_END,
        500
    )

    sol = solve_ivp(
        binding_ode_1,
        t_span,
        B0,
        t_eval=t_eval,
        args=(
            KON,
            KOFF,
            NP_CONC,
            receptor_density,
        )
    )

    return sol

def run_binding_model_2(receptor_density, duration):

    B0 = [0]
    T_END = duration

    t_span = (T_START, T_END)

    t_eval = np.linspace(
        T_START,
        T_END,
        500
    )

    sol = solve_ivp(
        binding_ode_2,
        t_span,
        B0,
        t_eval=t_eval,
        args=(
            KON,
            KOFF,
            NP_CONC,
            receptor_density,
        )
    )

    return sol
