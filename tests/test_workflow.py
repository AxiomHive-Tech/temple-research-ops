# Project ownership and stewardship: Nicholas M. Grossi and Caden H. McCullen.
# File purpose: unit tests for the research workflow validator.
# Individual authorship is not asserted by this ownership/stewardship attribution.
# AI-assisted update: Manus AI. Human review and acceptance remain the responsibility of project operators.

import copy
import json
import tempfile
import unittest
from pathlib import Path

from validate_workflow import validate_files

BASE = Path(__file__).parent
SCHEMA = BASE / "workflow.schema.json"
EXAMPLE = BASE / "example_workflow.json"


class WorkflowValidationTests(unittest.TestCase):
    def setUp(self):
        temporary_directory = tempfile.TemporaryDirectory(prefix="workflow-validation-")
        self.addCleanup(temporary_directory.cleanup)
        self.temp_instance = Path(temporary_directory.name) / "workflow_instance.json"
        self.instance = json.loads(EXAMPLE.read_text(encoding="utf-8"))

    def validate(self, instance):
        self.temp_instance.write_text(json.dumps(instance), encoding="utf-8")
        return validate_files(SCHEMA, self.temp_instance)

    def test_sample_is_valid_and_release_is_held(self):
        self.assertEqual(self.instance["release"]["status"], "blocked")
        self.assertEqual(self.validate(self.instance), [])

    def test_release_without_human_approval_is_rejected(self):
        changed = copy.deepcopy(self.instance)
        changed["release"]["status"] = "released"
        changed["release"]["release_record"]["decision"] = "released"
        changed["release"]["release_record"]["released_at"] = "2026-10-22T18:51:00-04:00"
        changed["stages"][7]["status"] = "completed"
        changed["stages"][7]["record"]["decision"] = "release"
        changed["stages"][7]["record"]["released_at"] = "2026-10-22T18:51:00-04:00"
        errors = self.validate(changed)
        self.assertTrue(any("human approval" in error for error in errors), errors)

    def test_unknown_source_link_is_rejected(self):
        changed = copy.deepcopy(self.instance)
        changed["stages"][5]["record"]["claims"][0]["source_ids"] = ["missing-source"]
        errors = self.validate(changed)
        self.assertTrue(any("unknown source_id" in error for error in errors), errors)

    def test_stage_order_is_rejected_when_changed(self):
        changed = copy.deepcopy(self.instance)
        changed["stages"][0], changed["stages"][1] = changed["stages"][1], changed["stages"][0]
        errors = self.validate(changed)
        self.assertTrue(errors)

    def test_commercial_release_requires_rights_review(self):
        changed = copy.deepcopy(self.instance)
        changed["release"]["status"] = "released"
        changed["release"]["release_record"]["decision"] = "released"
        changed["release"]["release_record"]["released_at"] = "2026-10-22T18:51:00-04:00"
        changed["stages"][7]["status"] = "completed"
        changed["stages"][7]["record"]["decision"] = "release"
        changed["stages"][7]["record"]["released_at"] = "2026-10-22T18:51:00-04:00"
        changed["stages"][6]["status"] = "approved"
        changed["stages"][6]["completed_at"] = "2026-10-22T18:50:59-04:00"
        changed["stages"][6]["record"]["reviewed_at"] = "2026-10-22T18:50:59-04:00"
        changed["stages"][4]["started_at"] = "2026-10-22T18:49:31-04:00"
        changed["output"]["rights_review"] = "pending"
        errors = self.validate(changed)
        self.assertTrue(any("commercial" in error.lower() or "rights" in error.lower() for error in errors), errors)


if __name__ == "__main__":
    unittest.main()
