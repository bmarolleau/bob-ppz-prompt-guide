# IBM Bob Premium Package for Z 3.x: Features, Modes, Workflows, Skills and Labs

🌐 **Language:** English · [Français](GLOBAL-docu-ibm-bob-for-z-3x-features-and-labs-FR.md)

IBM Bob Premium Package for Z (PPZ) is an AI-powered extension for IBM Bob IDE and Bob Shell. It combines guided workflows, automation and AI-driven insights to analyze, document, refactor and modernize mainframe applications written in COBOL and PL/I.

**Languages:** COBOL, PL/I, JCL, REXX, HLASM
**Middleware:** CICS, IMS, MQ, Db2
**Releases covered:** 3.0.0 (June 2026) to 3.1.10 (October 2026)

---

## 1. Key Features

| Area | Capability |
|---|---|
| Guided workflows | Structured, repeatable workflows for data dictionary, documentation, business rules, explanation, optimization, refactoring and Java transformation |
| Legacy understanding | Analysis of programs, copybooks, dependencies and control-flow paths, stored as a local metadata database |
| Integrated documentation | Program and application documentation, business rules extraction and multi-perspective explanations |
| Transformation | Implementation planning, service extraction (refactoring), COBOL/PL/I to Java planning and validation |
| Governance | Coding standards skills, ZCodeScan, impact analysis, data dictionary |
| Customization | Bob rules (`.bob/rules/`, `AGENTS.md`) to enforce naming, organization and documentation conventions; custom modes and skills |
| Deployment options | SaaS; on-premises on Red Hat OpenShift (including air-gapped); Z Understand and Refactor standalone on OpenShift; zCX; Bob Shell on Z |
| Remote access | z/OS virtual workspaces through Zowe Explorer |
| Z-specific knowledge | Z Context tool (retrieval over IBM Z documentation) |

