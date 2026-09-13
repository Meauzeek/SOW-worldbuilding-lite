"""Standard-library checks: archive size, identity references, no media/elevation."""
from pathlib import Path
import json
r=Path(__file__).resolve().parents[1]
files=[p for p in r.rglob('*') if p.is_file() and '.git' not in p.relative_to(r).parts]
size=sum(p.stat().st_size for p in files)
assert size<100_000_000,f'Repository files exceed 100 MB: {size}'
assert not [p for p in files if p.suffix.lower() in {'.png','.jpg','.jpeg','.webp','.tif','.tiff','.f32','.ttf','.woff','.woff2','.mp4','.pdf'}]
countries=json.loads((r/'data/countries.json').read_text(encoding='utf8'));cities=json.loads((r/'data/cities.json').read_text(encoding='utf8'))
ids=[c['id'] for c in countries+cities];assert len(set(ids))==len(ids)
country_ids={c['id'] for c in countries}
for c in cities:
 assert c['countryId'] in country_ids
 assert len(c['coordinates'])==2 and -180<=c['coordinates'][0]<=180 and -90<=c['coordinates'][1]<=90
for c in countries:assert not c.get('parentId') or c['parentId'] in country_ids
def scan(x):
 if isinstance(x,dict):
  assert not ({'media','elevation','elevationSource','customDem'} & set(x))
  for v in x.values():scan(v)
 elif isinstance(x,list):
  for v in x:scan(v)
 elif isinstance(x,str):assert not x.startswith('data:image/')
for p in (r/'data').iterdir():scan(json.loads(p.read_text(encoding='utf8')))
geo=json.loads((r/'data/boundaries.geojson').read_text(encoding='utf8'))
assert {f['properties']['id'] for f in geo['features']}==country_ids
print(f'PASS: {len(countries)} countries/territories, {len(cities)} cities; {size/1_000_000:.2f} MB; no image/elevation binaries.')
