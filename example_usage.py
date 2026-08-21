from client import AiPresentationSlideNarrativeGeneratorClient

def main():
    client = AiPresentationSlideNarrativeGeneratorClient()
    res = client.generate_deck("Flowmatic AI", ["$4.2M ARR", "180% NRR", "Fortune 500 customer"], "Series A investors")
    print(f"Slides Generated: {len(res['slide_deck'])} | Est. Duration: {res['estimated_presentation_minutes']} min")
    for slide in res["slide_deck"]:
        print(f"  Slide {slide['slide']}: {slide['title']} — {slide['content'][:60]}")
    print("Speaker Notes:")
    for k, v in res["speaker_notes"].items():
        print(f"  {k}: {v}")

if __name__ == "__main__":
    main()
