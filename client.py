class AiPresentationSlideNarrativeGeneratorClient:
    def generate_deck(self, topic: str, key_data_points: list = None, audience_type: str = "investors") -> dict:
        key_data_points = key_data_points or ["$4.2M ARR", "180% NRR", "3 enterprise logos"]
        slides = [
            {"slide": 1, "title": "The Problem", "content": "Manual processes cost mid-market ops teams $240K/yr in wasted hours.", "visual_spec": "Full-bleed pain illustration with stat overlay"},
            {"slide": 2, "title": "Our Solution", "content": f"{topic} — eliminating the bottleneck with AI-native automation.", "visual_spec": "Product screenshot with animated flow diagram"},
            {"slide": 3, "title": "Traction", "content": " | ".join(key_data_points), "visual_spec": "3-column metric cards with growth trend lines"},
            {"slide": 4, "title": "The Ask", "content": f"Raising $8M Series A to scale GTM for {audience_type}.", "visual_spec": "Clean use-of-funds pie chart"}
        ]
        notes = {f"Slide {s['slide']}": f"Emphasize: {s['content'][:60]}..." for s in slides}
        return {"slide_deck": slides, "speaker_notes": notes, "estimated_presentation_minutes": len(slides) * 3}
