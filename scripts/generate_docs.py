"""Regenerate AI-readable country chapters from this repository's JSON records."""
from pathlib import Path
import json
r=Path(__file__).resolve().parents[1]
countries=json.loads((r/'data/countries.json').read_text(encoding='utf8'))
cities=json.loads((r/'data/cities.json').read_text(encoding='utf8'))
names={c['id']:c['name'] for c in countries}
def text(v):return str(v if v is not None else '未设定').replace('|','／').replace('\n',' ')
index=['# 国家与地区索引','',f'共 {len(countries)} 个国家与地区，{len(cities)} 座城市。','', '| 国家 / 地区 | 英文名 | 首都 / 首府 | 城市数 |','|---|---|---|---|']
for c in countries:
 own=[x for x in cities if x['countryId']==c['id']]
 index.append(f"| [{text(c['name'])}](countries/{c['id']}.md) | {text(c.get('englishName'))} | {text(c.get('capital'))} | {len(own)} |")
 lines=[f"# {c['name']}",'',f"记录 ID：`{c['id']}`",'', '## 国家 / 地区设定','']
 for key,label in [('fullName','全称'),('englishName','英文名称'),('localName','本地名称'),('localLanguage','本地语言'),('localRomanization','本地名称拉丁转写'),('abbreviation','简称'),('capital','首都 / 首府'),('population','人口（人）'),('gdpHundredMillionUSD','GDP（亿美元）'),('realName','现实对应'),('presetSovereignty','政治地位')]:
  if c.get(key) is not None:lines.append(f"- {label}：{text(c[key])}")
 if c.get('parentId'):lines.append('- 上级归属：'+names.get(c['parentId'],c['parentId']))
 if c.get('constructedLanguage'):lines.append('- 语言说明：'+text(c['constructedLanguage']))
 lines+=['',c.get('notes',''),'','人口及经济数据口径：'+text(c.get('demographics',{}).get('kind','原有设定；未另行标识')),'','## 城市设定','']
 for city in own:
  lines += [f"### {city['name']}",'',f"记录 ID：`{city['id']}`",'']
  for key,label in [('englishName','英文 / 外文名'),('localName','本地名称'),('localLanguage','语言'),('realName','现实原型'),('population','人口（人）'),('gdpHundredMillionUSD','GDP（亿美元）'),('polityType','管辖类型')]:
   if city.get(key) is not None:lines.append(f"- {label}：{text(city[key])}")
  if city.get('nameEtymology'):lines.append('- 名称由来：'+text(city['nameEtymology']))
  if city.get('featuredReason'):lines.append('- 星标依据：'+text(city['featuredReason']))
  for link in city.get('relatedCharacters',[]):lines.append('- 关联角色：'+text(link['name'])+' · '+text(link.get('relation',''))+' · '+text(link.get('notes',''))+' · 来源：'+text(link.get('source','')))
  lines.append('- 坐标（经度、纬度）：'+text(city['coordinates']))
  if city.get('capital'):lines.append('- 首都 / 首府：'+('地区首府' if city.get('capitalRole')=='regional' else '是'))
  if city.get('hostCountryId'):lines.append('- 地理所在国家：'+names.get(city['hostCountryId'],city['hostCountryId']))
  if city.get('featured'):lines.append('- 小说重要地点：是')
  lines.append('- 计入国家汇总：'+('否' if city.get('includeInNationalTotals') is False else '是'))
  for n in city.get('nativeNames',[]):lines.append(f"- 其他本地名称：{text(n.get('name'))}（{text(n.get('language'))}）")
  lines += ['',city.get('notes',''),'']
 (r/'docs/countries'/f"{c['id']}.md").write_text('\n'.join(lines)+'\n',encoding='utf8')
(r/'docs/COUNTRY_INDEX.md').write_text('\n'.join(index)+'\n',encoding='utf8')
print(f'Generated {len(countries)} country chapters.')
