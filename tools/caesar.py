from string import ascii_lowercase
from string import digits


def caesar(text):
    for i in range(len(ascii_lowercase)):
        for c in text:
            if c in ascii_lowercase:
                print(chr((ord(c) + i) % 26 + 97), end="")
            elif c in digits:
                print(chr(27 - (int(c)) % 26 + 97), end="")
            else:
                print(c, end="")

        print()


if __name__ == "__main__":
    caesar("ny_nx_tsq3_zumnqq_kwtr_mjwj_68bcbcabc7")
