"""Módulo de configuración para el rastreador de criptomonedas."""

from typing import List


class Config:
    """Configuraciones predeterminadas de la aplicación."""
    DEFAULT_SYMBOL: str = "SOLUSDT"
    DEFAULT_SYMBOLS: List[str] = ["SOLUSDT", "ETHUSDT"]
    BASE_URL: str = "https://api.binance.com/api/v3/ticker/24hr"
    LOG_FILE: str = "prices.log"

# Diccionario alternativo para acceso flexible
CONFIG = {
    "default_symbol": Config.DEFAULT_SYMBOL,
    "default_symbols": Config.DEFAULT_SYMBOLS,
    "base_url": Config.BASE_URL,
    "log_file": Config.LOG_FILE,
}
