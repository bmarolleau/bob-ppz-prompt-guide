# IBM Bob Premium Package for Z 3.x : fonctionnalités, modes, workflows, skills et labs

🌐 **Langue :** [English](GLOBAL-docu-ibm-bob-for-z-3x-features-and-labs.md) · Français

IBM Bob Premium Package for Z (PPZ) est une extension pilotée par l'IA pour IBM Bob IDE et Bob Shell. Elle associe des workflows guidés, de l'automatisation et des analyses assistées par IA pour analyser, documenter, refactoriser et moderniser les applications mainframe écrites en COBOL et PL/I.

**Langages :** COBOL, PL/I, JCL, REXX, HLASM
**Middleware :** CICS, IMS, MQ, Db2
**Versions couvertes :** 3.0.0 (juin 2026) à 3.1.10 (octobre 2026)

---

## 1. Fonctionnalités clés

| Domaine | Capacité |
|---|---|
| Workflows guidés | Workflows structurés et reproductibles pour le dictionnaire de données, la documentation, les règles métier, l'explication, l'optimisation, le refactoring et la transformation vers Java |
| Compréhension du legacy | Analyse des programmes, copybooks, dépendances et chemins de flot de contrôle, stockée dans une base de métadonnées locale |
| Documentation intégrée | Documentation de programmes et d'applications, extraction des règles métier et explications multi-perspectives |
| Transformation | Planification d'implémentation, extraction de services (refactoring), planification et validation de la transformation COBOL/PL/I vers Java |
| Gouvernance | Skills de standards de codage, ZCodeScan, analyse d'impact, dictionnaire de données |
| Options de déploiement | SaaS ; sur site sur Red Hat OpenShift (y compris en environnement isolé) ; Z Understand et Refactor autonomes sur OpenShift ; zCX ; Bob Shell sur Z |
| Accès distant | Espaces de travail virtuels z/OS via Zowe Explorer |
| Connaissance spécifique à Z | Outil Z Context (recherche dans la documentation IBM Z) |

