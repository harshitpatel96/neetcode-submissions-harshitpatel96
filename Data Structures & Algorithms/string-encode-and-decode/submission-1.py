class Solution:
    """
    ["Hello", "World"] => "encoded string" => decoded list = ["Hello", "World"]

    "5#Hello5#World20#"

    A naiive algorithm would be iterating over each word in the list and then for each character of the string add a ord for that character and make that , seperated and then the final string would be that comma separated string along with other comma separated string from other words which is ; seperated. something like "97,98,44;44,66,98,45; ...." it would be O(mxn) time and O(mxn) space for the answer itself no extra space? I am not sure about the space
    """
    def encode(self, strs: List[str]) -> str:
        ans=""
        for s in strs:
            ans += str(len(s)) + "#" + s
        print(ans)
        return ans

    def decode(self, s: str) -> List[str]:
        ans = []
        j = 0
        while j < len(s):
            i = j
            while s[j] != "#":
                j += 1
            slen = int(s[i:j])
            i = j + 1
            j = i + slen
            ans.append(s[i:j])


        return ans

