# 🔬 Math & Simulation Lab

A collection of interactive mathematical tools and simulations built with [Streamlit](https://streamlit.io/). This application provides intuitive visualizations to explore concepts in probability, statistics, numerical methods, finance, and machine learning.

---

## 🌟 Features & Tools

1. **🪙 Coin Flip**
   - Explore **binomial probability distributions**. 
   - Calculate and visualize the probability of getting a certain number of heads in *n* coin flips.
   - **Topics**: Probability, Combinatorics, Binomial Distribution

2. **📈 Linear Regression**
   - Visualize **linear regression** on randomly generated data. 
   - Explore covariance, variance, standard deviation, correlation, and the coefficient of determination (R²).
   - **Topics**: Statistics, Machine Learning, Regression

3. **🎯 Monte Carlo — π Estimation**
   - Estimate the value of **π** using the Monte Carlo method with uniform or Gaussian distributions. 
   - Derives an estimate of *e* from the Gaussian simulation.
   - **Topics**: Monte Carlo, Numerical Methods, Probability

4. **📉 Random Stock Trend**
   - Simulate a **random stock price trend** using a multiplicative random walk. 
   - Configure parameters such as starting price, number of steps, and maximum variance.
   - **Topics**: Finance, Stochastic Processes, Simulation

5. **🏔️ Gradient Descent**
   - Visualize **Gradient Descent** step-by-step as it moves down the Mean Squared Error (MSE) loss landscape.
   - Includes an interactive contour plot and customizable learning steps.
   - **Topics**: Machine Learning, Optimization, Calculus

---

## 🚀 Getting Started

### Prerequisites

Ensure you have Python installed. The required libraries are listed in `requirements.txt`:
- `streamlit>=1.28.0`
- `numpy>=1.24.0`
- `pandas>=2.0.0`
- `matplotlib>=3.7.0`
- `scikit-learn>=1.3.0`

### Installation

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd streamlit_projects
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit application:
   ```bash
   streamlit run Homepage.py
   ```

## 🛠️ Technology Stack

- **Framework**: Streamlit
- **Data & Math**: NumPy, Pandas
- **Machine Learning**: scikit-learn
- **Visualization**: Matplotlib

## 📝 License

This project is open-source. Feel free to explore, learn, and contribute!
