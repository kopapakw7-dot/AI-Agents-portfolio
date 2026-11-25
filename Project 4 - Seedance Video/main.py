"""Generate a video with MAGI-2 (Sand AI, text-to-video) through the Higgsfield API.

Credentials are read at runtime from HF_KEY (format: key-id:key-secret) in
.env.local next to this file. The value is never printed or logged.
"""

import os
import sys
from pathlib import Path

from dotenv import load_dotenv

# Load .env.local before importing the SDK client so HF_KEY is in the environment.
load_dotenv(Path(__file__).with_name(".env.local"))

import higgsfield_client  # noqa: E402
from higgsfield_client import (  # noqa: E402
    NSFW,
    Cancelled,
    Completed,
    CredentialsMissedError,
    Failed,
    HiggsfieldClientError,
    InProgress,
    Queued,
)

MODEL = os.getenv("HF_MODEL", "sand/magi-2/text-to-video")
ARGUMENTS = {
    "prompt": "A cinematic scene at sunset",
    "duration": 5,  # 4-30 seconds
    "resolution": "1080p",  # MAGI-2 supports 1080p only
    "aspect_ratio": "16:9",
}


def find_video_url(result: dict) -> str | None:
    """Return the generated video's URL from the result payload, if present."""
    video = result.get("video")
    if isinstance(video, dict) and video.get("url"):
        return video["url"]
    for item in result.get("videos") or []:
        if isinstance(item, dict) and item.get("url"):
            return item["url"]
    if isinstance(result.get("url"), str):
        return result["url"]
    return None


def main() -> int:
    final_status = {"value": None}

    def on_enqueue(request_id: str) -> None:
        print(f"Request submitted: {request_id}")

    def on_queue_update(status) -> None:
        changed = type(status) is not type(final_status["value"])
        final_status["value"] = status
        if changed and isinstance(status, Queued):
            print("Status: queued")
        elif changed and isinstance(status, InProgress):
            print("Status: in progress")

    try:
        result = higgsfield_client.subscribe(
            MODEL,
            arguments=ARGUMENTS,
            on_enqueue=on_enqueue,
            on_queue_update=on_queue_update,
        )
    except CredentialsMissedError:
        print("Error: HF_KEY is not set. Add it to .env.local as key-id:key-secret.", file=sys.stderr)
        return 1
    except HiggsfieldClientError as exc:
        print(f"Error: Higgsfield API request failed: {exc}", file=sys.stderr)
        return 1

    status = final_status["value"]
    status_text = result.get("status") if isinstance(result, dict) else None

    if isinstance(status, Failed) or status_text == "failed":
        print(f"Generation failed: {result.get('error') or result}", file=sys.stderr)
        return 1
    if isinstance(status, Cancelled) or status_text == "canceled":
        print("Generation was canceled.", file=sys.stderr)
        return 1
    if isinstance(status, NSFW) or status_text == "nsfw":
        print("Generation was blocked by content moderation (NSFW).", file=sys.stderr)
        return 1
    if not (isinstance(status, Completed) or status_text == "completed"):
        print(f"Unexpected final status: {status_text or status}", file=sys.stderr)
        return 1

    url = find_video_url(result)
    if not url:
        print(f"Completed, but no video URL was found in the response: {result}", file=sys.stderr)
        return 1

    print(f"Video URL: {url}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
