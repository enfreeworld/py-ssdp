import ssdp.device
import time


def main():
    myManager = ssdp.device.DeviceManager()
    myDevice = ssdp.device.Device(name="bumblebee",
                                  domain_name='botqueue-com',
                                  device_type='Basic',
                                  version='1')
    assert isinstance(myDevice, ssdp.device.Device)
    assert isinstance(myManager, ssdp.device.DeviceManager)

    myManager.add_device(myDevice)

    while True:
        time.sleep(10)


if __name__ == "__main__":
    main()