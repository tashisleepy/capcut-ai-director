"""Pydantic data models for SmartCut."""

from typing import Optional

from pydantic import BaseModel, Field

from smartcut.config import MICROSECONDS_PER_SECOND


# Duplicate detection models (used by optional OpenAI mode)

class DuplicateGroup(BaseModel):
    """A group of duplicate paragraphs."""

    block_ids: list[int]
    keep: int
    remove: list[int]
    reason: str


class DuplicateGroups(BaseModel):
    """Result of duplicate detection."""

    groups: list[DuplicateGroup] = Field(default_factory=list)


# CapCut project models

class ProjectInfo(BaseModel):
    """CapCut project metadata."""

    name: str
    path: str
    project_id: str
    duration_us: int
    duration_formatted: str
    modified_time: int
    video_count: int = 0
    has_content: bool = True


class ExistingVideoSegment(BaseModel):
    """Video segment from existing CapCut project."""

    id: str
    material_id: str
    source_path: str
    timeline_start: float  # seconds
    timeline_end: float  # seconds
    source_start: float  # seconds
    source_end: float  # seconds
    duration: float  # seconds


class ExistingVideoMaterial(BaseModel):
    """Video material from existing CapCut project."""

    id: str
    path: str
    duration: float  # seconds
    width: int
    height: int


class ExistingTextSegment(BaseModel):
    """Text segment from existing CapCut project."""

    id: str
    material_id: str
    text: str
    timeline_start: float  # seconds
    timeline_end: float  # seconds


class CapCutProjectData(BaseModel):
    """Parsed CapCut project structure."""

    project_id: str
    project_name: str
    project_path: str
    duration: float  # seconds
    canvas_width: int
    canvas_height: int
    video_materials: list[ExistingVideoMaterial] = Field(default_factory=list)
    video_segments: list[ExistingVideoSegment] = Field(default_factory=list)
    text_segments: list[ExistingTextSegment] = Field(default_factory=list)


# CapCut auto-subtitle model

class CapCutSubtitleSegment(BaseModel):
    """A subtitle segment read from CapCut's auto-generated subtitles."""

    segment_id: str
    material_id: str
    text: str
    words_text: list[str] = Field(default_factory=list)
    words_start_ms: list[int] = Field(default_factory=list)
    words_end_ms: list[int] = Field(default_factory=list)
    timeline_start_us: int
    timeline_duration_us: int
    recognize_task_id: str

    @property
    def timeline_start_sec(self) -> float:
        return self.timeline_start_us / MICROSECONDS_PER_SECOND

    @property
    def timeline_end_sec(self) -> float:
        return (self.timeline_start_us + self.timeline_duration_us) / MICROSECONDS_PER_SECOND

    @property
    def timeline_end_us(self) -> int:
        return self.timeline_start_us + self.timeline_duration_us
