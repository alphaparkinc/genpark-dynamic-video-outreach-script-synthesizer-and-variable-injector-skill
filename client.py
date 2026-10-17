"""Dynamic Video Outreach Script Synthesizer and Variable Injector.
100% Python Standard Library.
"""

from typing import List, Dict, Any, Optional
import re


class VideoScriptSynthesizer:
    """Generates personalized video outreach scripts, calculates phoneme pacing and speaking duration,
    and injects dynamic variables (prospect name, company, pain point) with pronunciation hints."""

    WORDS_PER_MINUTE = 145.0

    @classmethod
    def synthesize_script(
        cls,
        template: str,
        variables: Dict[str, str],
        pronunciation_hints: Optional[Dict[str, str]] = None,
    ) -> Dict[str, Any]:
        """Substitutes variables into video outreach template and estimates natural speech duration."""
        pronunciation_hints = pronunciation_hints or {}
        rendered_script = template

        for key, val in variables.items():
            token = f"{{{{{key}}}}}"
            rendered_script = rendered_script.replace(token, str(val))

        words = re.findall(r'\w+', rendered_script)
        word_count = len(words)
        estimated_duration_seconds = round((word_count / cls.WORDS_PER_MINUTE) * 60, 1)

        # Build phoneme pronunciation overrides for avatar speech models
        active_pronunciations = {}
        for term, ipa_or_phonetic in pronunciation_hints.items():
            if term.lower() in rendered_script.lower():
                active_pronunciations[term] = ipa_or_phonetic

        # Pacing recommendation
        pacing_grade = "OPTIMAL_VIDEO_BYTE"
        if estimated_duration_seconds > 60.0:
            pacing_grade = "TOO_LONG_FOR_COLD_OUTREACH"
        elif estimated_duration_seconds < 15.0:
            pacing_grade = "VERY_BRIEF"

        return {
            "rendered_script": rendered_script,
            "word_count": word_count,
            "estimated_duration_seconds": estimated_duration_seconds,
            "pacing_grade": pacing_grade,
            "pronunciation_overrides": active_pronunciations,
            "injected_variables": variables,
        }
