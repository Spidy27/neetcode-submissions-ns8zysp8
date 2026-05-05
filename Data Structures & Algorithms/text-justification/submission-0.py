class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        stack = []
        width = 0

        for word in words:
            if width + len(word) + len(stack) > maxWidth:
                total_spaces = maxWidth - width
                gaps = len(stack) - 1

                if gaps == 0:
                    res.append(stack[0] + ' '* total_spaces)
                else:
                    space, extra = divmod(total_spaces, gaps)
                    line = ""
                    for i, w in enumerate(stack):
                        line += w
                        if i < gaps:
                            line += ' ' * space + (' ' if i < extra else '')
                    res.append(line)

                stack = [word]
                width = len(word)
            else:
                stack.append(word)
                width += len(word)
        last_line = ' '.join(stack)
        res.append(last_line + ' '*(maxWidth - len(last_line)))

        return res 
            