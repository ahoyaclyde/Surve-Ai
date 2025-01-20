from livepeer import Livepeer

s = Livepeer(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.stream.terminate(id="<id>")

if res is not None:
    # handle response
    pass