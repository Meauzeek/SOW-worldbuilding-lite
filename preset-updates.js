// Apply a named author update once, keeping unrelated user records intact.
export function applyPresetUpdate(data,patch){
 if(data.appliedUpdates?.includes(patch.id))return false;
 for(const update of patch.countries){const country=data.countries.find(c=>c.id===update.id);if(country)Object.assign(country,structuredClone(update));}
 for(const update of patch.cityUpdates||[]){const city=data.cities.find(c=>c.id===update.id);if(city)Object.assign(city,structuredClone(update));}
 for(const city of patch.cities)if(!data.cities.some(c=>c.id===city.id))data.cities.push(structuredClone(city));
 if(data.boundaries)for(const feature of patch.boundaries){const i=data.boundaries.features.findIndex(f=>f.properties.id===feature.properties.id);if(i>=0)data.boundaries.features[i]=structuredClone(feature);}
 data.appliedUpdates=[...(data.appliedUpdates||[]),patch.id];return true;
}
