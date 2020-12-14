# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""This script is used to synthesize generated parts of this library."""

import synthtool as s
from synthtool import gcp

common = gcp.CommonTemplates()

# ----------------------------------------------------------------------------
# Add templated files
# ----------------------------------------------------------------------------
templated_files = common.py_library(cov_level=100)
s.move(
    templated_files,
    excludes=[
        "docs/multiprocessing.rst",
        "noxfile.py",
        ".flake8",
        ".coveragerc",
        "setup.cfg",
    ],
)

s.replace(
    "CONTRIBUTING.rst",
    """\
  3.5, 3.6, 3.7 and 3.8 on both UNIX and Windows.
""",
    """\
  3.6, 3.7 and 3.8 on both UNIX and Windows.
""",
)

s.replace(
    "CONTRIBUTING.rst",
    """\
- Once you have downloaded your json keys, set the environment variable[ ]
""",
    """\
- Once you have downloaded your json keys, set the environment variable
""",
)

s.replace(
    "CONTRIBUTING.rst",
    """\
We support:

-  `Python 3.5`_
-  `Python 3.6`_
-  `Python 3.7`_
-  `Python 3.8`_

.. _Python 3.5: https://docs.python.org/3.5/
.. _Python 3.6: https://docs.python.org/3.6/
.. _Python 3.7: https://docs.python.org/3.7/
.. _Python 3.8: https://docs.python.org/3.8/
""",
    """\
We support:

-  `Python 3.6`_
-  `Python 3.7`_
-  `Python 3.8`_

.. _Python 3.6: https://docs.python.org/3.6/
.. _Python 3.7: https://docs.python.org/3.7/
.. _Python 3.8: https://docs.python.org/3.8/
""",
)

s.replace(
    "CONTRIBUTING.rst",
    """\
We also explicitly decided to support Python 3 beginning with version
3.5. Reasons for this include:
""",
    """\
We also explicitly decided to support Python 3 beginning with version
3.6. Reasons for this include:
""",
)
