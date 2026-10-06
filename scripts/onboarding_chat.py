#!/usr/bin/env python3
"""Render the illustrative onboarding-conversation image used in the README.

Not a screenshot of any product: a neutral mock of the conversation the
Onboarding skill drives, using the fictional demo-vault persona. Writes one
HTML file per language; render each to PNG with headless Chrome:

    python3 scripts/onboarding_chat.py /tmp/out
    google-chrome --headless=new --hide-scrollbars --force-device-scale-factor=2 \
        --window-size=1200,880 --screenshot=docs/assets/onboarding-chat.png /tmp/out/onboarding-chat.html
"""
import sys
from pathlib import Path

TEXT = {
    "": {
        "title": "Your AI assistant · connected to the vault",
        "tag": "Illustrative conversation",
        "turns": [
            ("u", "onboarding"),
            ("a", "This vault is brand new, so let's set it up by talking. <b>Tell me who you are and what you do</b> — or just paste your CV / LinkedIn and I'll extract it."),
            ("u", "<i>[pastes CV]</i> Also: I keep things short, and nothing goes out in my name before I read it."),
            ("a", "Here is the draft of <code>ME.md</code>:<div class='draft'><b>Marina Duarte</b> — product &amp; data consultant · MSc student<br>Tone: concise and direct<br>Non-negotiable: nothing sent without her review</div>Save it?"),
            ("u", "Yes. This week it's the Órbita dashboard, my course, and the thesis."),
            ("a", "I see <b>3 areas</b>: <code>orbita</code> · <code>estudio</code> · <code>mestrado</code>. Who are the people you deal with most, and which decisions have you had to re-explain lately?"),
        ],
        "done": "Written to your vault — nothing edited by hand",
        "files": ["ME.md", "6 project hubs", "8 people · 3 orgs", "4 decisions", "7 tasks on the board"],
        "last": "Your AIOS is up. Tomorrow the briefing arrives on its own.",
    },
    ".pt-BR": {
        "title": "Seu assistente de IA · conectado ao vault",
        "tag": "Conversa ilustrativa",
        "turns": [
            ("u", "onboarding"),
            ("a", "Este vault é novo, então vamos configurar conversando. <b>Me conta quem você é e o que você faz</b> — ou cole seu CV / LinkedIn que eu extraio."),
            ("u", "<i>[cola o CV]</i> E mais: sou direta, e nada sai em meu nome sem eu ler."),
            ("a", "Rascunho do <code>ME.md</code>:<div class='draft'><b>Marina Duarte</b> — consultora de produto e dados · mestranda<br>Tom: conciso e direto<br>Inegociável: nada enviado sem revisão dela</div>Posso gravar?"),
            ("u", "Pode. Esta semana é o painel da Órbita, meu curso e a dissertação."),
            ("a", "Vejo <b>3 áreas</b>: <code>orbita</code> · <code>estudio</code> · <code>mestrado</code>. Quem são as pessoas com quem você mais interage, e que decisões você teve que re-explicar ultimamente?"),
        ],
        "done": "Gravado no seu vault — nada editado na mão",
        "files": ["ME.md", "6 hubs de projeto", "8 pessoas · 3 orgs", "4 decisões", "7 tarefas no quadro"],
        "last": "Seu AIOS está de pé. Amanhã o briefing chega sozinho.",
    },
}

CSS = """
*{box-sizing:border-box;margin:0}
body{background:#14151a;font:17px/1.5 system-ui,-apple-system,"Segoe UI",sans-serif;color:#e6e6eb;padding:36px}
.win{background:#1e1f26;border:1px solid #34363f;border-radius:16px;overflow:hidden;max-width:1128px;margin:auto}
.bar{display:flex;align-items:center;gap:10px;padding:14px 20px;border-bottom:1px solid #34363f;color:#a9abb6;font-size:15px}
.dot{width:10px;height:10px;border-radius:50%;background:#16c79a}
.tag{margin-left:auto;font-size:12px;letter-spacing:.06em;text-transform:uppercase;border:1px solid #4a4c57;border-radius:99px;padding:3px 10px}
.chat{padding:26px 28px;display:flex;flex-direction:column;gap:14px}
.m{max-width:76%;padding:12px 16px;border-radius:14px}
.u{align-self:flex-end;background:#7c5cff;color:#fff;border-bottom-right-radius:4px}
.a{align-self:flex-start;background:#2a2c35;border-bottom-left-radius:4px}
code{background:#3a3d49;border-radius:5px;padding:1px 6px;font-size:.92em}
.draft{margin:10px 0;padding:10px 14px;border-left:3px solid #7c5cff;background:#23252d;border-radius:0 8px 8px 0;font-size:.95em}
.done{align-self:stretch;max-width:none;background:#172a26;border:1px solid #1f6b58}
.done h4{font-size:15px;color:#4fe0b8;margin-bottom:10px;font-weight:600}
.files{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:10px}
.files span{background:#1f3a34;border-radius:8px;padding:5px 12px;font-size:15px}
"""


def render(lang):
    t = TEXT[lang]
    turns = "\n".join(f'<div class="m {who}">{html}</div>' for who, html in t["turns"])
    files = "".join(f"<span>✓ {f}</span>" for f in t["files"])
    return f"""<!doctype html><meta charset="utf-8"><style>{CSS}</style>
<div class="win"><div class="bar"><span class="dot"></span>{t["title"]}<span class="tag">{t["tag"]}</span></div>
<div class="chat">{turns}
<div class="m a done"><h4>{t["done"]}</h4><div class="files">{files}</div>{t["last"]}</div>
</div></div>"""


if __name__ == "__main__":
    out = Path(sys.argv[1])
    out.mkdir(parents=True, exist_ok=True)
    for lang in TEXT:
        (out / f"onboarding-chat{lang}.html").write_text(render(lang), encoding="utf-8")
        print(out / f"onboarding-chat{lang}.html")