Documentation: [Bob for Z overview](https://bob.ibm.com/docs/ide/premium-packages/bob-for-z/bob-for-z-index) · [IBM Docs, Bob for Z 3.x](https://www.ibm.com/docs/en/bobz/3.x)

---

## 2. Modes, Workflows, Skills and Tools

### 2.1 Modes

| Mode | Purpose | Typical users |
|---|---|---|
| **Z Code** | Day-to-day engineering: code explanation, change planning, implementation, documentation | Developers |
| **Z Architect** | Architecture and design: impact analysis, implementation planning, system analysis, technical documentation | Architects, technical leads |

Bob's standard modes (Agent, Plan, Ask) remain available and are used in the labs for file and command operations.

Reference: [Modes](https://bob.ibm.com/docs/ide/premium-packages/bob-for-z/modes)

### 2.2 Workflows

Start a workflow with the **Start Workflow** button in the Bob chat panel, or with a slash command.

| Workflow | Description | Mode |
|---|---|---|
| Generate data dictionary | Maps variables to business-friendly descriptions (stored in `DD.json`) | Z Code |
| Generate program documentation | Structured documentation for COBOL, PL/I, HLASM and JCL programs | Z Code |
| Generate application documentation | Navigable HTML documentation with diagrams and cross-references | Z Architect |
| Explain code | Explanations from Architect, Business or Developer perspective | Z Code |
| Extract business rules | Structured business rules from COBOL, PL/I or HLASM | Z Code |
| Optimize COBOL program | Performance bottlenecks and prioritized recommendations | Z Code |
| Refactor COBOL or PL/I program | Identifies business logic to extract into service programs | Z Code |
| Generate refactored service program | Creates the service program from extraction candidates | Z Code |
| Plan transformation to Java | Requirements, architecture, implementation plan, readiness assessment | Z Code |
| Validate transformed code | Generated test data and JUnit tests to verify functional equivalence | Z Code |

Reference: [Workflows](https://bob.ibm.com/docs/ide/premium-packages/bob-for-z/workflows)

### 2.3 Slash Commands

| Command | Purpose |
|---|---|
| `/init` | Analyzes the codebase and generates `AGENTS.md` |
| `/data-dictionary-management` | Generates a data dictionary |
| `/sync-data-dictionary` | Synchronizes the local data dictionary with the central copy on the Z Understand server |
| `/explain` | Multi-perspective explanation of a whole source file |
| `/refactor` | Interactive refactoring with Z Understand extraction |
| `/refactor-report-generation` | Reports for service refactoring efforts |
| `/impact-analysis` | Impact analysis for a proposed change |
| `/implementation-planning` | Implementation plan for a business requirement |
| `/z-coding-standards-skill-builder` | Builds coding standards from existing code |
| `/sign-in-to-z-understand` | Authenticates with the Z Understand server |

Reference: [Using commands](https://bob.ibm.com/docs/ide/premium-packages/bob-for-z/Using_commands)

### 2.4 Skills

| Skill | Purpose | Mode |
|---|---|---|
| `z-coding-standards-skill-builder` | Consistent coding standards | Z Code |
| `implementation-planning` | Implementation plans based on Z Understand analysis | Z Architect |
| `impact-analysis` | Impact of changes across COBOL, PL/I, JCL, Assembler, REXX | Z Architect |
| `data-dictionary-management` | Create and maintain COBOL and PL/I data dictionaries | Z Code, Z Architect |
| `refactor-report-generation` | Reports for service refactoring | Z Code |
| `zdebug-cobol-batch-mode-jcl` (3.1.0+) | Creates and diagnoses batch JCL for debugging COBOL with Z Open Debug | Z Code |
| `explain` | Whole-file explanations. Not supported from release 3.0.20; use the Explain code workflow | Z Code, Z Architect |

Reference: [Using skills](https://bob.ibm.com/docs/ide/premium-packages/bob-for-z/Using_skills)

### 2.5 Tool Groups

| Group | Main tools |
|---|---|
| Scanning and control flow | `scan_program`, `get_control_flow`, `get_paragraphs`, `execute_sql_query` |
| Data dictionary | `get_variables`, `edit_data_dictionary`, `sync_data_dictionary` |
| Z Open Editor / ZCodeScan | `zopeneditor-cobol-get-program-control-flow`, `zopeneditor-cobol-get-data-flow`, `zcodescan-check-current-program` |
| Project-wide discovery (Z Understand) | `sign_in_to_z_understand`, `get_project_programs`, `get_project_resource_usage`, `get_project_inventory` |
| Refactoring | `refactor`, `submit_refactor_findings` |

Reference: [Using tools and tool groups](https://bob.ibm.com/docs/ide/premium-packages/bob-for-z/Using_tools)

### 2.6 Bob Rules and AGENTS.md

Rules are standing instructions that Bob applies to every task, without repeating them in each prompt. They extend Bob's default behavior with preferences, constraints and guidelines: coding style, documentation formats, testing requirements, project workflows and team conventions.

**Where rules live**

| Location | Scope | Applies to |
|---|---|---|
| `~/.bob/rules/` | Global: all your projects | All modes |
| `.bob/rules/` | Workspace: current project only | All modes |
| `.bob/rules-{mode-slug}/` | Workspace: current project only | One mode (use the slug of the mode, for example `rules-plan/` for Plan mode) |
| `AGENTS.md` (project root) | Workspace: current project only | All modes; loaded automatically and versioned with the project |

```text
.bob/
├── rules/
│   └── 01-naming-and-organization.md     # general rules, all modes
└── rules-{mode-slug}/
    ├── 01-style-guide.md                 # rules for one mode only
    └── 02-formatting.txt
```

**How rules are combined**

- Global rules (`~/.bob/rules/`) load first, then workspace rules (`.bob/rules/`). Workspace rules can override global rules.
- Within each level, mode-specific rules load before general rules.
- Files in a rules directory are loaded alphabetically; numeric prefixes (`01-`, `02-`) control the order.
- `/init` analyzes the codebase and generates `AGENTS.md`, which gives Bob the project context from the first task.

**Writing effective rules**

- Organize by topic, with one short bullet per rule and a concrete example of the expected result.
- Keep rules and `AGENTS.md` short. They are part of the standing context and consume tokens before you type anything: put only conventions, setup, test and style commands there.
- Use global rules for personal or organization-wide standards, and workspace rules for project requirements.

**Rules in the labs**

[Lab 1, Exercise 0](https://github.com/ovallod/Bob4z-a-thon/blob/main/EN/1-LabDiscoverCBSA_EN.md) creates the first rules of the CBSA project, before any analysis. One prompt (abridged below) defines where Bob stores what it generates and how it names it:

```text
Create the following Bob rules (file in .bob/rules):
- Documents must be stored in the docs/ directory. Documents specific to a program go in a
  sub-directory named after the program (for example docs/BNKMENU/).
- Tools must be stored in the tools/ directory.
- Schemas, drawings and graphs must be stored in graph/ directory.
- File names follow [PREFIX]-[TYPE]-[description].md, where PREFIX is the program name,
  CBSA (application) or GLOBAL (cross-cutting), and TYPE is analysis, archi, docu, inv, plan or spec.
```

Bob writes the rules to `.bob/rules/` or to a dedicated section of `AGENTS.md`; both are applied the same way. The following exercises then generate documents in the locations and with the names defined by these rules (for example `GLOBAL-docu-...` for cross-cutting documents).

References: [Custom rules](https://bob.ibm.com/docs/ide/configuration/rules) · [Standardize Bob's behavior](https://bob.ibm.com/docs/ide/tutorials/standardize-bobs-behavior) · [Custom rules in Bob Shell](https://bob.ibm.com/docs/shell/configuration/bobshell-custom-rules)

---

## 3. Latest Features (Last 4 Weeks)

The most recent release in the changelog is **3.1.10**, published in **October 2026**. The changelog gives the month only, not the day. Earlier releases (3.1.0, September 2026) fall outside the 4-week window.

Reference: [Changelog, IBM Z tab](https://bob.ibm.com/docs/ide/changelog?tab=premium-ibm-z)

### 3.1 New in 3.1.10

| Feature | Summary |
|---|---|
| Platform-specific VSIX packages | Packages for `linux-x64`, `darwin-arm64` and `win32-x64`; a universal VSIX remains available |
| Analysis scope in `zapp.yaml` | An `analysis` profile limits analysis to chosen directories and languages (COBOL, PL/I, JCL, HLASM); optional IMS and CICS settings |
| Analysis metadata management | Indexed workspace representation with incremental scanning and status indicators; can be enabled or disabled in settings |
| Plan transformation to Java | Generates requirements, architecture, implementation plans and readiness assessment; supports service decomposition |
| Validate transformed code | Generates test data and JUnit tests, maps source behavior to Java, produces validation reports; works without mainframe connectivity |
| Quantum Safe Cryptography | Discovery and assessment of cryptographic assets for quantum-readiness planning |
| JCL Call Extensibility Examples | Sample configurations for custom JCL call patterns |

### 3.2 Improvements in 3.1.10

- Data dictionary synchronization between local workspace and central repository.
- Updated synchronization file format with member-type selection and regex filtering for PDS and Endevor sources.
- Custom-built scanner integration with the IBM Application Discovery BuildClient CLI supports incremental builds.
- CRYPTO API and BMS map support for COBOL, PL/I and HLASM.
- Program documentation completion summary with direct links to all generated `.md` files.
- zTPF macro descriptions included in Assembler business rules extraction; `overview.md` generated for Assembler.
- **Skip Regeneration** option for code explanation in the Settings page.

### 3.3 Previous Release Milestones

| Release | Date | Highlights |
|---|---|---|
| 3.1.0 | September 2026 | On-premises deployment on OpenShift, standalone Z Understand and Refactor, Extension Pack, Check Project for JCL and HLASM, Endevor support, AI-powered COBOL performance recommendations |
| 3.0.20 | August 2026 | Decisions feature, Explain code from natural-language prompts, z/OS virtual workspaces with Zowe Explorer, JCL documentation, multi-lingual documentation |
| 3.0.10 | August 2026 | Check Project, Bring Your Own Scanner, zCX support, CA7 reports offline, program and application documentation workflows, Z Context tool |
| 3.0.0 | June 2026 | Structured workflows, data dictionary with bulk generation and sync, program documentation and business rules extraction, Bob Shell in the Z Understand Linux container |

---

## 4. Practical Labs & Tools Matrix

The labs use the CICS Banking Sample Application (CBSA) and are published in English in the [Bob4z-a-thon repository](https://github.com/ovallod/Bob4z-a-thon/tree/main/EN). A French version is available in the [FR folder](https://github.com/ovallod/Bob4z-a-thon/tree/main/FR).

| Lab | Tools, skills and workflows used | Learning objectives |
|---|---|---|
| **1. Discover CBSA** ([source](https://github.com/ovallod/Bob4z-a-thon/blob/main/EN/1-LabDiscoverCBSA_EN.md)) | Modes: Z Code, Z Architect, Agent. Bob rules (`.bob/rules`, `AGENTS.md`); `/init` with `scan_program`; Generate data dictionary workflow; `execute_sql_query`; `/z-coding-standards-skill-builder`; `/explain`; Generate documentation workflow (business rules); draw.io diagrams; impact analysis and implementation planning | Define Bob rules for naming and organization; initialize the workspace; build a data dictionary, application inventory and coding standards; produce architecture diagrams; document programs and business rules; run an impact analysis (fixed to variable SORTCODE); document the user journey; plan and implement a new feature (search by email) |
| **2. Discover CBSA Global** ([source](https://github.com/ovallod/Bob4z-a-thon/blob/main/EN/2-LabDiscoverCBSAGlobal_EN.md)) | Modes: Agent (front-end retrieval), Z Code. `/init` (`AGENTS.md`); data dictionary workflow; COBOL and front-end inventories; draw.io diagrams | Extend the CBSA analysis to the front end (Java, React, APIs); produce backend and frontend inventories and architecture diagrams; analyze a functional flow (local transfer); write a user guide; analyze credit scoring technically |
| **3. Skill Builder & Refactor** ([source](https://github.com/ovallod/Bob4z-a-thon/blob/main/EN/3-LabSkillBuilder-Refactor_EN.md)) | Z Code: `/z-coding-standards-skill-builder`. Z Architect: `/refactor` (Z Understand extraction), `extractionGoal.md` | Generate a custom coding standards skill and use it to generate compliant code; refactor `INQCUST` from VSAM to Db2: analyze, design the Db2 model, run interactive refactoring, plan migration and tests |
| **4. Optimize SQL & Db2 Config** ([source](https://github.com/ovallod/Bob4z-a-thon/blob/main/EN/4-LabOptimiseSQL%26DB2Config_EN.md)) | Modes: Agent, Z Code. Embedded SQL inventory; Db2 DDL JCL analysis; ERD generation; performance analysis; JCL generation; draw.io export | Inventory embedded SQL statements; detect anti-patterns (for example multi-row fetch, lock contention); reverse-engineer DDL to an entity-relationship diagram and storage hierarchy; recommend and implement improvements (for example the missing `PROCTRAN` index); export diagrams to draw.io |

### Tool and Capability Coverage by Lab

| Capability | Lab 1 | Lab 2 | Lab 3 | Lab 4 |
|---|:---:|:---:|:---:|:---:|
| Bob rules (`.bob/rules`) | ✓ | | | |
| `/init` and `AGENTS.md` | ✓ | ✓ | | |
| Data dictionary | ✓ | ✓ | | |
| Application inventory | ✓ | ✓ | | ✓ |
| Coding standards skill | ✓ | | ✓ | |
| Code explanation and business rules | ✓ | ✓ | | |
| Impact analysis and planning | ✓ | | | |
| Refactoring (`/refactor`) | | | ✓ | |
| Architecture diagrams (draw.io) | ✓ | ✓ | | ✓ |
| SQL and Db2 analysis | | | ✓ | ✓ |
| Front-end analysis | | ✓ | | |
| Code generation | ✓ | | ✓ | ✓ |
