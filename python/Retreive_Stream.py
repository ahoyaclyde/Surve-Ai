from livepeer import Livepeer

s = Livepeer(
    api_key="0a6bcfa4-b3c7-4a4e-b41b-4515d76799d3",
)

res = s.stream.get(id="6e5928e0-e309-42b2-baca-8e2c8aa5090d")

if res.stream is not None:
    # handle response
    print(res.stream)
    pass