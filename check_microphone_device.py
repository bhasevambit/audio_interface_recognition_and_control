import pyaudio

pa = pyaudio.PyAudio()

print("\nDevice count : ", pa.get_device_count(), "\n")

for i in range(pa.get_device_count()):
    # print(pa.get_device_info_by_index(i))
    dev_info = pa.get_device_info_by_index(i)
    print("index:", dev_info["index"], " ", dev_info["name"])

print("")
