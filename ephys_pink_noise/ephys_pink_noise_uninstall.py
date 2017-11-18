import os
import shutil
import pip


def main():
    shutil.rmtree(os.path.expanduser('~') + '/ephys_pink_noise', ignore_errors=True)
    pip.main(["uninstall", 'ephys_pink_noise'])
    os.remove(os.path.expanduser('~') + '/Desktop/ephys_pink_noise.lnk')


if __name__ == '__main__':
    main()
