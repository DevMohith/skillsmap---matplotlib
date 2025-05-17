#   mY first data visualization using matplotlib

import matplotlib.pyplot as plt


fig, ax = plt.subplots(figsize=(10, 6))
center_text = "Mohith Tummala"
ax.text(0.5, 0.5, center_text, fontsize=14, ha='center', va='center', fontweight='bold',
         bbox=dict(facecolor='lightgreen', edgecolor='black', boxstyle='round,pad=1'))

branches = {
    "AI/ML": {
        "pos": (0.2, 0.9),
        "details": [
            "🔹 Built AI agents for automation",
            "🔹 Developed and Trained ML prediction, classification, Custom models",
            "🔹 Integrated LLM's into GenAI application",
            "🔹 Helped my team to increase their productivity my automating their tasks",
        ]
    },
     "Full Stack Dev": {
        "pos": (0.8, 0.9),
        "details": [
            "🔹 Experienced in JavaScript, React, Vue for client UI development",
            "🔹 Professional Backend Developer with Node.js & Python",
            "🔹 Built enterprise-grade automation applications"
        ]
    },
    "Cloud & DevOps": {
        "pos": (0.5, 0.15),
        "details": [
            "🔹 Containerized apps using Docker",
            "🔹 Deployed applications on AWS App Runner, GCP Appengine and Cloudrun",
            "🔹 Deployed application on ",
            "🔹 Built CI/CD pipelines for many Applications"
        ]
    }
}


for title, content in branches.items():
    x, y = content["pos"]
    ax.plot([0.5, x], [0.5, y], 'k-', lw=1)
    ax.text(x, y, title, fontsize=12, ha='center', va='center',
            bbox=dict(facecolor='lightgreen', edgecolor='black', boxstyle='round,pad=0.7'))
    for i, detail in enumerate(content["details"]):
        ax.text(x, y - (i + 1) * 0.05, detail, fontsize=10, ha='center', va='top')


ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')
plt.title("Hey there!! I am a mid level T-SHAPED Software Engineer with wide range of skill is AI/ML, Full Stack Development, Cloud, Generative AI", fontsize=10)
plt.tight_layout()


plt.savefig("skills_map.png", dpi=300, bbox_inches='tight')
plt.show()
