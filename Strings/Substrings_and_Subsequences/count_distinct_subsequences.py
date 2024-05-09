def solve(string: str) -> int:
    dp = [0] * (len(string) + 1)
    dp[0] = 1

    mp = {}
    idx = 1

    while idx < len(dp):
        dp[idx] = dp[idx - 1] * 2
        c = string[idx - 1]

        if c in mp:
            dp[idx] -= dp[mp[c] - 1]
        mp[c] = idx
        idx += 1

    return dp[-1]


if __name__ == "__main__":
    string = 'gfg'
    print(solve(string))
