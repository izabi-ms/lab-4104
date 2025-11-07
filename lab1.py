total_bw = int(input("Enter total bandwidth (in kHz): "))
ch_bw = int(input("Enter channel bandwidth (in kHz): "))
total_channels = total_bw // (2 * ch_bw)
control_bw = 1000   # 1 MHz = 1000 kHz
control_channels = control_bw // (2 * ch_bw)
voice_channels = total_channels - control_channels

for n in [4, 7, 12]:
    print("Reuse:", n)
    print("Total channels per cell:", total_channels // n)
    print("Control per cell:", control_channels // n)
    print("Voice per cell:", voice_channels // n)
