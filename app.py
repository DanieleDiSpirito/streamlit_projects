import streamlit as st

st.set_page_config(
    page_title="Math & Simulation Lab",
    page_icon="🔬",
    layout="wide",
)

st.title("🔬 Math & Simulation Lab")
st.markdown("### A collection of interactive mathematical tools and simulations")
st.divider()

col1, col2 = st.columns(2)

with col1:
    st.page_link("pages/01_🪙_Coin_Flip.py", label="**🪙 Coin Flip**")
    st.markdown(
        "Explore **binomial probability distributions**. "
        "Calculate the probability of getting a certain number of heads "
        "in _n_ coin flips with interactive visualizations."
    )
    st.markdown("**Topics:** Probability, Combinatorics, Binomial Distribution")

with col2:
    st.page_link("pages/03_🎯_Monte_Carlo_Pi.py", label="**🎯 Monte Carlo — π Estimation**")
    st.markdown(
        "Estimate **π** using the Monte Carlo method with uniform or "
        "Gaussian distributions. Also derives an estimate of _e_ "
        "from the Gaussian simulation."
    )
    st.markdown("**Topics:** Monte Carlo, Numerical Methods, Probability")

st.markdown("<br>", unsafe_allow_html=True)

col3, col4 = st.columns(2)

with col3:
    st.page_link("pages/02_📈_Linear_Regression.py", label="**📈 Linear Regression**")
    st.markdown(
        "Visualize **linear regression** on randomly generated data. "
        "Explore covariance, variance, standard deviation, correlation "
        "and the coefficient of determination R²."
    )
    st.markdown("**Topics:** Statistics, Machine Learning, Regression")

with col4:
    st.page_link("pages/04_📉_Random_Stock_Trend.py", label="**📉 Random Stock Trend**")
    st.markdown(
        "Simulate a **random stock price trend** using a multiplicative "
        "random walk. Configure starting price, number of steps and "
        "maximum variance."
    )
    st.markdown("**Topics:** Finance, Stochastic Processes, Simulation")

st.markdown("<br>", unsafe_allow_html=True)

col5, col6 = st.columns(2)

with col5:
    st.page_link("pages/05_🏔️_Gradient_Descent.py", label="**🏔️ Gradient Descent**")
    st.markdown(
        "Visualize **Gradient Descent** moving down the Mean Squared Error (MSE) "
        "loss landscape with an interactive contour plot and learning steps."
    )
    st.markdown("**Topics:** Machine Learning, Optimization, Calculus")

st.divider()
st.markdown(
    "<p style='text-align:center; color: #666;'>Navigate using the sidebar ← to explore each tool</p>",
    unsafe_allow_html=True,
)
