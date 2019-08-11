class Solution:
    def defangIPaddr(self, address: str) -> str:
        split_address = address.split('.')
        defanged = []
        for el in split_address: 
            defanged.append(el)
            defanged.append('[.]')
        return ''.join(defanged)[:-3]