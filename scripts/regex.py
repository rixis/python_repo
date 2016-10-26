#!/usr/bin/env python3.5
#
#

import re
import sys

p = re.compile('[a-z]+')

print(p.match(sys.argv[1]))

# end of script