Documentation : [Présentation de Bob for Z](https://bob.ibm.com/docs/ide/premium-packages/bob-for-z/bob-for-z-index) · [IBM Docs, Bob for Z 3.x](https://www.ibm.com/docs/en/bobz/3.x)

---

## 2. Modes, workflows, skills et outils

### 2.1 Modes

| Mode | Objectif | Utilisateurs types |
|---|---|---|
| **Z Code** | Ingénierie au quotidien : explication de code, planification des changements, implémentation, documentation | Développeurs |
| **Z Architect** | Architecture et conception : analyse d'impact, planification d'implémentation, analyse de système, documentation technique | Architectes, responsables techniques |

Les modes standard de Bob (Agent, Plan, Ask) restent disponibles et sont utilisés dans les labs pour les opérations sur fichiers et commandes.

Référence : [Modes](https://bob.ibm.com/docs/ide/premium-packages/bob-for-z/modes)

### 2.2 Workflows

Lancez un workflow avec le bouton **Start Workflow** du panneau de chat Bob, ou avec une commande slash.

| Workflow | Description | Mode |
|---|---|---|
| Generate data dictionary | Associe les variables à des descriptions métier (stockées dans `DD.json`) | Z Code |
| Generate program documentation | Documentation structurée des programmes COBOL, PL/I, HLASM et JCL | Z Code |
| Generate application documentation | Documentation HTML navigable avec diagrammes et références croisées | Z Architect |
| Explain code | Explications selon la perspective Architecte, Métier ou Développeur | Z Code |
| Extract business rules | Règles métier structurées à partir de COBOL, PL/I ou HLASM | Z Code |
| Optimize COBOL program | Goulots d'étranglement de performance et recommandations priorisées | Z Code |
| Refactor COBOL or PL/I program | Identifie la logique métier à extraire dans des programmes de service | Z Code |
| Generate refactored service program | Crée le programme de service à partir des candidats à l'extraction | Z Code |
| Plan transformation to Java | Exigences, architecture, plan d'implémentation, évaluation de l'état de préparation | Z Code |
| Validate transformed code | Données de test et tests JUnit générés pour vérifier l'équivalence fonctionnelle | Z Code |

Référence : [Workflows](https://bob.ibm.com/docs/ide/premium-packages/bob-for-z/workflows)

### 2.3 Commandes slash

| Commande | Objectif |
|---|---|
| `/init` | Analyse la base de code et génère `AGENTS.md` |
| `/data-dictionary-management` | Génère un dictionnaire de données |
| `/sync-data-dictionary` | Synchronise le dictionnaire de données local avec la copie centrale du serveur Z Understand |
| `/explain` | Explication multi-perspectives d'un fichier source complet |
| `/refactor` | Refactoring interactif avec extraction Z Understand |
| `/refactor-report-generation` | Rapports pour les travaux de refactoring en services |
| `/impact-analysis` | Analyse d'impact d'un changement proposé |
| `/implementation-planning` | Plan d'implémentation pour un besoin métier |
| `/z-coding-standards-skill-builder` | Construit des standards de codage à partir du code existant |
| `/sign-in-to-z-understand` | S'authentifie auprès du serveur Z Understand |

Référence : [Utilisation des commandes](https://bob.ibm.com/docs/ide/premium-packages/bob-for-z/Using_commands)

### 2.4 Skills

| Skill | Objectif | Mode |
|---|---|---|
| `z-coding-standards-skill-builder` | Standards de codage cohérents | Z Code |
| `implementation-planning` | Plans d'implémentation basés sur l'analyse Z Understand | Z Architect |
| `impact-analysis` | Impact des changements sur COBOL, PL/I, JCL, Assembler, REXX | Z Architect |
| `data-dictionary-management` | Création et maintenance des dictionnaires de données COBOL et PL/I | Z Code, Z Architect |
| `refactor-report-generation` | Rapports pour le refactoring en services | Z Code |
| `zdebug-cobol-batch-mode-jcl` (3.1.0+) | Crée et diagnostique des JCL batch pour déboguer du COBOL avec Z Open Debug | Z Code |
| `explain` | Explications de fichiers complets. Non pris en charge à partir de la version 3.0.20 ; utilisez le workflow Explain code | Z Code, Z Architect |

Référence : [Utilisation des skills](https://bob.ibm.com/docs/ide/premium-packages/bob-for-z/Using_skills)

### 2.5 Groupes d'outils

| Groupe | Principaux outils |
|---|---|
| Scan et flot de contrôle | `scan_program`, `get_control_flow`, `get_paragraphs`, `execute_sql_query` |
| Dictionnaire de données | `get_variables`, `edit_data_dictionary`, `sync_data_dictionary` |
| Z Open Editor / ZCodeScan | `zopeneditor-cobol-get-program-control-flow`, `zopeneditor-cobol-get-data-flow`, `zcodescan-check-current-program` |
| Découverte à l'échelle du projet (Z Understand) | `sign_in_to_z_understand`, `get_project_programs`, `get_project_resource_usage`, `get_project_inventory` |
| Refactoring | `refactor`, `submit_refactor_findings` |

Référence : [Utilisation des outils et groupes d'outils](https://bob.ibm.com/docs/ide/premium-packages/bob-for-z/Using_tools)

---

## 3. Dernières fonctionnalités (4 dernières semaines)

La version la plus récente du journal des modifications est la **3.1.10**, publiée en **octobre 2026**. Le journal n'indique que le mois, pas le jour. Les versions antérieures (3.1.0, septembre 2026) sont en dehors de la fenêtre de 4 semaines.

Référence : [Journal des modifications, onglet IBM Z](https://bob.ibm.com/docs/ide/changelog?tab=premium-ibm-z)

### 3.1 Nouveautés de la 3.1.10

| Fonctionnalité | Résumé |
|---|---|
| Packages VSIX spécifiques à la plateforme | Packages pour `linux-x64`, `darwin-arm64` et `win32-x64` ; un VSIX universel reste disponible |
| Périmètre d'analyse dans `zapp.yaml` | Un profil `analysis` limite l'analyse aux répertoires et langages choisis (COBOL, PL/I, JCL, HLASM) ; paramètres IMS et CICS optionnels |
| Gestion des métadonnées d'analyse | Représentation indexée de l'espace de travail avec scan incrémental et indicateurs d'état ; activable ou désactivable dans les paramètres |
| Plan transformation to Java | Génère exigences, architecture, plans d'implémentation et évaluation de l'état de préparation ; prend en charge la décomposition en services |
| Validate transformed code | Génère des données de test et des tests JUnit, met en correspondance le comportement source avec Java, produit des rapports de validation ; fonctionne sans connexion au mainframe |
| Quantum Safe Cryptography | Découverte et évaluation des actifs cryptographiques pour préparer la résistance quantique |
| JCL Call Extensibility Examples | Exemples de configuration pour des schémas d'appel JCL personnalisés |

### 3.2 Améliorations de la 3.1.10

- Synchronisation du dictionnaire de données entre l'espace de travail local et le référentiel central.
- Nouveau format de fichier de synchronisation avec sélection du type de membre et filtrage par expression régulière pour les sources PDS et Endevor.
- L'intégration d'un scanner personnalisé avec la CLI BuildClient d'IBM Application Discovery prend en charge les builds incrémentaux.
- Prise en charge de l'API CRYPTO et des maps BMS pour COBOL, PL/I et HLASM.
- Résumé de fin de documentation de programme avec liens directs vers tous les fichiers `.md` générés.
- Descriptions des macros zTPF incluses dans l'extraction des règles métier Assembler ; `overview.md` généré pour Assembler.
- Option **Skip Regeneration** pour l'explication de code dans la page Paramètres.

### 3.3 Jalons des versions précédentes

| Version | Date | Points marquants |
|---|---|---|
| 3.1.0 | Septembre 2026 | Déploiement sur site sur OpenShift, Z Understand et Refactor autonomes, Extension Pack, Check Project pour JCL et HLASM, prise en charge d'Endevor, recommandations de performance COBOL assistées par IA |
| 3.0.20 | Août 2026 | Fonctionnalité Decisions, Explain code à partir de prompts en langage naturel, espaces de travail virtuels z/OS avec Zowe Explorer, documentation JCL, documentation multilingue |
| 3.0.10 | Août 2026 | Check Project, Bring Your Own Scanner, prise en charge de zCX, rapports CA7 hors ligne, workflows de documentation de programme et d'application, outil Z Context |
| 3.0.0 | Juin 2026 | Workflows structurés, dictionnaire de données avec génération en masse et synchronisation, documentation de programme et extraction des règles métier, Bob Shell dans le conteneur Linux Z Understand |

---

## 4. Labs pratiques et matrice des outils

Les labs utilisent la CICS Banking Sample Application (CBSA) et sont publiés en français dans le [dépôt Bob4z-a-thon](https://github.com/ovallod/Bob4z-a-thon/tree/main/FR). Une version anglaise est disponible dans le [dossier EN](https://github.com/ovallod/Bob4z-a-thon/tree/main/EN).

| Lab | Outils, skills et workflows utilisés | Objectifs d'apprentissage |
|---|---|---|
| **1. Discover CBSA** ([source](https://github.com/ovallod/Bob4z-a-thon/blob/main/FR/1-LabDiscoverCBSA.md)) | Modes : Z Code, Z Architect, Agent. `/init` avec `scan_program` ; workflow Generate data dictionary ; `execute_sql_query` ; `/z-coding-standards-skill-builder` ; `/explain` ; workflow de génération de documentation (règles métier) ; diagrammes draw.io ; analyse d'impact et planification d'implémentation | Définir les règles de nommage et d'organisation ; initialiser l'espace de travail ; construire un dictionnaire de données, un inventaire applicatif et des standards de codage ; produire des diagrammes d'architecture ; documenter les programmes et les règles métier ; réaliser une analyse d'impact (SORTCODE fixe vers variable) ; documenter le parcours utilisateur ; planifier et implémenter une nouvelle fonctionnalité (recherche par e-mail) |
| **2. Discover CBSA Global** ([source](https://github.com/ovallod/Bob4z-a-thon/blob/main/FR/2-LabDiscoverCBSAGlobal.md)) | Modes : Agent (récupération du front-end), Z Code. `/init` (`AGENTS.md`) ; workflow de dictionnaire de données ; inventaires COBOL et front-end ; diagrammes draw.io | Étendre l'analyse CBSA au front-end (Java, React, API) ; produire les inventaires backend et frontend et les diagrammes d'architecture ; analyser un flux fonctionnel (virement local) ; rédiger un guide utilisateur ; analyser techniquement le scoring de crédit |
| **3. Skill Builder & Refactor** ([source](https://github.com/ovallod/Bob4z-a-thon/blob/main/FR/3-LabSkillBuilder-Refactor.md)) | Z Code : `/z-coding-standards-skill-builder`. Z Architect : `/refactor` (extraction Z Understand), `extractionGoal.md` | Générer un skill de standards de codage personnalisé et l'utiliser pour produire du code conforme ; refactoriser `INQCUST` de VSAM vers Db2 : analyser, concevoir le modèle Db2, exécuter le refactoring interactif, planifier la migration et les tests |
| **4. Optimize SQL & Db2 Config** ([source](https://github.com/ovallod/Bob4z-a-thon/blob/main/FR/4-LabOptimizeSQL%26DB2Config.md)) | Modes : Agent, Z Code. Inventaire du SQL embarqué ; analyse des JCL DDL Db2 ; génération d'ERD ; analyse de performance ; génération de JCL ; export draw.io | Inventorier les instructions SQL embarquées ; détecter les anti-patterns (par exemple fetch multi-lignes, contention de verrous) ; rétro-concevoir les DDL en diagramme entité-relation et hiérarchie de stockage ; recommander et implémenter des améliorations (par exemple l'index manquant sur `PROCTRAN`) ; exporter les diagrammes vers draw.io |

### Couverture des outils et capacités par lab

| Capacité | Lab 1 | Lab 2 | Lab 3 | Lab 4 |
|---|:---:|:---:|:---:|:---:|
| `/init` et `AGENTS.md` | ✓ | ✓ | | |
| Dictionnaire de données | ✓ | ✓ | | |
| Inventaire applicatif | ✓ | ✓ | | ✓ |
| Skill de standards de codage | ✓ | | ✓ | |
| Explication de code et règles métier | ✓ | ✓ | | |
| Analyse d'impact et planification | ✓ | | | |
| Refactoring (`/refactor`) | | | ✓ | |
| Diagrammes d'architecture (draw.io) | ✓ | ✓ | | ✓ |
| Analyse SQL et Db2 | | | ✓ | ✓ |
| Analyse du front-end | | ✓ | | |
| Génération de code | ✓ | | ✓ | ✓ |
