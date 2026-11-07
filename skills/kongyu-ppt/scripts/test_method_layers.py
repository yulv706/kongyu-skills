from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class MethodLayerTests(unittest.TestCase):
    def test_universal_principle_layer_exists_and_is_domain_free(self) -> None:
        path = ROOT / "references" / "principles-and-derivation.md"
        self.assertTrue(path.is_file(), "missing universal principle/derivation reference")
        text = path.read_text(encoding="utf-8")
        self.assertIn("## Universal principles", text)
        self.assertIn("## Scenario variables", text)
        self.assertIn("## Derivation", text)
        principles = text.split("## Universal principles", 1)[1].split(
            "## Scenario variables", 1
        )[0]
        for forbidden in (
            "tsshd",
            "QUIC",
            "Bash",
            "X25519",
            "AuthoritySnapshot",
            "worked-event",
            "attack-first",
            "proof-obligation",
        ):
            self.assertNotIn(forbidden.lower(), principles.lower())

    def test_universal_principles_do_not_force_graphics_or_linear_story_order(self) -> None:
        reference = (ROOT / "references" / "principles-and-derivation.md").read_text(
            encoding="utf-8"
        )
        principles = reference.split("## Universal principles", 1)[1].split(
            "## Scenario variables", 1
        )[0]
        self.assertIn("externally represented", principles)
        self.assertIn("dependency constraints", principles)
        for biased_phrase in (
            "A visual that only",
            "Sequence by prerequisites and consequences",
            "what question or consequence the current step creates",
        ):
            self.assertNotIn(biased_phrase, principles)

        entrypoint = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("linear or non-linear", entrypoint)
        self.assertNotIn("makes later units necessary or useful", entrypoint)

    def test_entrypoint_routes_principles_before_scenario_methods(self) -> None:
        text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        principle_ref = "references/principles-and-derivation.md"
        scenario_ref = "references/teaching-complex-systems.md"
        self.assertIn(principle_ref, text)
        self.assertIn(scenario_ref, text)
        self.assertLess(text.index(principle_ref), text.index(scenario_ref))
        self.assertNotRegex(text, re.compile(r"anchor event|concrete event", re.I))

    def test_complex_system_method_declares_derived_scope(self) -> None:
        text = (ROOT / "references" / "teaching-complex-systems.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("Derived scenario method", text)
        self.assertIn("principles-and-derivation.md", text)

    def test_derivation_examples_cover_distinct_scenario_families(self) -> None:
        text = (ROOT / "references" / "principles-and-derivation.md").read_text(
            encoding="utf-8"
        )
        for scenario in (
            "Novice teaching",
            "Expert design review",
            "Academic results",
            "Executive decision",
            "Incident or operations review",
            "Reading-first document",
        ):
            self.assertIn(scenario, text)

    def test_scenario_examples_preserve_distinct_reasoning_orders(self) -> None:
        text = (ROOT / "references" / "principles-and-derivation.md").read_text(
            encoding="utf-8"
        )
        expected_terms = {
            "Novice teaching": ("prerequisite", "transfer"),
            "Expert design review": ("threat", "proof obligations"),
            "Academic results": ("central finding", "interpreted figures"),
            "Executive decision": ("decision first", "recommendation"),
            "Incident or operations review": ("timeline", "state transitions"),
            "Reading-first document": ("navigation", "without narration"),
        }
        for scenario, terms in expected_terms.items():
            row = next(
                (line for line in text.splitlines() if line.startswith(f"| {scenario} |")),
                "",
            )
            self.assertTrue(row, f"missing derivation example row: {scenario}")
            for term in terms:
                self.assertIn(term, row, f"{scenario} must preserve '{term}'")


if __name__ == "__main__":
    unittest.main()
