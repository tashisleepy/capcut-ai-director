"""OpenAI LLM client for duplicate detection (optional, requires OPENAI_API_KEY)."""

import json
from typing import Optional

from openai import OpenAI

from smartcut.config import LLM_MODEL
from smartcut.core.models import DuplicateGroup, DuplicateGroups

DUPLICATE_DETECTION_PROMPT = """You are analyzing a video transcript where the speaker often repeats the same phrase multiple times (multiple takes). The LAST take is always the best.

Below are consecutive text blocks separated by pauses. Identify groups of blocks that are duplicate takes of the same content. For each group, mark which one to KEEP (always the last one in the group) and which ones to REMOVE.

Rules:
- Only group blocks that are clearly attempts at saying the same thing
- If a block is unique content (not a retry), don't include it in any group
- The "keep" block should always be the last one in the duplicate group
- Be conservative - only mark as duplicates if you're confident

Blocks:
{blocks}

Return JSON in this exact format:
{{
  "groups": [
    {{
      "block_ids": [1, 2, 3],
      "keep": 3,
      "remove": [1, 2],
      "reason": "Three attempts at the same intro"
    }}
  ]
}}

If there are no duplicates, return: {{"groups": []}}"""


class LLMClient:
    """Client for OpenAI Chat API for content analysis."""

    def __init__(self, api_key: str, model: Optional[str] = None):
        self.client = OpenAI(api_key=api_key)
        self.model = model or LLM_MODEL

    def detect_duplicates(self, paragraphs: list[dict]) -> DuplicateGroups:
        """
        Detect duplicate takes in a list of paragraphs.

        Args:
            paragraphs: List of dicts with 'id' and 'text' keys.

        Returns:
            DuplicateGroups with identified duplicate groups.
        """
        if not paragraphs:
            return DuplicateGroups(groups=[])

        blocks_text = "\n".join(
            f"[{p['id']}] \"{p['text']}\""
            for p in paragraphs
        )

        prompt = DUPLICATE_DETECTION_PROMPT.format(blocks=blocks_text)

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a video editing assistant that identifies duplicate takes in transcripts."},
                {"role": "user", "content": prompt},
            ],
            response_format={"type": "json_object"},
            temperature=0.1,
        )

        result = json.loads(response.choices[0].message.content)
        groups = [
            DuplicateGroup(
                block_ids=g["block_ids"],
                keep=g["keep"],
                remove=g["remove"],
                reason=g.get("reason", ""),
            )
            for g in result.get("groups", [])
        ]
        return DuplicateGroups(groups=groups)
