from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(page_title="Linear Regression", page_icon="📈", layout="wide")
st.title("📈 Linear Regression")

num_points = st.sidebar.slider("Number of random points:", min_value=1, max_value=100, value=10)

x = np.random.rand(num_points, 1) * 100
y = 3 * x + np.random.randn(num_points, 1) * 50

reg = LinearRegression().fit(x, y)
a = reg.coef_[0][0]
b = reg.intercept_[0]

cov_xy = np.cov(x.flatten(), y.flatten())[0, 1]
s_x2 = np.var(x, ddof=1)
s_y2 = np.var(y, ddof=1)
s_x = np.sqrt(s_x2)
s_y = np.sqrt(s_y2)
rho = np.corrcoef(x.flatten(), y.flatten())[0, 1]
R2 = reg.score(x, y)

st.sidebar.latex(f"y = {a:.2f}x + {b:.2f}" if b > 0 else f"y = {a:.2f}x - {-b:.2f}")
st.sidebar.latex(f"\\text{{Covariance}}: cov_{{x,y}} = {cov_xy:.2f}")
st.sidebar.latex(f"\\text{{Variance}}: s_x^2 = {s_x2:.2f}")
st.sidebar.latex(f"\\text{{Variance}}: s_y^2 = {s_y2:.2f}")
st.sidebar.latex(f"\\text{{Standard Deviation}}: s_x = {s_x:.2f}")
st.sidebar.latex(f"\\text{{Standard Deviation}}: s_y = {s_y:.2f}")
st.sidebar.latex(f"\\text{{Correlation Index}}: \\rho = {rho:.2f}")
st.sidebar.latex(f"\\text{{Determination Index}}: R^2 = {R2:.2f}")

fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(x, y, color='#7C3AED', label='Random Points', alpha=0.8)
ax.plot(x, reg.predict(x), color='#F59E0B', linewidth=2, label='Regression Line')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Random Points and Linear Regression')
ax.legend()
fig.patch.set_facecolor('#0F0F1A')
ax.set_facecolor('#1A1A2E')
ax.tick_params(colors='#E2E8F0')
ax.xaxis.label.set_color('#E2E8F0')
ax.yaxis.label.set_color('#E2E8F0')
ax.title.set_color('#E2E8F0')
st.pyplot(fig)
