# @author: zh
from input import loop, select_device

def main():
    device = select_device()
    loop(device)


if __name__ == '__main__':
    main()
