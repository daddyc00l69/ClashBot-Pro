# -*- coding: utf-8 -*-
"""
ClashBot-Pro - Integrity and Verification Test Suite (New Update)
"""
import os
import sys
import unittest
import importlib

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOURCE_DIR = os.path.join(BASE_DIR, "Source")
RESOURCES_DIR = os.path.join(BASE_DIR, "Resources")

if SOURCE_DIR not in sys.path:
    sys.path.insert(0, SOURCE_DIR)

class TestRecoveredUpdate(unittest.TestCase):
    def test_fixed_points_count(self):
        import fixed_points_source
        self.assertGreaterEqual(len(fixed_points_source.__all__), 900)

    def test_new_modules_importable(self):
        new_mods = ['ranked_unlock', 'rush_bh', 'startup_checks', 'equipment_upgrade']
        for mod_name in new_mods:
            m = importlib.import_module(mod_name)
            self.assertIsNotNone(m)

    def test_templates_presence(self):
        tpl_dir = os.path.join(RESOURCES_DIR, "templates")
        self.assertTrue(os.path.exists(tpl_dir))
        count = sum(len(f) for _, _, f in os.walk(tpl_dir))
        self.assertGreaterEqual(count, 1020)

if __name__ == '__main__':
    unittest.main()
