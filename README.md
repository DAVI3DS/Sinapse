```
                                                         
              ███████  ██    ██  ███    ██  █████   ██████  ███████ ███████ 
              ██       ██    ██  ████   ██ ██   ██ ██       ██      ██      
              ███████  ██    ██  ██ ██  ██ ███████ ██   ███ █████   ███████ 
                   ██  ██    ██  ██  ██ ██ ██   ██ ██    ██ ██           ██ 
              ███████   ██████   ██   ████ ██   ██  ██████  ███████ ███████ 
                                                                             
```

<h1 align="center">🔍 Modpack Analyzer</h1>
<p align="center"><b>Diagnóstico inteligente de modpacks — incompatibilidades, dependências ausentes e score de estabilidade.</b></p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12%2B-3776AB?style=flat&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/PySide6-6.11-41CD52?style=flat&logo=qt&logoColor=white" alt="PySide6">
  <img src="https://img.shields.io/badge/SQLite-003B57?style=flat&logo=sqlite&logoColor=white" alt="SQLite">
  <img src="https://img.shields.io/badge/API-Modrinth-00D571?style=flat&logo=modrinth&logoColor=white" alt="Modrinth">
  <img src="https://img.shields.io/badge/API-CurseForge-F16436?style=flat&logo=curseforge&logoColor=white" alt="CurseForge">
  <img src="https://img.shields.io/badge/license-MIT-yellow?style=flat" alt="License">
  <img src="https://img.shields.io/badge/status-ativo-2ecc71?style=flat" alt="Status">
</p>

<br>

---

## ✨ Funcionalidades

```
┌────────────────────────────────────────────────────────────┐
│  🎯 Importação inteligente                                 │
│     Arraste sua pasta de mods, .zip (CurseForge), .mrpack  │
│     CSV ou TXT — o scanner reconhece o formato.            │
│                                                             │
│  🔬 Análise profunda                                       │
│     Consulta APIs do Modrinth e CurseForge para detectar   │
│     dependências obrigatórias e incompatibilidades.         │
│                                                             │
│  📊 Score de Estabilidade                                  │
│     Nota 0–100 com indicador visual (🟢 Estável /           │
│     🟡 Moderado / 🔴 Instável).                            │
│                                                             │
│  📋 Relatório detalhado                                    │
│     Lista de mods com status, problemas encontrados e       │
│     ações sugeridas (links para download).                  │
│                                                             │
│  📚 Histórico de análises                                  │
│     SQLite local guarda todo histórico. Compare a evolução  │
│     do seu modpack ao longo do tempo.                       │
│                                                             │
│  💾 Exportação                                             │
│     Exporte relatório em JSON ou CSV, lista de mods em TXT. │
│                                                             │
│  🌐 Offline-first                                          │
│     Cache local de metadados. Funciona sem internet para    │
│     consultar dados de análises anteriores.                 │
└────────────────────────────────────────────────────────────┘
```

<br>

## 🚀 Começando

### Pré-requisitos

- Python 3.12+
- Pip

### Instalação

```bash
# Clone
git clone https://github.com/seu-usuario/modpack-analyzer.git
cd modpack-analyzer

# Instale dependências
pip install -r requirements.txt

# Rode!
python main.py
```

<br>

## 🎮 Como usar

```
                        ╔═══════════════════════╗
                        ║   🟢 85/100 ESTAVEL   ║
                        ╚═══════════════════════╝
                               │
     ┌─────────────────────────┼─────────────────────────┐
     │                         │                         │
     ▼                         ▼                         ▼
 ┌──────────┐          ┌──────────────┐          ┌────────────┐
 │ 📁       │          │ ⚠️ Problemas │          │ 📋 Relatório│
 │ Importar │          │ OptiFine ↔   │          │ Deps: 2    │
 │ Arraste  │          │ Sodium       │          │ Conflict: 1│
 │ a pasta  │ ───────> │ ❌ JEI ←     │ ───────> │ Sugestões: │
 │ ou       │          │   Architect  │          │ Instalar   │
 │ .zip     │          │ ℹ️ Inv.HUD   │          │ moonlit... │
 └──────────┘          └──────────────┘          └────────────┘
```

**Passo a passo:**

1. **Abra o aplicativo** — tela limpa com área de importação
2. **Arraste** a pasta do seu modpack ou clique em "Importar"
3. Os mods aparecem na tabela com status "Aguardando análise"
4. Clique **"🔍 Analisar Modpack"**
5. Pronto! Score, problemas detectados e relatório detalhado
6. Salve o histórico automaticamente e **exporte** quando quiser

<br>

## 🧠 Score de Estabilidade

