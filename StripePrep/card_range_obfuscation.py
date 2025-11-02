def card_range_obfuscation(input_str: str) -> str:
    # Split the strin to each of their repective parts
    lines = [l.strip() for l in input_str.splitlines() if l.strip()]
    print(lines)
    bin6 = lines[0]
    n = int(lines[1])
    raw_intervals = lines[2:2+n]

    print(raw_intervals)

    # parse the intervals 10 digit number into a int
    intervals = []
    for r in raw_intervals:
        start_s, end_s, brand = r.split(",",2)
        start = int(start_s)
        end = int(end_s)
        intervals.append((start, end, brand))
    
    # Sort by the start offeset
    intervals.sort()
    print(intervals)

    MAX_OFFSET = 10_000_000_000 - 1 # 0 to 9,999,999,999 inclusive
    ptr = 0
    out = []

    for(s, e ,brand) in intervals:
        # If this interval is entirely before ptr, skip it
        if e < ptr:
            continue

        # If there's a gap before this interval, fill with UNKNOWN
        if s > ptr:
            gap_s = ptr
            gap_e = s - 1
            out.append((gap_s, gap_e, "UNKNOWN"))
            ptr = s
        
        # Now ptr <= s or ptr == s
        # take the portion of [s,e] starting from ptr (handles overlap)
        take_s = max(s, ptr)
        take_e = e
        out.append((take_s,take_e, brand))
        ptr = take_e + 1
        if ptr > MAX_OFFSET:
            break
    
    # if anything remains aftyer processing the intervals, fill with UNKNOWN
    if ptr <= MAX_OFFSET:
        out.append((ptr, MAX_OFFSET, "UNKNOWN"))
    
    # Helper function to format the full 16 digit number: BIN + 0-padded 10 digit offset
    def fmt(bin6, offset):
        return f"{bin6}{offset:010d}"
    
    # Produce sortedf output lines
    lines_out = []
    for (s, e, brand) in out:
        lines_out.append(f"{fmt(bin6,s)},{fmt(bin6, e)},{brand}")
    
    return "\n".join(lines_out)

# Example usage / test:
input_data = """777777
2
1000000000,3999999999,VISA
4000000000,5999999999,MASTERCARD
"""
print(card_range_obfuscation(input_data))