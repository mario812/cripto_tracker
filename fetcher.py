"""Módulo para consultar datos de mercado de Binance usando urllib.request."""

import json
import urllib.error
import urllib.parse
import urllib.request
from typing import Any, Dict

from config import Config


def get_crypto_data(symbol: str = Config.DEFAULT_SYMBOL) -> Dict[str, Any]:
    """Consulta el endpoint de 24hr ticker de Binance para obtener precio y cambio de 24h.

    Args:
        symbol: Par de mercado a consultar (por ejemplo, 'BTCUSDT').

    Returns:
        Dict conteniendo:
            - 'symbol': Símbolo consultado
            - 'lastPrice': Último precio de cotización (str)
            - 'priceChangePercent': Porcentaje de cambio en 24 horas (str)
    """
    params = urllib.parse.urlencode({"symbol": symbol.upper()})
    url = f"{Config.BASE_URL}?{params}"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Python/urllib"
    }

    req = urllib.request.Request(url, headers=headers)

    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            payload = json.loads(response.read().decode("utf-8"))
            return {
                "symbol": payload.get("symbol", symbol.upper()),
                "lastPrice": payload.get("lastPrice"),
                "priceChangePercent": payload.get("priceChangePercent"),
            }
    except urllib.error.HTTPError as err:
        raise RuntimeError(f"Error HTTP {err.code} al consultar Binance: {err.reason}") from err
    except urllib.error.URLError as err:
        raise RuntimeError(f"Error de conexión de red al consultar Binance: {err.reason}") from err
    except json.JSONDecodeError as err:
        raise RuntimeError("No se pudo parsear la respuesta JSON de Binance.") from err
