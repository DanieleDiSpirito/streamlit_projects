import streamlit as st
import random
from random import gauss
import matplotlib.pyplot as plt
from math import pi as PI, e as E

st.set_page_config(page_title="Monte Carlo — π", page_icon="🎯", layout="wide")
st.title("🎯 Monte Carlo Simulation for π Estimation")

def distance(P, Q):
    return ((P[0] - Q[0]) ** 2 + (P[1] - Q[1]) ** 2) ** 0.5

def estimate_pi(points, is_gauss=False):
    in_circle = 0
    for P in points:
        if distance(P, (0, 0)) < 1:
            in_circle += 1
    if is_gauss:
        return 8 * in_circle / len(points)
    return 4 * in_circle / len(points)

def estimate_e(estimated_pi):
    p = estimated_pi / 8
    e = (1 - p) ** (-2)
    return e

num_points = st.sidebar.number_input("Number of Points", min_value=100, max_value=100000, value=10000)
use_gaussian = st.checkbox("Use Gaussian Distribution")

if st.button("▶ Run Simulation"):
    if use_gaussian:
        points = [(gauss(0, 1), gauss(0, 1)) for _ in range(num_points)]
    else:
        points = [(2 * random.random() - 1, 2 * random.random() - 1) for _ in range(num_points)]

    estimated_pi = estimate_pi(points, use_gaussian)
    error = 100 * abs(estimated_pi - PI) / PI

    st.write(f"**Estimated π:** `{estimated_pi:.4f}` (ε = `{error:.4f}%`)")
    st.write(f"**True π:** `{PI:.8f}`")

    if use_gaussian:
        estimated_e = estimate_e(estimated_pi)
        error_e = 100 * abs(estimated_e - E) / E
        st.write(f"**Estimated e:** `{estimated_e:.4f}` (ε = `{error_e:.4f}%`)")
        st.write(f"**True e:** `{E:.8f}`")
        with st.expander("📖 See the math behind the $e$ estimation"):
            st.markdown("""
            When $X$ and $Y$ are independent standard normal random variables, the sum of their squares $R^2 = X^2 + Y^2$ follows an **Exponential distribution** with $\lambda = 1/2$ (also a Chi-squared distribution).
            
            The probability $p$ of a point falling inside the unit circle ($R^2 < 1$) is the cumulative distribution function (CDF) evaluated at 1:
            $$p = P(R^2 < 1) = 1 - e^{-1/2} = 1 - \\frac{1}{\\sqrt{e}}$$
            
            By estimating this probability $p$ via the Monte Carlo simulation, we can algebraically solve for $e$:
            $$\\frac{1}{\\sqrt{e}} = 1 - p \implies e = (1 - p)^{-2}$$

            More info here: [Pi Monte Carlo Simulation using Gaussian Distribution](https://github.com/DanieleDiSpirito/uni/blob/master/secondo_anno/statistica/Pi_Monte_Carlo_Simulation_using_Gaussian_Distribution.pdf)
            """)

    fig, ax = plt.subplots(figsize=(7, 7))
    ax.scatter([p[0] for p in points], [p[1] for p in points], s=0.5, color='#7C3AED', alpha=0.5)
    circle = plt.Circle((0, 0), 1, fill=False, color='#F59E0B', linewidth=2)
    ax.add_patch(circle)
    ax.set_aspect('equal')
    title = "Gaussian Distribution" if use_gaussian else "Monte Carlo Simulation for π Estimation"
    ax.set_title(title)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    fig.patch.set_facecolor('#0F0F1A')
    ax.set_facecolor('#1A1A2E')
    ax.tick_params(colors='#E2E8F0')
    ax.xaxis.label.set_color('#E2E8F0')
    ax.yaxis.label.set_color('#E2E8F0')
    ax.title.set_color('#E2E8F0')
    st.pyplot(fig)
