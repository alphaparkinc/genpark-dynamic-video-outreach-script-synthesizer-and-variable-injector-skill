# genpark-dynamic-video-outreach-script-synthesizer-and-variable-injector-skill

Dynamic multi-variable video outreach script generator with phoneme pacing and personalized token injection.

100% Python Standard Library implementation with zero external dependencies.

## Key Capabilities

- **Dynamic Personalized Script Templating**: Merges prospect and company metadata (`{{first_name}}`, `{{company}}`, `{{pain_point}}`) into outreach copy.
- **Natural Speech Cadence & Duration Estimator**: Calculates spoken duration (WPM) to ensure scripts fit optimal cold video lengths (< 45s).
- **Phonetic Pronunciation Overrides**: Attaches custom pronunciation hints for company names and specialized terms.

## Architecture

```
[Template Script + Dynamic Variables + Pronunciation Hints]
                             │
                             ▼
┌────────────────────────────────────────────────────────┐
│               VideoScriptSynthesizer                   │
│  - Multi-Token Replacement Engine                      │
│  - Words-Per-Minute Speech Duration Estimator          │
│  - Phonetic Override Mapping                           │
└────────────────────────────────────────────────────────┘
                             │
                             ▼
[Rendered Video Outreach Script with Duration & Pacing]
```

## MCP Server Integration

Run standard MCP stdio server:
```bash
python mcp_server.py
```

Exposed Tools:
- `synthesize_video_script`: Synthesizes personalized video outreach scripts, calculates speech duration, and injects pronunciation overrides.

## Quickstart (Python API)

```python
from client import VideoScriptSynthesizer

template = "Hi {{name}}, love what {{company}} is building!"
res = VideoScriptSynthesizer.synthesize_script(template, {"name": "Sara", "company": "Figma"})
print(res["rendered_script"], "Duration:", res["estimated_duration_seconds"], "s")
```

---

## GenPark Ecosystem

- **Official Website**: [https://www.genpark.ai](https://www.genpark.ai)
- **LinkedIn Page**: [https://www.linkedin.com/company/92955550](https://www.linkedin.com/company/92955550)
