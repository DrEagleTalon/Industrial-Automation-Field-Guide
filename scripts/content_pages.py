"""Aggregates all content modules. Import and use ALL_PAGES."""
from content_04_motor_control import CONTENT as C04
from content_05_plcs             import CONTENT as C05
from content_06_programming      import CONTENT as C06
from content_07_hmi              import CONTENT as C07
from content_08_networks         import CONTENT as C08
from content_09_troubleshooting  import CONTENT as C09
from content_10_integration      import CONTENT as C10
from content_11_standards        import CONTENT as C11
from content_12_safety           import CONTENT as C12
from content_13_specialty        import CONTENT as C13
from content_14_softskills       import CONTENT as C14

ALL_PAGES = {}
for src in (C04, C05, C06, C07, C08, C09, C10, C11, C12, C13, C14):
    for folder, files in src.items():
        ALL_PAGES.setdefault(folder, {}).update(files)
