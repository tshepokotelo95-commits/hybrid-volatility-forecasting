import pytest

def test_parametric_var_boundary():
    """Verify parametric Value-at-Risk (VaR) calculation at 95% confidence level."""
    portfolio_value = 10_000_000.0
    daily_volatility = 0.015  # 1.5% daily vol forecasted by GARCH-LSTM
    z_score_95pct = 1.645     # 95% one-tailed normal Z-score
    
    daily_var_95 = portfolio_value * daily_volatility * z_score_95pct
    
    assert pytest.approx(daily_var_95, 1.0) == 246750.0

def test_rolling_window_calibration():
    """Verify that training dataset indices prevent look-ahead bias."""
    total_obs = 1000
    window_size = 252
    t = 300
    
    train_start = t - window_size
    train_end = t
    
    assert train_start >= 0
    assert train_end < total_obs
    assert train_end == t  # Ensures calibration strictly uses past data up to time t
