# capcut-ai-director

**The first AI editing director for CapCut Desktop Pro.** Upload a video. Get frame-accurate, timestamped editing instructions with real CapCut asset names. No vague advice. No hallucinations. Surgical precision.

---

## What This Does

You film. AI directs. You execute.

Instead of "add some transitions here," you get:

```
00:00:05:00
Action: Add Flash transition (duration: 00:00:00:06)
Path: Left panel → Transitions → Trending → Flash
Why: Beat drop in background audio. Flash aligns with energy spike
```

### Before vs After

| Traditional AI Feedback | capcut-ai-director |
|---|---|
| "The opening is slow, add some pacing" | "00:00:00:00-00:00:02:00: Cut initial silence. Dead air kills retention in first 2s" |
| "Use a transition between these shots" | "00:00:05:00: Add Flash transition (6 frames). Left panel → Transitions → Trending → Flash" |
| "Add captions for emphasis" | "00:00:02:00: Add caption 'This changed everything'. Style: Bold Impact. KF-05 Bold Impact template #7" |
| "Color grade to match mood" | "00:00:08:15: Apply AI Stylize with Preset ID: warm-cinematic-35. Strength: 0.7" |

---

## Quick Demo

**Input:** Your video file (any length, any format CapCut supports)

**Output:** Timestamped editing plan across three stages

```markdown
VIDEO EDIT PLAN
Platform: TikTok
Intensity: 4
Mode: Viral
Frame Rate: 30fps

═══════════════════════════════════════════

HOOK SECTION (00:00:00:00-00:00:04:00)

00:00:00:00-00:00:02:00
Action: Cut initial 2-second silence
Navigation: Right panel → Timeline → select segment → Delete
Why: Dead air kills retention in first 2 seconds

00:00:02:00
Action: Add text overlay - "Watch to the end"
Style: KF-05 #12 Bold Impact White
Duration: 00:00:00:20 (duration on screen)
Position: Center of frame
Why: Anchors viewer attention before hook payload

00:00:02:15
Action: Add zoom animation
Effect: Zoom-In
Amount: 108%
Duration: 00:00:00:12
Easing: Ease-Out
Why: Emphasis on speaker's vocal inflection.visual punch

═══════════════════════════════════════════

BODY SECTION (00:00:04:00-00:00:12:00)

00:00:05:00
Action: Add transition before dialogue shift
Type: Flash transition (KF-03 #14)
Duration: 00:00:00:06
Navigation: Left panel → Transitions → Trending → Flash
Why: Audio beat drop at this moment.Flash snaps with energy

...
```

Every timestamp. Every asset. Every "why."

---

## Architecture

```
USER VIDEO
    ↓
┌─────────────────────────────┐
│ Stage 1: Free Analysis      │
│ (Gemini multimodal)         │
│ - Scene detection           │
│ - Speech/emotion/beats      │
│ - Silence & attention       │
└────────────┬────────────────┘
             ↓
    Creative brief (no CapCut)
             ↓
┌─────────────────────────────┐
│ Stage 2: Asset Grounding    │
│ (KF-01 through KF-10        │
│  injected into prompt)      │
│ - 3,467 effects             │
│ - 2,225 transitions         │
│ - 600+ filters              │
│ - 200+ text templates       │
│ - 50+ sticker categories    │
│ - 10 Knowledge Files        │
└────────────┬────────────────┘
             ↓
    FRAME-ACCURATE EDITING PLAN
    (with exact asset names &
     navigation paths)
```

**Two-stage prompting** separates free creative thinking from grounded execution. Stage 1 prevents the asset catalog from constraining ideas; Stage 2 ensures every suggestion uses real CapCut tools.

---

## Installation

### Requirements
- Claude Code, Claude Desktop, Cursor, or VS Code
- Python 3.10+
- CapCut Desktop Pro installed (for opening/executing plans)

### Step 1: Clone the repo
```bash
git clone https://github.com/your-org/capcut-ai-director.git
cd capcut-ai-director
```

### Step 2: Set up the MCP server
```bash
cd mcp-server
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -e .
```

### Step 3: Configure Claude Code / Claude Desktop

