from pathlib import Path
import yaml
ROOT=Path(__file__).resolve().parents[1]
def test_manifest_and_skills():
    a=yaml.safe_load((ROOT/'agent.yaml').read_text()); assert a['spec_version']=='0.1.0'
    for s in a['skills']:
        p=ROOT/'skills'/s/'SKILL.md'; t=p.read_text(); assert t.startswith('---\n') and '\nname:' in t and '\ndescription:' in t
    for t in a['tools']: assert (ROOT/'tools'/f'{t}.yaml').exists()
