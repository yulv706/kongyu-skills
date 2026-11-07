from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from audience_use_gate import parse_gate, validate


class AudienceUseGateTests(unittest.TestCase):
    def parse(self, body: str) -> dict[str, str]:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "spec_lock.md"
            path.write_text(body, encoding="utf-8")
            return parse_gate(path)

    def test_rejected_status_blocks_full_build(self) -> None:
        values = self.parse("## audience_use_gate\n- status: rejected\n")
        self.assertTrue(validate(values, "full-build"))

    def test_ai_reviewer_cannot_satisfy_gate(self) -> None:
        values = self.parse(
            "## audience_use_gate\n"
            "- status: sequence_approved\n"
            "- human_reviewer: ChatGPT reviewer\n"
            "- sequence: beats 1-6\n"
            "- retell: the user returns to the same task through gated authority\n"
            "- loss_points: none observed\n"
        )
        self.assertIn(
            "human_reviewer cannot be an AI, agent, model, or unknown reviewer",
            validate(values, "full-build"),
        )

    def test_human_sequence_approval_allows_full_build(self) -> None:
        values = self.parse(
            "## audience_use_gate\n"
            "- status: sequence_approved\n"
            "- human_reviewer: human reviewer A\n"
            "- sequence: beats 1-6 in order\n"
            "- retell: the relationship, not the old connection, authorizes return\n"
            "- loss_points: confused one term, repaired before beat 5\n"
            "- spoken_run: not_run\n"
        )
        self.assertEqual([], validate(values, "full-build"))

    def test_audience_ready_requires_spoken_run(self) -> None:
        values = self.parse(
            "## audience_use_gate\n"
            "- status: audience_ready\n"
            "- human_reviewer: independent human\n"
            "- sequence: complete talk\n"
            "- retell: a valid unassisted retell\n"
            "- loss_points: none observed\n"
            "- unseen_transfer: correctly solved a new cross-layer case\n"
            "- delayed_reconstruction: correct after a short delay\n"
            "- spoken_run: failed\n"
        )
        self.assertIn(
            "spoken_run must be passed for audience-ready",
            validate(values, "audience-ready"),
        )

    def test_audience_ready_requires_unseen_transfer_and_delay(self) -> None:
        values = self.parse(
            "## audience_use_gate\n"
            "- status: audience_ready\n"
            "- human_reviewer: independent human\n"
            "- sequence: complete talk\n"
            "- retell: a valid unassisted retell\n"
            "- loss_points: none observed\n"
            "- spoken_run: passed\n"
        )
        errors = validate(values, "audience-ready")
        self.assertIn("unseen_transfer is required for audience-ready", errors)
        self.assertIn("delayed_reconstruction is required for audience-ready", errors)

    def test_placeholder_words_do_not_count_as_human_evidence(self) -> None:
        values = self.parse(
            "## audience_use_gate\n"
            "- status: audience_ready\n"
            "- human_reviewer: pending\n"
            "- sequence: TBD\n"
            "- retell: todo\n"
            "- loss_points: not_run\n"
            "- unseen_transfer: pending\n"
            "- delayed_reconstruction: unknown\n"
            "- spoken_run: passed\n"
        )
        errors = validate(values, "audience-ready")
        for key in (
            "human_reviewer",
            "sequence",
            "retell",
            "loss_points",
            "unseen_transfer",
            "delayed_reconstruction",
        ):
            self.assertTrue(
                any(error.startswith(key) and "placeholder" in error for error in errors),
                f"{key} placeholder must fail closed: {errors}",
            )

    def test_audience_ready_passes_with_human_evidence(self) -> None:
        values = self.parse(
            "## audience_use_gate\n"
            "- status: audience_ready\n"
            "- human_reviewer: independent human\n"
            "- sequence: complete talk\n"
            "- retell: a valid unassisted retell\n"
            "- loss_points: none observed\n"
            "- unseen_transfer: correctly solved a new transport failure case\n"
            "- delayed_reconstruction: reconstructed the model after a short delay\n"
            "- spoken_run: passed\n"
        )
        self.assertEqual([], validate(values, "audience-ready"))


if __name__ == "__main__":
    unittest.main()
