import re


class Solution:
    def isNumber(self, string: str) -> bool:
        pattern = re.compile(r"""
            ^\s*                             # Optional leading whitespace
            [+-]?                            # Optional sign
            (
                (\d+\.\d*)|(\.\d+)|(\d+)     # Digits with optional decimal
            )
            ([eE][+-]?\d+)?                  # Optional exponent
            \s*$                             # Optional trailing whitespace
        """, re.VERBOSE)
        
        return bool(pattern.match(string))
    