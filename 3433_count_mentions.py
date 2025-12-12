class Solution(object):
    def countMentions(self, numberOfUsers, events):
        """
        :type numberOfUsers: int
        :type events: List[List[str]]
        :rtype: List[int]
        """
        mentions = [0] * numberOfUsers
        offline_until = [0] * numberOfUsers  # time when user becomes online again

        # Group events by timestamp preserving input order within the same timestamp
        from collections import defaultdict
        buckets = defaultdict(list)
        for ev in events:
            typ, ts, data = ev
            t = int(ts)
            buckets[t].append((typ, data))

        # Process timestamps in chronological order
        for t in sorted(buckets.keys()):
            group = buckets[t]

            # 1) Apply all OFFLINE events at this timestamp first
            for typ, data in group:
                if typ == "OFFLINE":
                    user_id = int(data)
                    # user becomes offline immediately at t and will come back at t+60
                    offline_until[user_id] = t + 60

            # Compute online status AFTER applying OFFLINEs and any automatic comebacks at t
            online = [t >= offline_until[i] for i in range(numberOfUsers)]

            # 2) Now handle MESSAGE events at this timestamp (in original order)
            for typ, data in group:
                if typ != "MESSAGE":
                    continue
                msg = data.strip()
                if msg == "ALL":
                    # ALL includes offline users too
                    for i in range(numberOfUsers):
                        mentions[i] += 1
                elif msg == "HERE":
                    # Only currently online users
                    for i in range(numberOfUsers):
                        if online[i]:
                            mentions[i] += 1
                else:
                    # explicit id<number> tokens (may have duplicates)
                    tokens = msg.split()
                    for tok in tokens:
                        if tok.startswith("id"):
                            user_id = int(tok[2:])
                            mentions[user_id] += 1

        return mentions
