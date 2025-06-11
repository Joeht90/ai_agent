from main import main


def test():
    main("what files are in the root?", verbose=False)
    main("what files are in the pkg directory?", verbose=False)

if __name__ == "__main__":
    test()
