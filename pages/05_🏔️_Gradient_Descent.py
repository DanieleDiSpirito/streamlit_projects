import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

st.set_page_config(page_title="Gradient Descent", page_icon="🏔️", layout="wide")
st.title("🏔️ Gradient Descent in Linear Regression")
st.markdown("Visualize how Gradient Descent finds the optimal parameters (slope and intercept) for a linear regression model by moving down the Mean Squared Error (MSE) loss landscape.")

# Generate random linear data
np.random.seed(42)  # For consistent dataset
X = 2 * np.random.rand(100)
y = 4 + 3 * X + np.random.randn(100)

# Function to compute MSE
def compute_mse(m, b, X, y):
    predictions = m * X + b
    return np.mean((predictions - y) ** 2)

# Grid for contour plot
m_vals = np.linspace(0, 6, 50)
b_vals = np.linspace(0, 8, 50)
M, B = np.meshgrid(m_vals, b_vals)
Z = np.zeros_like(M)
for i in range(50):
    for j in range(50):
        Z[i, j] = compute_mse(M[i, j], B[i, j], X, y)

# Sidebar settings
st.sidebar.header("Hyperparameters")
learning_rate = st.sidebar.number_input("Learning Rate (α)", min_value=0.01, max_value=0.5, value=0.1, step=0.01)
max_steps = st.sidebar.number_input("Max Steps", min_value=10, max_value=100, value=20, step=5)
run_button = st.sidebar.button("↻ Restart Simulation")

# Gradient Descent loop
m_current, b_current = 0.0, 0.0
m_history, b_history, loss_history = [m_current], [b_current], [compute_mse(m_current, b_current, X, y)]

for _ in range(max_steps):
    # Compute gradients
    predictions = m_current * X + b_current
    error = predictions - y
    m_grad = 2 * np.mean(error * X)
    b_grad = 2 * np.mean(error)
    
    # Update parameters
    m_current -= learning_rate * m_grad
    b_current -= learning_rate * b_grad
    
    m_history.append(m_current)
    b_history.append(b_current)
    loss_history.append(compute_mse(m_current, b_current, X, y))

# Autoplay state logic
if 'step' not in st.session_state:
    st.session_state.step = 0
if 'playing' not in st.session_state:
    st.session_state.playing = False

# Function to update step from slider
def update_step():
    st.session_state.step = st.session_state.slider_step

col_play, col_slider = st.columns([1, 5])
with col_play:
    if st.session_state.playing:
        if st.button("⏸ Pause"):
            st.session_state.playing = False
            st.rerun()
    else:
        if st.button("▶ Play"):
            st.session_state.playing = True
            if st.session_state.step >= max_steps:
                st.session_state.step = 0
            st.rerun()

with col_slider:
    step = st.slider("Gradient Descent Step", min_value=0, max_value=max_steps, value=st.session_state.step, key='slider_step', on_change=update_step, label_visibility="collapsed")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### Loss Function Contour")
    fig1, ax1 = plt.subplots(figsize=(6, 5))
    
    # Contour plot
    cp = ax1.contourf(M, B, Z, levels=np.logspace(-0.1, 1.7, 25), cmap='viridis', alpha=0.9)
    colorbar = fig1.colorbar(cp, ax=ax1, label="Mean Squared Error")
    colorbar.ax.yaxis.label.set_color('#E2E8F0')
    colorbar.ax.tick_params(colors='#E2E8F0')

    
    # Plot the path up to the current step
    ax1.plot(m_history[:step+1], b_history[:step+1], color='red', marker='o', markersize=4, linestyle='-', linewidth=2, label='GD Path')
    ax1.scatter(3.0, 4.0, color='white', marker='*', s=200, label='True Minimum', edgecolors='black', zorder=5) # True parameters
    
    ax1.set_xlabel("Slope (m)", color='#E2E8F0')
    ax1.set_ylabel("Intercept (b)", color='#E2E8F0')
    ax1.legend()
    fig1.patch.set_facecolor('#0F0F1A')
    ax1.set_facecolor('#1A1A2E')
    ax1.tick_params(colors='#E2E8F0')
    ax1.xaxis.label.set_color('#E2E8F0')
    ax1.yaxis.label.set_color('#E2E8F0')
    ax1.title.set_color('#E2E8F0')
    st.pyplot(fig1)

with col2:
    st.markdown("### Linear Regression Fit")
    fig2, ax2 = plt.subplots(figsize=(6, 5))
    ax2.scatter(X, y, color='#7C3AED', alpha=0.6, label='Data points')
    
    # Plot current regression line
    m_step = m_history[step]
    b_step = b_history[step]
    X_line = np.array([0, 2])
    y_line = m_step * X_line + b_step
    
    ax2.plot(X_line, y_line, color='red', linewidth=3, label=f'Fit: y = {m_step:.2f}x + {b_step:.2f}')
    
    ax2.set_xlabel("X", color='#E2E8F0')
    ax2.set_ylabel("y", color='#E2E8F0')
    ax2.legend()
    fig2.patch.set_facecolor('#0F0F1A')
    ax2.set_facecolor('#1A1A2E')
    ax2.tick_params(colors='#E2E8F0')
    ax2.xaxis.label.set_color('#E2E8F0')
    ax2.yaxis.label.set_color('#E2E8F0')
    ax2.title.set_color('#E2E8F0')
    st.pyplot(fig2)

with col3:
    st.markdown("### MSE Loss over Steps")
    fig3, ax3 = plt.subplots(figsize=(6, 5))
    
    ax3.plot(range(step+1), loss_history[:step+1], color='#38BDF8', linewidth=2, marker='o', markersize=3, label='MSE Loss')
    ax3.set_xlim(0, max_steps)
    ax3.set_yscale('log')
    
    start_loss = max(1, loss_history[0]) if loss_history else 100
    min_loss = min(loss_history)
    ax3.set_ylim(max(1e-4, min_loss * 0.5), start_loss * 1.5)
    
    ax3.set_xlabel("Step / Iteration", color='#E2E8F0')
    ax3.set_ylabel("Mean Squared Error", color='#FFFFFF')
    ax3.legend()
    fig3.patch.set_facecolor('#0F0F1A')
    ax3.set_facecolor('#1A1A2E')
    ax3.tick_params(colors='#E2E8F0')
    ax3.xaxis.label.set_color('#E2E8F0')
    ax3.yaxis.label.set_color('#E2E8F0')
    ax3.title.set_color('#E2E8F0')
    st.pyplot(fig3)

st.markdown("---")
st.write(f"**Step {step}** — MSE Loss: `{loss_history[step]:.4f}` | $m = {m_history[step]:.4f}$ | $b = {b_history[step]:.4f}$")

# Autoplay loop
if st.session_state.playing:
    if st.session_state.step < max_steps:
        time.sleep(0.5)
        st.session_state.step += 1
        st.rerun()
    else:
        st.session_state.playing = False
