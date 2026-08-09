"""
Ravewear Vision — See Designs, Analyze Aesthetics
==================================================
Photo-based design analysis and generation.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).parent.parent.parent / "mermicorn-commerce-ai" / "src"))
from commerce_ai.vision import MermicornVision, VisionResult


class RavewearVision:
    """
    Vision-powered design analysis.
    
    See a design → Analyze it → Improve it → Generate variations
    """
    
    def __init__(self, api_key: str | None = None):
        self.vision = MermicornVision(api_key=api_key)
    
    def analyze_design(self, image_path: str) -> VisionResult:
        """Analyze a rave wear design."""
        prompt = """Analyze this rave wear/fashion design.

Identify:
- Garment type (top, bottom, accessory)
- Colors and patterns
- Materials (estimated)
- Style category (rave, festival, club, streetwear)
- Design elements (cutouts, LED placement, UV-reactive areas)
- Target audience
- Price positioning

Provide JSON with:
- garment_type: {type, style, category}
- color_analysis: {primary, secondary, accent, hex_codes}
- materials_estimated: list
- design_elements: list
- aesthetic_rating: 1-10
- market_appeal: 1-10
- uv_compatibility: true/false
- led_compatibility: true/false
- improvement_suggestions: list
- similar_styles: list
- confidence: 0-1"""
        
        return self.vision.analyze_image(image_path, task="design")
    
    def compare_designs(self, image1_path: str, image2_path: str) -> VisionResult:
        """Compare two designs."""
        return self.vision.compare_images(image1_path, image2_path)
    
    def get_stats(self) -> dict[str, Any]:
        return {"vision_stats": self.vision.get_stats()}
