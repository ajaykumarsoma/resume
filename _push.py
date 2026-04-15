import subprocess
REPO = "/Users/amac/MechInterpLab/Resume"
def run(cmd):
    r = subprocess.run(cmd, cwd=REPO, capture_output=True, text=True)
    out = (r.stdout + r.stderr).strip()[:160]
    print(f"  {' '.join(cmd[:3])} -> {out}")
run(["git", "add", "-A"])
run(["git", "commit", "-m",
     "improve: gap-analysis fixes — metrics, red-team framing, section restructure\n\n"
     "Summary: '33 experiments' -> 30; add adversarial testing to specialisation list\n"
     "Ashley bullets: add ~3000 SKUs, ~35% failure reduction, 8 vendor tools, 12 failure modes\n"
     "Guardrails: add red-team / adversarial jailbreak testing framing\n"
     "Fine-Tuning: break dense list into 4 scannable bullets with key metrics\n"
     "MI: lead with L7-L8 convergence finding across 4 independent methods\n"
     "Skills Stack: replace 'Apple M4 MPS' with PEFT, W&B, Git/GitHub\n"
     "Section header: '33 projects' -> 30 (accurate count)"])
run(["git", "push"])
print("DONE — https://github.com/ajaykumarsoma/resume")
