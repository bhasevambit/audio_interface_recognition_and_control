import pyaudio

pa = pyaudio.PyAudio()

print("\n=== All Audio Devices ===")

for host_index in range(0, pa.get_host_api_count()):
    print(pa.get_host_api_info_by_index(host_index))
    for device_index in range(
            0, pa.get_host_api_info_by_index(host_index)['deviceCount']
    ):
        print(
            pa.get_device_info_by_host_api_device_index(
                host_index,
                device_index
            )
        )
