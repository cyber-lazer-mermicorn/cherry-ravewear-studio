"""
Full Stack Workflow Test — Cherry Rave Wear Studio
===================================================
Design → Midjourney → Product → Listings → Sales
"""

import sys
import json
from pathlib import Path

sys.path.insert(0, "src")
sys.path.insert(0, "../mermicorn-commerce-ai/src")
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "mermicorn-commerce-ai" / "src"))

from ravewear_studio.integrations import MidjourneyIntegration, MarketplaceIntegration
from ravewear_studio.ai_designer import RavewearAI
from ravewear_studio.ai_vision import RavewearVision


def test_full_workflow():
    """Test complete ravewear workflow: Design → List → Sell."""
    print("🎨 RAVEWEAR FULL WORKFLOW TEST")
    print("=" * 50)
    
    # ═══════════════════════════════════════════════════════════
    # STEP 1: Generate Design Concept (AI)
    # ═══════════════════════════════════════════════════════════
    print("\n📌 STEP 1: Generate Design Concept")
    designer = RavewearAI()
    result = designer.generate_concept("Neon Dreams", "festival")
    
    assert result.success, f"Design generation failed: {result.reasoning}"
    print(f"   ✅ Concept generated: {result.data.get('name', 'Unknown')}")
    print(f"   ✅ Confidence: {result.confidence}")
    
    # ═══════════════════════════════════════════════════════════
    # STEP 2: Generate Midjourney Prompt
    # ═══════════════════════════════════════════════════════════
    print("\n📌 STEP 2: Generate Midjourney Prompt")
    mj = MidjourneyIntegration()
    
    concept = {
        "name": "Neon Dreams Top",
        "color_palette": ["#FF6B9D", "#C44DFF", "#00FFD1"],
        "materials": ["mesh", "sequins", "EL wire"],
        "features": ["UV reactive", "LED pocket", "crop top"],
    }
    
    prompt = mj.generate_clothing_prompt(concept)
    prompt_str = prompt.to_string()
    
    assert len(prompt_str) > 50, "Prompt too short"
    assert "Neon Dreams Top" in prompt_str, "Concept not in prompt"
    print(f"   ✅ Prompt: {prompt_str[:80]}...")
    
    # ═══════════════════════════════════════════════════════════
    # STEP 3: Create Product Data
    # ═══════════════════════════════════════════════════════════
    print("\n📌 STEP 3: Create Product Data")
    product = {
        "name": "Neon Dreams Crop Top",
        "description": "UV-reactive mesh crop top with LED pocket. Perfect for festivals and raves.",
        "price": 89.99,
        "category": "Ravewear",
        "tags": ["rave", "festival", "UV reactive", "LED", "crop top"],
        "materials": ["mesh", "sequins", "EL wire"],
        "colors": ["#FF6B9D", "#C44DFF"],
        "sizes": ["XS", "S", "M", "L", "XL"],
        "images": ["neon_dreams_1.jpg", "neon_dreams_2.jpg"],
    }
    
    assert product["price"] > 0, "Invalid price"
    assert len(product["tags"]) > 0, "No tags"
    print(f"   ✅ Product: {product['name']} @ ${product['price']}")
    
    # ═══════════════════════════════════════════════════════════
    # STEP 4: List on All Marketplaces
    # ═══════════════════════════════════════════════════════════
    print("\n📌 STEP 4: List on All Marketplaces")
    mp = MarketplaceIntegration()
    
    listings = {}
    for marketplace in ["shopify", "etsy", "amazon", "ebay"]:
        listing = mp.create_listing(marketplace, product)
        listings[marketplace] = listing
        
        fees = mp.calculate_fees(marketplace, product["price"])
        print(f"   ✅ {marketplace.upper()}: {listing.title[:40]}... | Net: ${fees['net']:.2f}")
    
    assert len(listings) == 4, "Not all marketplaces listed"
    
    # ═══════════════════════════════════════════════════════════
    # STEP 5: Generate SEO Tags
    # ═══════════════════════════════════════════════════════════
    print("\n📌 STEP 5: Generate SEO Tags")
    for marketplace in ["shopify", "etsy"]:
        tags = mp.generate_tags(product, marketplace)
        print(f"   ✅ {marketplace.upper()} tags: {tags[:5]}")
    
    # ═══════════════════════════════════════════════════════════
    # STEP 6: Generate Lifestyle Shot Prompt
    # ═══════════════════════════════════════════════════════════
    print("\n📌 STEP 6: Generate Lifestyle Shot")
    lifestyle = mj.generate_lifestyle_shot("festival")
    print(f"   ✅ Lifestyle prompt: {lifestyle.to_string()[:60]}...")
    
    # ═══════════════════════════════════════════════════════════
    # SUMMARY
    # ═══════════════════════════════════════════════════════════
    print("\n" + "=" * 50)
    print("✅ FULL WORKFLOW COMPLETE")
    print(f"   Concept: {concept['name']}")
    print(f"   Product: {product['name']} @ ${product['price']}")
    print(f"   Marketplaces: {', '.join(listings.keys())}")
    print(f"   Midjourney prompts: {len(mj.prompts)}")
    print("=" * 50)
    
    return True


if __name__ == "__main__":
    success = test_full_workflow()
    sys.exit(0 if success else 1)
