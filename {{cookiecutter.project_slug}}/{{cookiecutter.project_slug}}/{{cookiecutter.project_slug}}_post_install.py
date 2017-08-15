import os
import sys
from win32com.client import Dispatch


# import shutil
# import glob


def create_shortcut(name, location):
    python_install = sys.base_prefix
    shell = Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(os.path.join(location, name + '.lnk'))
    shortcut.Targetpath = python_install + f'/Scripts/{name}.exe'
    shortcut.WorkingDirectory = os.path.expanduser('~') + f'/{name}'
    shortcut.IconLocation = python_install + f'/lib/site-packages/{name}.ico'
    shortcut.save()


def main():
    """
    Create application directory and shortcuts to entry points

    """
    # create application directory
    app_path = os.path.expanduser('~') + '/{{ cookiecutter.project_slug }}'
    if not os.path.exists(app_path):
        os.makedirs(app_path)

    # example of copying default app data
    """
    shutil.copy(module_path + '', app_path)
    for f in glob.glob(module_path + '/*'):
        shutil.copy(f, app_path+'/')
    """

    # launcher and uninstall shortcuts
    create_shortcut('{{ cookiecutter.project_slug }}', os.path.expanduser('~') + '/Desktop')
    create_shortcut('{{ cookiecutter.project_slug }}_uninstall', os.path.expanduser('~'))


if __name__ == '__main__':
    main()
