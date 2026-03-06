import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from math import comb

st.set_page_config(page_title="Coin Flip", page_icon="🪙", layout="wide")
st.title("🪙 Coin Flip")

num_flip = st.sidebar.slider("Number of coin flips:", min_value=1, max_value=10, value=5)
flip_type = st.sidebar.selectbox("Choose:", ["At least", "Precisely", "Less than"])
symbol = {"At least": r"\geq", "Precisely": "=", "Less than": "<"}
num_heads = st.sidebar.slider("Number of heads:", min_value=0, max_value=num_flip, value=min(5, num_flip))

prob = np.array([0.0] * (num_flip + 1))
for i in range(num_flip + 1):
    prob[i] = comb(num_flip, i) * 0.5 ** num_flip

if flip_type == "At least":
    result = sum(prob[num_heads:])
elif flip_type == "Precisely":
    result = prob[num_heads]
else:
    result = sum(prob[:num_heads])

st.sidebar.latex(f"P(X {symbol[flip_type]} {num_heads}) = {result:.5f}")

for i in range(num_flip + 1):
    st.sidebar.latex(f"P(X = {i}) = {prob[i]:.5f}")

fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(range(num_flip + 1), prob, color='#7C3AED', label='Probabilities')

if flip_type == "At least":
    ax.bar(range(num_heads, num_flip + 1), prob[num_heads:], color='#F59E0B', label='Selected Probability')
elif flip_type == "Precisely":
    ax.bar(num_heads, prob[num_heads], color='#F59E0B', label='Selected Probability')
else:
    ax.bar(range(num_heads), prob[:num_heads], color='#F59E0B', label='Selected Probability')

ax.set_xlabel('Number of Heads')
ax.set_ylabel('Probability')
ax.set_title('Coin Flip Probability Distribution')
ax.legend()
fig.patch.set_facecolor('#0F0F1A')
ax.set_facecolor('#1A1A2E')
ax.tick_params(colors='#E2E8F0')
ax.xaxis.label.set_color('#E2E8F0')
ax.yaxis.label.set_color('#E2E8F0')
ax.title.set_color('#E2E8F0')
st.pyplot(fig)
