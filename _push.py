"""Create GitHub repo and push the LaTeX resume."""
import subprocess, os

REPO = "/Users/amac/MechInterpLab/Resume"

def run(cmd, **kw):
    r = subprocess.run(cmd, cwd=REPO, capture_output=True, text=True, **kw)
    out = (r.stdout + r.stderr).strip()
    print(f"  {cmd[0]} {cmd[1] if len(cmd)>1 else ''} -> {out[:100]}")
    return r

# Write .gitignore
with open(os.path.join(REPO, ".gitignore"), "w") as f:
    f.write(".DS_Store\n*.aux\n*.log\n*.out\n*.synctex.gz\n"
            "*.fls\n*.fdb_latexmk\n*.toc\n")

# Init git
run(["git", "init", "-q"])
run(["git", "config", "user.email", "ajaykumar.career@gmail.com"])
run(["git", "config", "user.name", "ajaykumarsoma"])

# Remove remote if exists, then re-add
run(["git", "remote", "remove", "origin"])
run(["git", "remote", "add", "origin",
     "https://github.com/ajaykumarsoma/resume.git"])

# Stage and commit
run(["git", "add", "-A"])

msg = ("init: LaTeX resume for AI Safety / LLM Fine-Tuning / RLHF roles\n\n"
       "Jake's Resume template with full content:\n"
       "- Email: ajaykumar.career@gmail.com\n"
       "- Summary: 18yr IT exp, MTech VNIT Nagpur, safety/alignment focus\n"
       "- Ashley Furniture AI Engineer experience (fill in real metrics)\n"
       "- 33 independent research projects in 4 categories:\n"
       "    1. Manufacturing AI Safety: ManufacturingRAG, SupplyChainGuardrails,\n"
       "       ProductDescriptionAlignment, LLMRiskScorer\n"
       "    2. Alignment & Safety: RewardModeling, GRPO, DPO, Guardrails, EvalFramework\n"
       "    3. Fine-Tuning & Inference: LoRA, SFT, KD, PTQ, SLERP, SpecDec, RAG, JSON\n"
       "    4. Mechanistic Interpretability: 13 experiments\n"
       "- Skills and Education sections\n"
       "Compile: Overleaf (pdfLaTeX) or local pdflatex")

run(["git", "commit", "-m", msg])

# Create GitHub repo
print("\nCreating GitHub repo...")
r = subprocess.run(
    ["gh", "repo", "create", "ajaykumarsoma/resume",
     "--public",
     "--description",
     ("LaTeX CV for AI Safety / LLM Fine-Tuning / RLHF roles | "
      "MTech VNIT Nagpur | 18yr IT | 33 ML research projects | "
      "ajaykumar.career@gmail.com")],
    cwd=REPO, capture_output=True, text=True
)
print(" ", (r.stdout + r.stderr).strip()[:150])

# Push
print("\nPushing...")
r = subprocess.run(
    ["git", "push", "-u", "origin", "main", "--force"],
    cwd=REPO, capture_output=True, text=True
)
print((r.stdout + r.stderr).strip()[:200])
print("\nDONE")
print("Repo: https://github.com/ajaykumarsoma/resume")
