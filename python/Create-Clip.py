from livepeer import Livepeer

s = Livepeer(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.stream.create_clip(request={
    "playback_id": "eaw4nk06ts2d0mzb",
    "start_time": 1587667174725,
    "end_time": 1587667174725,
    "name": "My Clip",
    "session_id": "de7818e7-610a-4057-8f6f-b785dc1e6f88",
})

if res.data is not None:
    # handle response
    pass