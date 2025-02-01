from livepeer import Livepeer
import json 

Livepeer_Connect = Livepeer(
    api_key="0a6bcfa4-b3c7-4a4e-b41b-4515d76799d3",
)

res = Livepeer_Connect.playback.get(id="8185pgj6dix7e7nv")

# Header Url 
if res.playback_info is not None:
    # handle response
    print(res.playback_info)
    
	
    pass