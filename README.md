![CI Pipeline](https://github.com/tshepokotelo95-commits/hybrid-volatility-forecasting/actions/workflows/ci.yml/badge.svg)

# Hybrid Volatility Forecasting

[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Systematic risk architecture combining GARCH(1,1) and LSTM neural networks to map out-of-sample parametric Value-at-Risk (VaR) boundaries[span_0](start_span)[span_0](end_span).

---

## 🏛️ Institutional Audit & Quantitative Refactoring

This repository was systematically updated to transition the core forecasting pipeline from a basic machine learning script into an institutional-grade, production-ready risk management framework.

### 1. Elimination of Look-Ahead Bias (`model_main.py` -> `model_v2.py`)
* **Legacy Vulnerability:** The initial iteration calibrated the GARCH(1,1) parameters across the entire historical data sample before generating volatility inputs for the LSTM neural network, inadvertently leaking future variance structures into past data points.
* **Production Refactor:** Implemented a strict rolling-window calibration loop. The GARCH model is now re-calibrated dynamically at each time step using only historical information available up to that day, simulating an authentic live trading desk environment.

### 2. Hybrid Econometric & Neural Network Architecture
* **GARCH(1,1) Volatility Modeling:** Captures time-varying conditional volatility clustering and leverage effects in high-frequency financial return series.
* **LSTM Sequence Modeling:** Takes econometric volatility forecasts as dynamic features to capture non-linear temporal dependencies and tail-risk regimes.
* **Parametric Value-at-Risk (VaR):** Computes confidence-interval risk boundaries (e.g., 95% VaR) to quantify capital exposure under stressed market conditions.

---

## 📊 Backtest Analytics & Stress Testing

* **Vectorized Backtesting Engine (`src/backtest_engine.py`):** Evaluates strategy performance, tracking drawdowns, hit rates, and risk-adjusted return metrics.
* **Monte Carlo Stress Testing (`src/stress_test_simulation.py`):** Simulates thousands of price paths to stress-test portfolio resilience against extreme tail-risk shocks.
* **Master Pipeline Execution (`src/master_pipeline.py`):** Automates end-to-end data ingestion, feature engineering, hybrid model fitting, and risk dashboard generation.

---

## 🚀 Quickstart

```bash
# Clone repository
git clone [https://github.com/tshepokotelo95-commits/hybrid-volatility-forecasting.git](https://github.com/tshepokotelo95-commits/hybrid-volatility-forecasting.git)
cd hybrid-volatility-forecasting

# Install dependencies
pip install -r requirements.txt

# Run master forecasting and backtest pipeline
python src/master_pipeline.py
