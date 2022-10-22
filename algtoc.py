from akamus import Kamus
from utils.fragmenter import fragment
import sys
# sys.tracebacklimit = 0

if __name__ == "__main__":
    # t = Kamus(open("test.alg").read(), 0, 0)
    frag = fragment("test.alg")

    # try:
    #     t.show_tokens()
    #     t.show_register()
    # except SyntaxError as e:
    #     print(e)
    # except ValueError:
    #     pass