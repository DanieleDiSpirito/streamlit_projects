import streamlit as st
import matplotlib.pyplot as plt
import random
import time

st.set_page_config(page_title="Random Stock Trend", page_icon="📉", layout="wide")
st.title("📉 Random Stock Trend Simulation")

def random_stock_trend(starting_point, loops, max_variance):
    values = [0.0] * loops
    values[0] = starting_point
    for idx in range(1, loops):
        values[idx] = (1 + (random.random() - 0.5) * max_variance * 2) * values[idx - 1]
    return values

starting_point = st.number_input("Starting Point", value=100, min_value=0)
loops = st.number_input("Number of Loops", value=1000, min_value=1)
max_variance = st.number_input("Max Variance", value=0.05, min_value=0.01, max_value=1.0, step=0.01)

if st.button("▶ Generate Trend"):
    with st.spinner("Generating trend..."):
        time.sleep(1)
        values = random_stock_trend(starting_point, loops, max_variance)
        st.success("Trend generated!")

    st.sidebar.header("Trend Statistics")
    st.sidebar.write(f"**Starting point:** {starting_point}")
    st.sidebar.write(f"**Final value:** {values[-1]:.2f}")
    trend_pct = 100 * (values[-1] - starting_point) / starting_point
    color = "🟢" if trend_pct >= 0 else "🔴"
    st.sidebar.write(f"**Trend:** {color} {trend_pct:.2f}%")
    st.sidebar.write(f"**Average value:** {sum(values) / len(values):.2f}")
    st.sidebar.write(f"**Max value:** {max(values):.2f}")
    st.sidebar.write(f"**Min value:** {min(values):.2f}")
    st.sidebar.write(f"**Range:** {max(values) - min(values):.2f}")

    fig, ax = plt.subplots(figsize=(10, 6))
    line_color = '#10B981' if values[-1] >= starting_point else '#EF4444'
    ax.plot(values, color=line_color, linewidth=1.2)
    ax.axhline(y=starting_point, color='#F59E0B', linestyle='--', linewidth=1, alpha=0.7, label='Starting Point')
    ax.set_xlabel('Time')
    ax.set_ylabel('Value')
    ax.set_title('Random Stock Trend')
    ax.legend()
    fig.patch.set_facecolor('#0F0F1A')
    ax.set_facecolor('#1A1A2E')
    ax.tick_params(colors='#E2E8F0')
    ax.xaxis.label.set_color('#E2E8F0')
    ax.yaxis.label.set_color('#E2E8F0')
    ax.title.set_color('#E2E8F0')
    st.pyplot(fig)
