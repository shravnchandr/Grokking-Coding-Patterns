class Solution:
    def numDecodings(self, string: str) -> int:
        decoding_array = [0] * len(string +1)
        decoding_array[len(string)] = 1

        for index in range(len(string) -1, -1, -1):
            if string[index] != '0':
                decoding_array[index] = decoding_array[index +1]

            if index < len(string) -1 and 10 <= int(string[index: index +2]) <= 26:
                decoding_array[index] = decoding_array[index] + decoding_array[index +2]

        return decoding_array[0]
        