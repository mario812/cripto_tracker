"""Punto de entrada principal para consultar y registrar cotizaciones de criptomonedas."""

from datetime import datetime
from config import Config
from fetcher import get_crypto_data


def log_price_record(log_path: str, symbol: str, price: float, change_percent: float) -> str:
    """Guarda una línea de registro con timestamp en el archivo especificado.

    Args:
        log_path: Ruta al archivo de log (ej. 'prices.log').
        symbol: Par de cotización (ej. 'BTCUSDT').
        price: Precio actual.
        change_percent: Variación porcentual en 24h.

    Returns:
        Línea de texto guardada sin el salto de línea.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sign = "+" if change_percent > 0 else ""
    log_line = f"[{timestamp}] {symbol} | Precio: ${price:,.2f} USDT | Cambio 24h: {sign}{change_percent:.2f}%\n"

    with open(log_path, mode="a", encoding="utf-8") as f:
        f.write(log_line)

    return log_line.strip()


def main() -> None:
    """Ejecuta la consulta para cada par configurado, muestra en consola y guarda los registros."""
    symbols = Config.DEFAULT_SYMBOLS

    print("=" * 52)
    print("             CRIPTO TRACKER - BINANCE")
    print("=" * 52)

    for symbol in symbols:
        try:
            data = get_crypto_data(symbol)
            pair = data["symbol"]
            last_price = float(data["lastPrice"])
            price_change = float(data["priceChangePercent"])

            sign = "+" if price_change > 0 else ""

            print(f" Par:            {pair}")
            print(f" Precio actual:  ${last_price:,.2f} USDT")
            print(f" Cambio 24h:     {sign}{price_change:.2f}%")

            saved_entry = log_price_record(
                Config.LOG_FILE,
                pair,
                last_price,
                price_change
            )
            print(f" [OK] Guardado:  {saved_entry}")
            print("-" * 52)

        except Exception as err:
            print(f" [ERROR] No se pudo procesar '{symbol}': {err}")
            print("-" * 52)


if __name__ == "__main__":
    main()
