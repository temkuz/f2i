from f2i.cli import parse_args


def main():
    namespace = parse_args()
    if namespace.func is not None:
        namespace.func(namespace)


if __name__ == '__main__':
    main()
