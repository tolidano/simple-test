#!/usr/bin/env python3
import random, unittest

class MyTestClass(unittest.TestCase):
    def testThatAlwaysPasses(self):
        self.assertTrue(True)
        self.assertFalse(False)
        self.assertNotEqual(True, False)

    def testThatSometimesFails(self):
        self.assertTrue(True)
        self.assertFalse(False)

        # "Do I feel lucky?"
        self.assertNotEqual(0, random.randrange(0,6))

        # "Well do ya, punk?"
        self.assertNotEqual(0, random.randrange(0,6))
