try:
    f1 = open("data1.txt", "w")
    f2 = open("data2.txt", "w")
    try:
        f1.write("First file content\n")
        f2.write("Second file content\n")
        print("files written successfully")
    finally:
        f1.close()
        f2.close()
except Exception as e:
    print(f"An error occurred: {e}")