"""
Problem 2: A5/1 Code


i.e., 0b1010101010101010101
      0b1100110011001100110011
      0b11100001111000011110000  32
"""

import sys

L1, L2, L3 = 19, 22, 23
MASK1, MASK2, MASK3 = (1 << L1) - 1, (1 << L2) - 1, (1 << L3) - 1


MSB_TAPS_X = [13, 16, 17, 18]
MSB_TAPS_Y = [20, 21]
MSB_TAPS_Z = [7, 20, 21, 22]

MSB_CLK_X, MSB_CLK_Y, MSB_CLK_Z = 8, 10, 10


def my_to_lsb_positions(length, msb_indices):
   return [length - 1 - idx for idx in msb_indices]


def my_to_lsb_position(length, msb_idx):
    return length - 1 - msb_idx


def bit(value, pos_lsb):
    return (value >> pos_lsb) & 1


def majority(a, b, c):
    return (a & b) | (a & c) | (b & c)


def clock_right_feed_msb(state, length, taps_lsb):
    
    fb = 0
    for t in taps_lsb:
        fb ^= bit(state, t)
    state = (state >> 1) | (fb << (length - 1))
    return state


def parse_value(s):
    s = s.strip().lower()
    if s.startswith("0b"):
        return int(s[2:], 2)
    elif s.startswith("0x"):
        return int(s[2:], 16)
    return int(s)


def to_bin(v, width):
    b = bin(v)[2:]
    if len(b) < width:
        return "0" * (width - len(b)) + b
    return b[-width:]


def generate(x, y, z, n):
 
    state_x, state_y, state_z = x, y, z
    out = []

    #These will be Converted MSB indices to LSB positions
    X_taps = my_to_lsb_positions(L1, MSB_TAPS_X)
    Y_taps = my_to_lsb_positions(L2, MSB_TAPS_Y)
    Z_taps = my_to_lsb_positions(L3, MSB_TAPS_Z)
    X_clk = my_to_lsb_position(L1, MSB_CLK_X)
    Y_clk = my_to_lsb_position(L2, MSB_CLK_Y)
    Z_clk = my_to_lsb_position(L3, MSB_CLK_Z)

    for _ in range(n):
        maj = majority(bit(state_x, X_clk), bit(state_y, Y_clk), bit(state_z, Z_clk))

        if bit(state_x, X_clk) == maj:
            state_x = clock_right_feed_msb(state_x, L1, X_taps)
        if bit(state_y, Y_clk) == maj:
            state_y = clock_right_feed_msb(state_y, L2, Y_taps)
        if bit(state_z, Z_clk) == maj:
            state_z = clock_right_feed_msb(state_z, L3, Z_taps)

        out_bit = (state_x & 1) ^ (state_y & 1) ^ (state_z & 1)
        out.append(str(out_bit))

    keystream = "".join(out)
    return keystream, state_x, state_y, state_z


def main():
    if len(sys.argv) != 5:
        print("My usage: python a51.py <X> <Y> <Z> <N>")
        print("The example is:")
        print("python a51.py 0b1010101010101010101 0b1100110011001100110011 0b11100001111000011110000 32")
        sys.exit(0)

    X = parse_value(sys.argv[1]) & MASK1
    Y = parse_value(sys.argv[2]) & MASK2
    Z = parse_value(sys.argv[3]) & MASK3
    N = int(sys.argv[4])

    ks, Xf, Yf, Zf = generate(X, Y, Z, N)

    # Print four lines 
    print(ks)
    print(to_bin(Xf, L1))
    print(to_bin(Yf, L2))
    print(to_bin(Zf, L3))


if __name__ == "__main__":
    main()
