import sys
from pathlib import Path

# Add parent directory to sys.path to allow importing StaffService
sys.path.append(str(Path(__file__).parent.parent))

import StaffService

if __name__ == "__main__":
    StaffService.menu_staff()
