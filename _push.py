import subprocess
REPO = "/Users/amac/MechInterpLab/Resume"
def run(cmd):
    r = subprocess.run(cmd, cwd=REPO, capture_output=True, text=True)
    print(f"  {' '.join(cmd[:3])} -> {(r.stdout+r.stderr).strip()[:120]}")
run(["git","add","-A"])
run(["git","commit","-m",
     "update: fill in full employment history and education\n\n"
     "Experience:\n"
     "  2022-present  Ashley Furniture — Lead Engineer, AI\n"
     "  2016-2021     TCS — IT Analyst / Technical Lead\n"
     "  2011-2016     Genpact — Senior Software Engineer\n"
     "  2006-2010     Infosys — Software Engineer\n"
     "Education:\n"
     "  MTech Applied AI, VNIT Nagpur, 2026\n"
     "  BTech ECE, JNTU, 2006\n"
     "Summary updated: Lead Engineer (AI), 18yr IT across Infosys/Genpact/TCS/Ashley"])
run(["git","push"])
print("DONE — https://github.com/ajaykumarsoma/resume")
