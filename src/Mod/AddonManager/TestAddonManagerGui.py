# ***************************************************************************
# *                                                                         *
# *   Copyright (c) 2022-2023 FreeCAD Project Association                   *
# *                                                                         *
# *   This file is part of FreeCAD.                                         *
# *                                                                         *
# *   FreeCAD is free software: you can redistribute it and/or modify it    *
# *   under the terms of the GNU Lesser General Public License as           *
# *   published by the Free Software Foundation, either version 2.1 of the  *
# *   License, or (at your option) any later version.                       *
# *                                                                         *
# *   FreeCAD is distributed in the hope that it will be useful, but        *
# *   WITHOUT ANY WARRANTY; without even the implied warranty of            *
# *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU      *
# *   Lesser General Public License for more details.                       *
# *                                                                         *
# *   You should have received a copy of the GNU Lesser General Public      *
# *   License along with FreeCAD. If not, see                               *
# *   <https://www.gnu.org/licenses/>.                                      *
# *                                                                         *
# ***************************************************************************

# Unit test for the Addon Manager module GUI
from AddonManagerTest.gui.test_gui import TestGui as AddonManagerTestGui

from AddonManagerTest.gui.test_workers_utility import (
    TestWorkersUtility as AddonManagerTestWorkersUtility,
)
from AddonManagerTest.gui.test_workers_startup import (
    TestWorkersStartup as AddonManagerTestWorkersStartup,
)
from AddonManagerTest.gui.test_installer_gui import (
    TestInstallerGui as AddonManagerTestInstallerGui,
)
from AddonManagerTest.gui.test_installer_gui import (
    TestMacroInstallerGui as AddonManagerTestMacroInstallerGui,
)
from AddonManagerTest.gui.test_update_all_gui import (
    TestUpdateAllGui as AddonManagerTestUpdateAllGui,
)
from AddonManagerTest.gui.test_uninstaller_gui import (
    TestUninstallerGUI as AddonManagerTestUninstallerGUI,
)

# dummy usage to get flake8 and lgtm quiet
False if AddonManagerTestGui.__name__ else True
False if AddonManagerTestWorkersUtility.__name__ else True
False if AddonManagerTestWorkersStartup.__name__ else True
False if AddonManagerTestInstallerGui.__name__ else True
False if AddonManagerTestMacroInstallerGui.__name__ else True
False if AddonManagerTestUpdateAllGui.__name__ else True
False if AddonManagerTestUninstallerGUI.__name__ else True
