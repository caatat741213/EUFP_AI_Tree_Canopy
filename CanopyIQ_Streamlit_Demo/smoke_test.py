from pathlib import Path
import json
import pandas as pd

BASE = Path(__file__).resolve().parent
idx = pd.read_csv(BASE / 'data/canopyiq_index.csv')
model = pd.DataFrame(json.load(open(BASE / 'data/model_results.json', encoding='utf-8')))
meta = json.load(open(BASE / 'data/metadata.json', encoding='utf-8'))
geo = json.load(open(BASE / 'data/canopyiq_communities.geojson', encoding='utf-8'))

assert len(idx) == 51, len(idx)
assert idx['pc'].nunique() == 51
assert len(geo['features']) == 51
assert set(idx['pc']) == {f['properties']['pc'] for f in geo['features']}
assert meta['communities_with_tree_records'] == 52
assert meta['unranked_due_to_missing_backlog'] == ['SOUTH PLAINS']
pooled = model.loc[model.model.str.startswith('P:')].iloc[0]
assert float(pooled.roc_auc) == 0.835
assert float(pooled.pr_auc) == 0.692
assert float(pooled.f1) == 0.589
print('PASS: CanopyIQ demo data and current model metrics are internally consistent.')
