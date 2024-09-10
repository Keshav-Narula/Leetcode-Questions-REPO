class Solution(object):
  #Runtime 6ms Beats 97.68%
  #Memory 11.62 MB Beats 61.07%
    def mergeAlternately(self, word1, word2):
        i = 0
        j = 0
        result = []

        #Loop through until the end of the smaller string (word1, word 2)
        while i < len(word1) and j < len (word2):
            result.append(word1[i])
            result.append(word2[j])
            i+=1
            j+=1
        #Append any remaining characters from either string to the end of the result array 
        result.extend(word1[i:])
        result.extend(word2[j:])

        #Join the array of characters, with deliminator '' and return the resulting string
        return ''.join(result)