Add to your `claude_desktop_config.json` (Mac: `~/.claude/claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "capcut-director": {
      "command": "/path/to/capcut-ai-director/mcp-server/venv/bin/python",
      "args": ["-m", "smartcut.server"]
    }
  }
}
```

**Windows path example:**
```json
"command": "C:\\Users\\YourName\\capcut-ai-director\\mcp-server\\venv\\Scripts\\python.exe"
```

### Step 4: Restart Claude Code or Claude Desktop

The `capcut-director` MCP server is now available. Claude can now:
- List your CapCut projects
- Open and inspect projects
- Smart-cut (silence + duplicate removal)

---

## Usage

### In Claude Code / Claude Desktop

**Direct the edit of a video:**
```
I just filmed a product demo. Can you direct the edit for TikTok?
Use viral intensity (4/5), and assume 30fps.
My CapCut file is "Product Demo - Take 3".
```

**Result:** Timestamped editing plan with every action, path, and reason.

### Available MCP Tools

| Tool | Use | Example |
|------|-----|---------|
| `list_capcut_projects` | See your drafts | "Show me my CapCut projects" |
| `open_capcut_project` | Inspect a project | "Open 'My Vlog' project" |
| `smart_cut_project` | Auto-cut silences + duplicates | "Smart cut 'Podcast #5'" |

---

## Knowledge Base

**380 KB of structured CapCut intelligence** across 10 Knowledge Files:

| KF | Content | Count |
|---|---|---|
| KF-01 | Core UI Navigation (left panel, right panel, timeline controls) | 538 lines |
| KF-02 | All Effects (name, icon, category, use case) | 4,042 lines |
| KF-03 | Transitions (all 2,225 variations with metadata) | 2,393 lines |
| KF-04 | Filters (600+ with names & previews) | 186 lines |
| KF-05 | Text & Captions (200+ templates, fonts, styles) | 744 lines |
| KF-06 | Stickers (50+ categories, naming convention) | 651 lines |
| KF-07 | Audio & Music Intelligence (Suno integration, mixing tips) | 1,123 lines |
| KF-08 | Animations (preset names, easing, duration) | 586 lines |
| KF-09 | Effect Metadata (top 150 effects, advanced settings) | 1,447 lines |
| KF-10 | AI Stylize (presets, strength settings, mood matching) | 211 lines |

**Total:** ~13,000 lines of actionable CapCut knowledge.

---

## Creative Modes

Choose your edit style. AI adapts intensity and asset selection accordingly.

| Mode | Vibe | Best For | Intensity | Example Output |
|------|------|----------|-----------|---|
| **Viral** | Fast cuts, hooks, rapid fire | TikTok, Reels, YouTube Shorts | 4-5 | Flash + zoom + captions every 2s |
| **Cinematic** | Smooth transitions, color grading, depth | Brand films, product launches, vlogs | 2-3 | Slow dissolves, subtle color grades, 12-frame transitions |
| **Documentary** | Pacing, lower thirds, voiceover emphasis | Explainers, interviews, podcasts | 2-3 | Silence cuts, text overlays, subtle zoom |
| **Meme** | Jump cuts, speed ramps, sound effects | Comedy, reaction, trending audio | 5 | Hard cuts, 2-4 frame transitions, rapid captions |
| **Aesthetic** | Color-first, filters, minimal movement | Fashion, luxury, interior, mood content | 1-2 | AI Stylize preset, one slow zoom, minimal transitions |
| **Minimal** | Clean, breathing room, intentional pauses | Conferences, slow-burn storytelling, ASMR | 1 | Hard cuts only, no effects, text only when necessary |

---

## Examples

### Example 1: TikTok Product Demo (Viral, Intensity 4)

**Command:**
```
Direct the edit for my product demo "iPhone Case Unboxing".
Platform: TikTok
Mode: Viral
Intensity: 4
Frame rate: 30fps
```

**Output snippet:**
```
HOOK (00:00:00:00–00:00:03:00)

00:00:00:00–00:00:01:00
Action: Cut silence (B-roll of hand moving to box)
Why: Hook must start with action, not dead air

00:00:01:00
Action: Add text "This case is INSANE"
Style: KF-05 #8 (Bold Impact, white outline)
Duration: 00:00:00:18
Why: Establish value claim before unboxing

00:00:01:15
Action: Zoom to 110% over 00:00:00:12 (12 frames)
Easing: Ease-Out
Why: Vocal stress on "INSANE".zoom reinforces emphasis

00:00:02:00
Action: Hard cut to close-up of case
Transition: None
Why: Action change + audio beat.hard cut is cleanest
```

### Example 2: LinkedIn Thought Leadership (Cinematic, Intensity 2)

**Command:**
```
I'm talking about the future of AI (2:14 video).
Platform: LinkedIn
Mode: Cinematic
Intensity: 2
Frame rate: 30fps
```

**Output snippet:**
```
INTRO (00:00:00:00–00:00:10:00)

00:00:00:00–00:00:02:00
Action: Slow dissolve from black to speaker
Transition: Dissolve (KF-03 #45)
Duration: 00:00:01:00
Why: Cinematic entrance.builds anticipation

00:00:02:15
Action: Add lower-third graphic "AI transformation"
Style: KF-05 #3 (Corporate, sans-serif, left-aligned)
Duration: video length (stays on screen)
Why: Professional context + speaker intro

00:00:05:00
Action: Apply AI Stylize."warm corporate"
Preset: KF-10 #2 (warm-professional-40)
Strength: 0.65
Why: Color grade supports "optimistic future" narrative
```

---

## MCP Tools

The backing MCP server provides three core tools:

### `list_capcut_projects`
Lists all CapCut projects in your drafts folder.
```
INPUT: (none)
OUTPUT: [
  { name: "Product Demo - Take 3", path: "...", created: "2026-04-01" },
  { name: "Podcast #5", path: "...", created: "2026-03-28" },
  ...
]
```

### `open_capcut_project`
Opens and inspects a CapCut project. Returns video segments, text, audio, effects currently applied.
```
INPUT: { project_name: "Product Demo - Take 3" }
OUTPUT: {
  segments: [...],
  text_elements: [...],
  audio_tracks: [...],
  applied_effects: [...]
}
```

### `smart_cut_project`
Auto-removes silences (gaps > 1s between subtitles) and duplicate takes.
Requires auto-generated subtitles in CapCut (Text → Auto Captions).
```
INPUT: { project_name: "Podcast #5" }
OUTPUT: { removed_ranges: [...], duplicates_removed: [...] }
```

---

## Timecode Format

All editing instructions use CapCut's native **frame-based timecode**: `HH:MM:SS:FF`

| Example | Meaning |
|---------|---------|
| `00:00:00:00` | Frame 0 |
| `00:00:00:15` | Frame 15 (0.5 sec at 30fps) |
| `00:00:01:00` | Frame 0 of second 1 (exactly 1.0 sec) |
| `00:00:10:00` | 10 seconds |
| `00:01:00:00` | 1 minute |

**Range example:** `00:00:01:00-00:00:03:15` = from 1.0s to 3.5s

**At 30fps, valid frames are 00–29.** Frame 30 doesn't exist; it rolls to 00:00:01:00.

Why frame-accurate? Because the CapCut timeline displays frames. Direct timecode matching = zero conversion errors.

---

## Pricing & Commercial Use

**MIT License** - free for personal and commercial use. Fork, modify, deploy.

---

## Contributing

Issues, feature requests, and PRs welcome.

**For knowledge file updates** (new effects, transitions, filters added to CapCut):
1. Submit PR updating relevant KF file
2. Include CapCut version tested
3. Include screenshot evidence of new asset in CapCut UI

**For mode additions** (new creative styles beyond Viral/Cinematic/etc):
1. Define the intensity curve and asset selection rules
2. Include 3 example outputs
3. PR against `brain/capcut-ai-director-brain.md`

---

## Credits

- **Brain architecture:** [Tashi](https://github.com/tashisleepy)
- **CapCut UI mapping:** 101 screen recordings + 193 panel screenshots + expert review feedback
- **Knowledge files:** Community contributors + CapCut desktop research
- **Two-stage prompting:** Inspired by frontier AI directing work in commercial production

---

## License

MIT
