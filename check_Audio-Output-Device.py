import pyaudio

pa = pyaudio.PyAudio()

print("\n=== Audio Output Devices (Speaker) ===")

for i in range(pa.get_device_count()):
    dev_info = pa.get_device_info_by_index(i)

    # print("maxOutputChannels:", dev_info["maxOutputChannels"])

    if dev_info["maxOutputChannels"] != 0:
        print(
            "index:",
            dev_info["index"],
            " ",
            dev_info["name"],
            "( IN-Ch:",
            dev_info["maxInputChannels"],
            "/ OUT-Ch:",
            dev_info["maxOutputChannels"],
            ")"
        )

print("")
