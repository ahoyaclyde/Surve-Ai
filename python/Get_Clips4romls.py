from livepeer import Livepeer

s = Livepeer(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.stream.get_clips(id="<id>")

if res.data is not None:
    # handle response
    pass