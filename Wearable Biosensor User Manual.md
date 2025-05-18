---
Date: May 18, 2025
tags:
  - EmbeddedSystems
---
This is the user manual for the wearable biosensor prototype. The kit should contain the following:
1. A modified plastic container box with sensors attached to its insides.
2. A belt strap and buckle for wearing unto the body.
3. An ECG cable with electrodes.

## Powering the Device
In order to power the device, the user must remove the green paper cap from the white 5V jumper pin and attach it to the brown female jumper wire.

Make sure that the other side of this brown jumper pin is attached to the GND pin on the power supply module. Also check if the red jumper wire is connected to the power supply module's 5V pin.

When properly connected, three red LED bulbs should light up.

One should be from the ESP32-C3 Super Mini power indicator LED bulb.

The second should be on the AD8232 Heart Rate Sensor indicator LED bulb which is in the center of a heart-shaped drawing. This can be found on the back side of the device sitting roughly 45 degrees from the bottom. At times, this might not appear to turn on at all or may appear to lose its light gradually. This can partly be attributed to lose connection to the power pin or reduced current traveling toward the sensor module. Most of the time though, this sensor still works even with the red bulb turned off.

Third, the final one should be found on the bottom of the device which is the MAX30102 IR Oximeter. If this does not turn on, try to press on the jumper wires connecting to this sensor and then restart the device by unplugging and replugging the white 5V jumper wire and the brown GND wire. The device WILL NOT WORK AT ALL if this sensor does not turn on.

To turn off the device, pull away the white and brown jumper wires and make sure to attach the green cap on the white jumper pin.

## Wearing the Device
To wear the device, the user should have an assistant place the biosensor on the forearm. The GY-906 IR thermal sensor should be facing distal from the body, pointing toward the wrist.

Afterward, the device should be held in place with a modified belt strap with the attached buckle. It is important to have an assistant to tighten this to the right level in order to reduce the chances of the device slipping out during intense physical activity.

Once held in place, the user should then wear the finger gloves on the index and middle fingers. The choice between the black and red wires to each finger does not matter. Any finger can be worn with either one. But do make sure to have the metal parts touch the fingers' skin in order to have a proper reading. Fingernails do not count.

Lastly, the ECG cable should be connected to the 3.5mm jack. Then place the ECG cable under the arm sleeve and toward the abdomen. Take not of the R and L markings.

### Wearing the ECG Electrodes
There are three ECG electrodes. These should sit on the fleshy portion of the body, and not on top of bones.

The electrode with the L marking should be placed on the chest area in the same level as the heart. You may place this over the pectoralis minor muscles.

Likewise, you may place one of the R electrodes on the opposite pectoralis minor muscles.

For the other R electrode, place this on the abdominal muscles under the top R electrode. Be sure to place this on a spot that is not covered by the rib cage.

## Recharging the Device
To recharge the device, use a microUSB cable and attach it into the power supply unit attached on the cover of the casing.

## Warnings
1. The device uses an exposed lithium-polymer battery which presents a fire hazard. DO NOT, IN ANY CIRCUMSTANCE, DISPOSE THE DEVICE IN FIRE.
2. The device is also not waterproof. Please avoid using the device where there is a chance for water to splash into the open holes near the electronics.
3. Jumper wires may come off loose at times. Please refrain from making sudden jerky movements while removing pins or powering/de-powering the device.