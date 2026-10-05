import sys
import json
import urllib.request

def get_exchange_and_crypto(crypto_symbol="BTC", fiat_currency="USD"):
    """
    Consume la API externa pública de CoinGecko/Binance para obtener la cotización
    de una criptomoneda expresada en la moneda fiat solicitada.
    """
    try:
        # API Externa no nativa de Google (CoinGecko Simple Price API)
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_symbol.lower()}&vs_currencies={fiat_currency.lower()}&include_24hr_change=true"
        
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            
        return {
            "status": "success",
            "crypto": crypto_symbol.upper(),
            "fiat": fiat_currency.upper(),
            "data": data.get(crypto_symbol.lower(), {})
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }

if __name__ == "__main__":
    # Manejo de argumentos CLI
    crypto = sys.argv[1] if len(sys.argv) > 1 else "bitcoin"
    fiat = sys.argv[2] if len(sys.argv) > 2 else "usd"
    
    result = get_exchange_and_crypto(crypto, fiat)
    print(json.dumps(result, indent=2))
    