| Pontuação | Rótulo | Cor | Significado |
|:---------:|:------:|:---:|:------------|
| 80–100 | **Estavel** | 🟢 | Confiável, bem balanceado |
| 50–79 | **Moderado** | 🟡 | Atenção — há riscos |
| 0–49 | **Instavel** | 🔴 | Alto risco de conflitos e crashes |

### Penalidades aplicadas

| Problema | Penalidade |
|:---------|:----------:|
| Dependência obrigatória ausente | −15 pts |
| Incompatibilidade crítica | −10 pts |
| Incompatibilidade major | −5 pts |
| Dependência recomendada ausente | −2 pts |
| Mod não identificado | −2 pts |

<br>

## 🏗️ Arquitetura

```
src/
├── app.py                 # Entry point da aplicação PySide6
├── db/
│   └── database.py        # Singleton SQLite com migrações
├── api/
│   ├── base.py            # Cliente HTTP base (rate-limit, cache)
│   ├── modrinth.py        # API Modrinth v2
│   └── curseforge.py      # API CurseForge v1
├── analysis/
│   ├── scanner.py         # Importa modpacks (.zip, .mrpack, pasta, CSV)
│   ├── resolver.py        # Motor de resolução de dependências
│   └── scorer.py          # Calcula score de estabilidade
├── models/
│   ├── mod.py             # Dataclass Mod
│   ├── modpack.py         # Dataclass Modpack
│   └── analysis.py        # Dataclass AnalysisResult / Issue
└── ui/
    ├── main_window.py     # Janela principal
    ├── import_widget.py   # Drag-and-drop + botões
    ├── score_card.py      # Gauge circular de estabilidade
    ├── mod_list.py        # Tabela de mods com indicadores
    ├── report_widget.py   # Relatório detalhado em HTML
    ├── history_panel.py   # Histórico lateral
    ├── styles.py          # QSS dark moderno
    └── theme.py           # Paleta de cores
```

<br>

## 🗄️ Banco de Dados (SQLite)

O banco local `modpack_analyzer.db` armazena:

| Tabela | Armazena |
|:-------|:---------|
| `modpacks` | Perfis importados |
| `mods` | Mods individuais com slugs/IDs |
| `modpack_mods` | Relação modpack ↔ mods |
| `dependencies` | Cache de dependências |
| `incompatibilities` | Cache de incompatibilidades |
| `analysis_history` | Histórico de scores |
| `analysis_details` | Issues de cada análise |

<br>

## 🎨 Tema

Interface dark moderna com paleta:

```css
Fundo:      #1a1a2e    │  Primária:    #0f3460
Superfície: #16213e    │  Destaque:    #e94560
Texto:      #eaeaea    │  Sucesso:     #2ecc71
Secundário: #8892b0    │  Warning:     #f1c40f
                                           🔴 Erro: #e74c3c
```

<br>

## 🧪 Testes

Teste de integração ponta a ponta:

```bash
python -c "
from src.analysis.scanner import scan
from src.analysis.resolver import Resolver
from src.analysis.scorer import calculate

mods = scan('caminho/para/seu/modpack')
r = Resolver()
issues = r.analyze(mods)
result = calculate(issues, len(mods))
print(f'Score: {result.score}/100 — {result.score_label}')
print(f'Problemas: {len(result.all_issues)}')
for i in result.all_issues:
    print(f'  [{i.issue_type}] {i.mod_name}: {i.description}')
"
```

<br>

## 🔧 Configuração CurseForge

Para usar a API da CurseForge (adicional), defina a variável de ambiente:

```bash
# Windows (PowerShell)
$env:CURSEFORGE_API_KEY = "sua-chave-aqui"

# Linux/macOS
export CURSEFORGE_API_KEY="sua-chave-aqui"
```

> 💡 A API do Modrinth é pública e não requer chave — funciona direto.

<br>

## 📦 Build (futuro)

Para gerar um executável standalone:

```bash
pip install pyinstaller
pyinstaller --onefile --windowed --name "Synapse" main.py
```

<br>

---

<p align="center">
  <b>Modpack Analyzer</b> — feito com ☕, 🐍 Python e 💙 pelo open source<br>
  <sub>Contribuições, issues e sugestões são bem-vindas!</sub>
</p>

<p align="center">
  <a href="#"><img src="https://img.shields.io/badge/⭐-Star no GitHub-2ecc71?style=social" alt="Star"></a>
  <a href="#"><img src="https://img.shields.io/badge/🐛-Reportar Bug-e74c3c?style=social" alt="Bug"></a>
  <a href="#"><img src="https://img.shields.io/badge/💡-Sugerir Melhoria-3498db?style=social" alt="Idea"></a>
</p>
