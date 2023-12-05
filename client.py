#!/usr/bin/env python
"""Convert stdin to upper case."""
for line in iter(raw_input, 'quit'):
        print line.upper()
