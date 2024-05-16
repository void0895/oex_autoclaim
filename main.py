import proc

# data
data='{"domain":{"name":"Agiex","version":"1","chainId":"1","verifyingContract":"0x0000000000000000000000000000000000000000"},"types":{"AGIEX":[{"name":"address","type":"string"}]},"value":{"address":"0xE039880CfF560AdBf0dcE1732732D0a1d09bc267","signer":"0xE039880CfF560AdBf0dcE1732732D0a1d09bc267","v":27,"r":"0x72258281b451880663e588695890ffbd2bc3e4886eca1fb7e8869f5fdf3ae564","s":"0x035ca33167973939b88924ef703a0ba787bd2c2a38ed3205d62971abcc193479"},"signature":"0x72258281b451880663e588695890ffbd2bc3e4886eca1fb7e8869f5fdf3ae564035ca33167973939b88924ef703a0ba787bd2c2a38ed3205d62971abcc1934791b","version":{"app":1,"build":12}}'
info='{"domain":{"name":"openex.network","version":"1","chainId":"7798","verifyingContract":"0x0000000000000000000000000000000000000000"},"types":{"OEX":[{"name":"request","type":"uint256"}]},"value":{"request":1715488550939,"signer":"0xE039880CfF560AdBf0dcE1732732D0a1d09bc267","v":28,"r":"0x5fb7528faa811fe3fc9e608b5fe1c99ea4c5efb819fa830023c82377c0c46d15","s":"0x6af4692e493f60c0a1ebd2cfdf4215984c03c40f6dd0e533c3fea6b308a1ed4b"},"signature":"0x5fb7528faa811fe3fc9e608b5fe1c99ea4c5efb819fa830023c82377c0c46d156af4692e493f60c0a1ebd2cfdf4215984c03c40f6dd0e533c3fea6b308a1ed4b1c","version":{"app":1,"build":12}}'
# data2
data2='{"domain":{"name":"Agiex","version":"1","chainId":"1","verifyingContract":"0x0000000000000000000000000000000000000000"},"types":{"AGIEX":[{"name":"address","type":"string"}]},"value":{"address":"0x4eC3290A8bbb89A4e4D9500c8E07fd34eE394bcA","signer":"0x4eC3290A8bbb89A4e4D9500c8E07fd34eE394bcA","v":28,"r":"0xcea04fb919f3948daf94381f9b432b24407903bdd497b44df9a6828c87f817b9","s":"0x2b00cec16f078e2c2c329224e55fd9e306bc38c0d1712f6c35f87f31456346ec"},"signature":"0xcea04fb919f3948daf94381f9b432b24407903bdd497b44df9a6828c87f817b92b00cec16f078e2c2c329224e55fd9e306bc38c0d1712f6c35f87f31456346ec1c","version":{"app":1,"build":12}}'
info2='{"domain":{"name":"openex.network","version":"1","chainId":"7798","verifyingContract":"0x0000000000000000000000000000000000000000"},"types":{"OEX":[{"name":"request","type":"uint256"}]},"value":{"request":1715488866045,"signer":"0x4eC3290A8bbb89A4e4D9500c8E07fd34eE394bcA","v":27,"r":"0x36099c30c8c4676bda39e01ea63c8bb604f643ce78870083711dcfeee5ed417a","s":"0x3d2fe487c74d242bbbffd9794036c938820925222c75cb59f39e7c5fece41f57"},"signature":"0x36099c30c8c4676bda39e01ea63c8bb604f643ce78870083711dcfeee5ed417a3d2fe487c74d242bbbffd9794036c938820925222c75cb59f39e7c5fece41f571b","version":{"app":1,"build":12}}'
# auth
auth1 = proc.auth(data)
auth2 = proc.auth(data2)
# info and reward
info = proc.info(data=info)
print(f"ID : {info.get('email')}\nSatoshi Airdrop : {float(info.get('satoshiOEX')) / 100000000:2f}\nOEX Airdrop : {info.get('longUSDT')}")
print("==> ", end='')
proc.reward(auth1)
info2 = proc.info(data=info2)
print(f"ID : {info2.get('email')}\nSatoshi Airdrop : {float(info2.get('satoshiOEX')) / 100000000:2f}\nOEX Airdrop : {info2.get('longUSDT')}")
print("==> ", end='')
proc.reward(auth2)


