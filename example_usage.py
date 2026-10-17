"""Example usage for Dynamic Video Outreach Script Synthesizer."""
from client import VideoScriptSynthesizer

if __name__ == "__main__":
    template = (
        "Hey {{first_name}}, noticed that {{company}} is rapidly expanding its AI platform. "
        "We built an autonomous agent layer that helps teams like {{company}} scale customer operations without adding headcount. "
        "Would love to show you a quick 2-minute workflow."
    )
    variables = {"first_name": "Marcus", "company": "Stripe"}
    hints = {"Stripe": "strahyp"}

    res = VideoScriptSynthesizer.synthesize_script(template, variables, hints)
    print("Script Preview:\n", res["rendered_script"])
    print(f"\nDuration: {res['estimated_duration_seconds']}s | Words: {res['word_count']} | Grade: {res['pacing_grade']}")
