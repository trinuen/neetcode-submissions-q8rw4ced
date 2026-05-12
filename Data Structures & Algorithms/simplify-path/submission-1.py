class Solution:
    def simplifyPath(self, path: str) -> str:
        names = path.split('/')
        stack = []
        dirs  = {'.', '..'}
        
        for i in names:
            if len(i) > 0 and i not in dirs:
                stack.append(i)
            if stack and i == '..':
                stack.pop()
        return '/' + '/'.join(stack)