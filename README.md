# py-flamework-api-multiclient

Python bindings for Flamework-derived APIs with support for multiple parallel requests (using grequest).

## Installation

You can install this by either cloning this repository and running

```
$> python setup.py install
```

## Example

`flamework.api.multiclient` subclasses `flamework.api.client` and exports
a single additional `execute_methods` that takes a list of (method, args) tuples
and returns a generator (of standard `execute_method` responses.

```
import flamework.api.multiclient
import pprint

HOSTNAME='api.collection.cooperhewitt.org'
ENDPOINT='/rest'

TOKEN='S33KR3T'

api = flamework.api.multiclient.OAuth2(ACCESS_TOKEN, hostname=HOSTNAME, endpoint=ENDPOINT)

reqs = (
    ('cooperhewitt.labs.whatWouldMicahSay', {}),
    ('cooperhewitt.objects.getRandom', {'has_image': 1}),
    ('cooperhewitt.labs.whatWouldMicahSay', {}),
    ('cooperhewitt.objects.getRandom', {'has_image': 1}),
    ('cooperhewitt.labs.whatWouldMicahSay', {}),
    ('cooperhewitt.objects.getRandom', {'has_image': 1}),
)

for rsp in api.execute_methods(reqs):
    print pprint.pformat(rsp)

rsp = api.execute_method(*req[1]):
print pprint.pformat(rsp)

```
	
## See also

* [py-flamework-api](https://github.com/cooperhewitt/py-flamework-api)

