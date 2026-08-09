"""
Ravewear Studio — Platform Integration
========================================
Connects to Mermicorn central API.
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "mermicorn-client"))

from mermicorn_client import MermicornClient


def get_client() -> MermicornClient:
    return MermicornClient(
        api_url=os.environ.get("MERMICORN_API_URL", "http://localhost:8000"),
        api_key=os.environ.get("MERMICORN_API_KEY", ""),
    )


def sync_products(products: list[dict]) -> dict:
    """Sync ravewear products to central platform."""
    client = get_client()
    results = []
    for p in products:
        result = client.products.add(
            name=p["name"], price=p["price"],
            description=p.get("description", ""),
            tags=p.get("tags", ["rave", "festival"]),
        )
        results.append(result)
    return {"synced": len(results), "results": results}
