if __name__ == '__main__':
    def bracket_check(test_string):
        result = 0
        for a in test_string:
            if "(" in a:
                result += 1
            elif ")" in a:
                result -= 1

            if result < 0:
                return "NO"
        if result > 0:
            return "NO"
        return "YES"


    print(bracket_check(input()))