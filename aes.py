#input
    #in : 16 byte array , will translate to 2d array
    # -----------------------------
    # | in0 | in4 | in8  | in12 |
    # -----------------------------
    # | in1 | in5 | in9  | in13 |
    # -----------------------------
    # | in2 | in6 | in10 | in14 |
    # -----------------------------
    # | in3 | in7 | in11 | in15 |
    # -----------------------------

    #s : state , 2d array 
    # 4x4 State Array 
    # -----------------------------
    # | s0,0 | s0,1 | s0,2 | s0,3 |
    # -----------------------------
    # | s1,0 | s1,1 | s1,2 | s1,3 |
    # -----------------------------
    # | s2,0 | s2,1 | s2,2 | s2,3 |
    # -----------------------------
    # | s3,0 | s3,1 | s3,2 | s3,3 |
    # -----------------------------

#Cipher()
    #1. SubBytes
    #2. ShiftRows
    #3. MixColumns
    #4. AddRoundKey


if __name__ == "__main__":
    # 示例输入的十六进制字符串
    hex_string = "00112233445566778899aabbccddeeff"

    # 确保输入字符串的长度是32（每个十六进制字符占4位，总共128位）
    assert len(hex_string) == 32, "Hex string length must be 32."

    # 将十六进制字符串按字节拆分成列表
    aes_in = [hex_string[i:i+2] for i in range(0, len(hex_string), 2)]

    # 构建4x4状态数组
    state_array = [ [0 for _ in range(4)] for _ in range(4) ]

    #00 
    #01
    #02 
    #03

    for j in range(4):
        for i in range(4):
            state_array[i][j] = aes_in[i*4+j]

    print("4x4 State Array:")
    for row in state_array:
        print(" | ".join(row))
        print("---------------------")
    
    