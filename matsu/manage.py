#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    # If you create a settings_dev.py and settings_prod.py, change second parameter to "matsu.settings_dev" for development.
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "matsu.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
