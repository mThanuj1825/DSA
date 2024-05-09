def search(string: str, sub_string: str, start=0) -> int:
    for i in range(start, len(string)):
        for j in range(i, i + len(sub_string) + 1):
            cur = string[i:j]
            if cur == sub_string:
                return i

    return -1


if __name__ == "__main__":
    string = "Hello World"
    sub_string = "world"
    print(search(string, sub_string))
