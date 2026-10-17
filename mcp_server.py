"""MCP server for Dynamic Video Outreach Script Synthesizer."""
import sys
import json
from client import VideoScriptSynthesizer


def handle_request(req):
    method = req.get("method")
    if method == "tools/list":
        return {
            "tools": [
                {
                    "name": "synthesize_video_script",
                    "description": "Synthesizes personalized video outreach scripts, calculates speech duration, and injects pronunciation overrides",
                    "inputSchema": {
                        "type": "object",
                        "properties": {
                            "template": {"type": "string"},
                            "variables": {"type": "object"},
                            "pronunciation_hints": {"type": "object"},
                        },
                        "required": ["template", "variables"],
                    },
                }
            ]
        }
    elif method == "tools/call":
        params = req.get("params", {})
        tool_name = params.get("name")
        args = params.get("arguments", {})
        if tool_name == "synthesize_video_script":
            res = VideoScriptSynthesizer.synthesize_script(
                args.get("template", ""),
                args.get("variables", {}),
                pronunciation_hints=args.get("pronunciation_hints"),
            )
            return {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}
    return {"error": "Method not found"}


if __name__ == "__main__":
    for line in sys.stdin:
        if line.strip():
            print(json.dumps(handle_request(json.loads(line))))
            sys.stdout.flush()
