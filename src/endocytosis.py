import numpy as np
from scipy.integrate import solve_ivp
import sys
from pathlib import Path
sys.path.append(str(Path().resolve().parent))

from src.constants import *

def endocytosis_ode(
    t, y, ke, bound_complexes
):
    I = y[0]
    B = bound_complexes(t)

    dIdt = ke * B

    return [dIdt]

def run_endocytosis_model(binding_sol, duration):
    B_interp = lambda t: np.interp(
        t, binding_sol.t, binding_sol.y[0]
        )

    T_END = duration
    I0 = [0]

    t_span = (T_START, T_END)
    t_eval = binding_sol.t
    sol = solve_ivp(endocytosis_ode,
        t_span, I0,
        t_eval=t_eval,
        args=(KE, B_interp)
    )

    return sol


#def calc_internalisation(bound_complexes, ke, time):