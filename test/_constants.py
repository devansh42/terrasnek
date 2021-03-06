"""
Constants for default values in the TFE API implementation testing.
"""

import os
import sys

TFE_HOSTNAME = os.getenv("TFE_HOSTNAME", None)
TFE_TOKEN = os.getenv("TFE_TOKEN", None)

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", None)
GITHUB_SECRET = os.getenv("GITHUB_SECRET", None)

TEST_EMAIL = os.getenv("TEST_EMAIL", None)
TEST_ORG_NAME = os.getenv("TEST_ORG_NAME", None)
TEST_USERNAME = os.getenv("TEST_USERNAME", None)
TEST_TEAM_NAME = os.getenv("TEST_TEAM_NAME", None)

if TFE_HOSTNAME is None:
    sys.exit("Environment variable TFE_HOSTNAME must be set.")

if TFE_TOKEN is None:
    sys.exit("Environment variable TFE_TOKEN must be set.")

if GITHUB_TOKEN is None:
    sys.exit("Environment variable GITHUB_TOKEN must be set.")

if GITHUB_SECRET is None:
    sys.exit("Environment variable GITHUB_SECRET must be set.")

if TEST_EMAIL is None:
    sys.exit("Environment variable TEST_EMAIL must be set.")

if TEST_ORG_NAME is None:
    sys.exit("Environment variable TEST_ORG_NAME must be set.")

if TEST_USERNAME is None:
    sys.exit("Environment variable TEST_USERNAME must be set.")

if TEST_TEAM_NAME is None:
    sys.exit("Environment variable TEST_TEAM_NAME must be set.")
