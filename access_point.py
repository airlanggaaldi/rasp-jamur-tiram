import network

# sta_if = network.WLAN(network.STA_IF)
# print(sta_if.active())

ap_if = network.WLAN(network.AP_IF)
print(ap_if.active())