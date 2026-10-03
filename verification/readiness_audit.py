from pathlib import Path
import yaml
root=Path(__file__).resolve().parents[1]
required=['agent.yaml','SOUL.md','README.md','EXPLAINABILITY.md']
for f in required: assert (root/f).exists(), f"Missing {f}"
a=yaml.safe_load((root/'agent.yaml').read_text())
for s in a['skills']: assert (root/'skills'/s/'SKILL.md').exists(), s
for t in a['tools']: assert (root/'tools'/f'{t}.yaml').exists(), t
print('READINESS AUDIT: PASS')
print('Checked core manifest, skills, tools, and documentation.')
