import re

class Solution(object):
    def validateCoupons(self, code, businessLine, isActive):
        """
        :type code: List[str]
        :type businessLine: List[str]
        :type isActive: List[bool]
        :rtype: List[str]
        """
        priority = {
            "electronics": 0,
            "grocery": 1,
            "pharmacy": 2,
            "restaurant": 3
        }

        valid = []
        for i in range(0, len(code)):
            if not re.match(r"^[a-zA-Z0-9_]+$", code[i]):
                continue

            # 2. business line must be valid
            if businessLine[i] not in priority:
                continue

            # 3. coupon must be active
            if not isActive[i]:
                continue

            valid.append([code[i], businessLine[i]])

        # Sort by businessLine priority, then by code
        valid.sort(key=lambda x: (priority[x[1]], x[0]))

        # Return only codes
        return [c[0] for c in valid]