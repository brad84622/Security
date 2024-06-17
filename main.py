import ctypes


#python top with c lib api



if __name__ == "__main__":
    print("python start")

    lib = ctypes.CDLL("/Users/bradchen/vscode/Security/libexample.so")

    lib.hello()
    print(lib.add(5,6))