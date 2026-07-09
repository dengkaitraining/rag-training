### CLI 工具就叫Shell
### 系統環境變數對所有應用程式有效,例如PATH
### 應用程式環境變數
```python
API_KEY = os.getenv("GEMINI_API_KEY")
```
 - 程式會使用到 ```GEMINI_API_KEY``` 環境變數。
 - 我們可以設定在作業系統,讓它記下來。
 - 也可以執行時再設定
 - 1. ```cmd``` 命令提示字元
```powershell
set GEMINI_API_KEY=<user_api_key>
```
 - 2. PowerShell 視窗
```powershell
$env:GEMINI_API_KEY="你的_API_KEY "
```
### RAG_prompt = ```<user_prompt>``` + ```<context>``` + ```<specifier>```
 - ```<context>``` 有可能很大
 - 所以 reasoning token也會很多
 - cost 會 over buget

### RAG 可以檢索 Domain Knowledge 後再提問,避免 LLM 答非所問。同樣的名詞在不同領域,意義不一樣。
```markdown
Harness Engineering** (specifically Wire Harness
Engineering) is a specialized branch of electrical and
mechanical engineering focused on designing, developing,
and manufacturing wire harnesses. \n\nA wire harness (or
cable assembly) is an organized bundle of wires, cables,
connectors, and terminals that transmits electrical power and
signals throughout a system—such as an airplane, car,
spacecraft, medical device, or industrial machine.\n\nHere is a
comprehensive guide to the principles, processes, tools, and
trends in Harness Engineering.\n\n---\n\n### 1. The Core

Components of a Wire Harness\nAn engineer must
understand and select the right components based on the
environment, electrical load, and mechanical constraints:\n*
**Wires & Cables:** Conductors (usually copper or aluminum)
categorized by gauge (AWG or metric), voltage rating, and
temperature rating.\n* **Insulation & Sheathing:** Materials
like PVC, Teflon (PTFE), or XLPE that protect the wires from
heat, chemicals, and abrasion.\n* **Terminals:** The metal
components crimped or soldered to the end of a wire to make
the electrical connection (pins, sockets, ring terminals).\n*
**Connectors:** The plastic or metal housings that hold the
terminals and plug into devices.\n* **Protective Coverings:**
Conduits, corrugated tubes, braided sleeving, and electrical
tape that protect the bundle from external hazards.\n*
**Fixings & Fasteners:** Clips, clamps, cable ties, and
grommets used to route and secure the harness to the vehicle
or machine chassis.\n\n---\n\n### 2. The Harness Design
Process\nHarness engineering bridge the gap between
electrical schematics and physical mechanical installation.
The workflow generally follows these steps:\n\n#### Phase A:
System Architecture & Schematics (Electrical)\n* The system
engineers define what needs to be connected (sensors,
actuators, ECUs, power sources).\n* Harness engineers
design the **schematic diagram**

, showing the point-to-point
electrical connections, wire gauges, inline connectors, and
fuses.\n\n#### Phase B: 3D Routing (Mechanical)\n* Using a
3D CAD model of the vehicle or product, the engineer routes
the bundle through the physical space.\n* Key considerations:
Avoid sharp edges, high-heat zones (like exhaust pipes), and
moving parts. Ensure correct bend radii (wires cannot bend at
90-degree angles without stress).\n\n#### Phase C: 2D
Formboard/Nailboard Design (Manufacturing)\n* The 3D CAD
model is flattened into a 1:1 scale 2D drawing called a
**formboard** or **nailboard**.\n* This drawing is printed out
on a giant table in the factory. Workers lay the physical wires

directly on top of the drawing to build the harness.\n\n####
Phase D: Testing & Validation\n* **Continuity Testing:**
Ensuring every wire connects to the correct pin.\n* **Pull
Testing:** Testing the mechanical strength of the crimped
terminals.\n* **Environmental Testing:** Exposing prototypes
to vibration, thermal shock, dust, and water (IP ratings).\n\n---
\n\n### 3. Industry Standards\nHarness engineering is highly
regulated to ensure safety and reliability. The most critical
standards include:\n* **IPC/WHMA-A-620:** The global
"bible" for cable and wire harness assembly acceptance. It
defines visual quality criteria for crimping, soldering, and
splicing.\n* **SAE (Society of Automotive Engineers):**
Standards like SAE J1128 for low-voltage automotive
cables.\n* **AS9100 / MIL-SPEC:** Strict standards for
aerospace and military harnesses, requiring high traceability
and extreme environment survival.\n\n---\n\n### 4. Essential
Software Tools\nModern harness design relies heavily on
specialized CAD suites:\n* **Electrical & Schematic Design:**
Zuken E3.series, Mentor Graphics (Siemens) Capital,
AutoCAD Electrical.\n* **3D Routing:** CATIA V5/V6
(Electrical Harness Discipline), Siemens NX, SolidWorks
Electrical 3D.\n* **PLM (Product Lifecycle Management):**
Teamcenter or Windchill, used to manage revisions and Bills
of Materials (BOM).\n\n---\n\n### 5. Key Design
Challenges\n* **Space & Weight Constraints:** In aerospace
and automotive (especially EVs), reducing weight is critical.
Engineers must optimize wire gauges and search for
lightweight alternatives like aluminum wire.\n*

**Electromagnetic Interference (EMI):** Signals from high-
power wires can corrupt data in sensor wires. Engineers must

design shields, twisted pairs, and physical separation between
power and signal lines.\n* **High Voltage (HV) Safety:** With
the rise of Electric Vehicles (EVs), engineers must design

harnesses carrying up to 1000V. These require orange-
colored conduits, touch-proof connectors, and heavy

shielding.\n\n---\n\n### 6. Modern Trends in Harness
Engineering\n* **Vehicle Electrification (EVs):** Requires
high-voltage distribution systems, heavy copper busbars, and
advanced thermal management for the harness.\n*
**Autonomous Driving & High-Speed Data:** Self-driving cars
require massive data transmission (cameras, LiDAR, radar).
Harness engineers must integrate Ethernet, coax, and optical
fibers.\n* **Automated Manufacturing:** Historically, wire
harness assembly has been highly manual. The industry is
moving toward automated wire cutting, stripping, crimping,
and even robotic tape wrapping.\n* **Model-Based Systems
Engineering (MBSE):** Integrating electrical design directly
with software and mechanical data to predict failures before
physical prototypes are built.\n\n### Careers in Harness
Engineering\nIf you are interested in this field, roles include
**Harness Design Engineer** (focused on CAD and
schematics),

**Harness Release Engineer** (managing

supplier relations and delivery), and **Manufacturing/Process
Engineer** (focused on how the harness is built on the factory
floor). It is a highly sought-after specialty in the automotive,
aerospace, defense, and robotics industries.

**Harness Engineering** in the context of Large Language
Models (LLMs) refers to the discipline of designing, building,
and maintaining the infrastructure, tools, and frameworks
used to **evaluate, benchmark, test, and safely deploy
LLMs**. \n\nJust as a traditional "test harness" in software
engineering is used to run a suite of tests and capture the
results, an LLM Harness surrounds a model to feed it
prompts, capture its completions, grade its performance, and
guard it against unsafe behavior.\n\nHere is a comprehensive
guide to Harness Engineering in LLMs, covering why it is
crucial, its key components, popular tools, and best
practices.\n\n---\n\n### 1. Why is Harness Engineering
Critical for LLMs?\nUnlike traditional deterministic software,

LLMs are probabilistic ("black boxes"). A minor change in a
prompt, temperature, or model version can completely change
the output. Harness engineering solves several critical
challenges:\n* **The "Vibe Check" Problem:** Developers
often test LLMs by manually typing a few prompts. This does
not scale. A harness automates testing over thousands of
scenarios.\n* **Regression Testing:** When upgrading from
GPT-3.5 to GPT-4, or fine-tuning a local model, a harness
ensures that fixing one bug hasn\'t broken ten other
features.\n* **Safety and Alignment:** Harnesses act as
"guardrails" to prevent models from generating toxic content,
leaking personally identifiable information (PII), or succumbing
to prompt injection.\n* **Cost and Latency Optimization:** It
helps measure token usage, cost, and response times across
different model providers.\n\n---\n\n### 2. Core Components
of an LLM Harness\nAn LLM harness generally operates in
two phases: **Evaluation (Pre-deployment)** and
**Runtime/Guardrails (In-production)**.\n\n```\n[User/Dataset]
---> [Input Guardrails] ---> [LLM] ---> [Output Guardrails] --->
[Evaluator/User]\n | |\n +----------- (Telemetry) -----------
+\n```\n\n#### A. Input & Output Guardrails (Runtime
Harness)\nThis wraps the LLM during live production to filter
inputs and outputs.\n* **Input Filter:** Detects prompt injection
attacks, jailbreak attempts, or toxic inputs before they reach
the LLM.\n* **Output Filter:** Checks the LLM\'s response for
PII, profanity, hallucinations, or copyright violations before
showing it to the user.\n\n#### B. Evaluation Engine (Offline
Harness)\nThis is used during development to score the
model\'s intelligence and accuracy.\n* **Dataset Registry:** A
collection of "golden datasets" (curated prompt-response pairs
representing ideal behavior).\n* **Execution Engine:** Sends
these prompts to the LLM (or multiple LLMs in parallel).\n*
**Scorers/Metrics:** Algorithmic or LLM-based judges that
grade the outputs.\n\n#### C. Telemetry and Observability\n*
Logs every input/output pair.\n* Tracks latency, token count,

and cost.\n* Monitors "drift" (when user behavior or model
responses change over time).\n\n---\n\n### 3. Key
Methodologies in LLM Evaluation (The Eval
Harness)\nEvaluating LLMs is notoriously difficult. Harness
engineers use four primary methods to grade LLM
outputs:\n\n1. **Rule-Based / Exact Match:** Best for
factual/coding tasks (e.g.,

"Does the output contain the correct

SQL syntax?"

, JSON validation, or Regex matching).\n2.
**Semantic Similarity:** Using embedding models to see if the
LLM\'s answer is semantically close to the "ground truth"
answer (e.g., BLEU, ROUGE, or Cosine Similarity).\n3.

**LLM-as-a-Judge:** Using a more powerful model (like GPT-
4) to grade the output of a smaller/cheaper model (like

LLaMA-3) based on a rubric (e.g., tone, helpfulness,
accuracy).\n4. **Human-in-the-Loop (HITL):** Integrating
interfaces (like Label Studio) where human annotators rate
outputs to create reinforcement learning feedback loops.\n\n--
-\n\n### 4. Industry-Standard LLM Harness Tools\nIf you are
doing harness engineering today, you will likely use a
combination of these open-source and commercial
tools:\n\n#### Evaluation Frameworks (The "Test"
Harnesses)\n* **lm-evaluation-harness (by EleutherAI):** The
industry standard for academic benchmarking. It is used to
test open-source models on tasks like MMLU, GSM8K, and
HellaSwag to place them on the Hugging Face
Leaderboard.\n* **Promptfoo:** A popular, developer-friendly

CLI tool for testing prompt quality, model outputs, and red-
teaming.\n* **DeepEval / Ragas:** Open-source frameworks

specifically designed for testing **RAG (Retrieval-Augmented
Generation)** systems (measuring faithfulness, answer
relevance, etc.).\n\n#### Guardrail Frameworks (The
"Runtime" Harnesses)\n* **NVIDIA NeMo Guardrails:** An
open-source toolkit for adding programmable guardrails to
LLM-based conversational systems.\n* **Guardrails AI:** A
framework that validates LLM outputs against a specified

schema (e.g., ensuring the output is valid JSON and contains
no PII).\n* **Llama Guard:** A specialized safeguard model by
Meta designed to classify inputs and outputs for
safety.\n\n#### Observability & LLMOps\n* **Langfuse / Arize
Phoenix / Portkey:** Tools that act as LLM application
gateways, tracing calls, tracking latency, and measuring user
feedback (thumbs up/down).\n\n---\n\n### 5. Step-by-Step:
How to Engineer a Basic LLM Harness\nIf you were to build a
basic evaluation harness for a company\'s customer service
bot, the workflow would look like this:\n\n1. **Define the
"Golden Dataset":** Create a spreadsheet of 100 historical
customer questions and the ideal "correct" answers.\n2.
**Write the Test Script:** Use a tool like `promptfoo` or write a
Python script using `Langchain`.\n3. **Run the Prompts:**
Send the 100 questions to your current LLM prompt.\n4.
**Evaluate:**\n * Use a JSON parser to ensure the output
format is correct.\n * Use GPT-4 to score the tone of the
response from 1 to 5.\n5. **Calculate the Score:** Generate a
report (e.g.,

"Prompt Version 1.2 passed 92% of tests,
average latency 1.2 seconds").\n6. **CI/CD Integration:**
Integrate this script into your GitHub Actions. If a developer
changes a prompt and the test score drops below 90%, block
the code from deploying.\n\n### Summary\n**Harness
Engineering** is the bridge between raw LLM capabilities and
enterprise-grade reliability. Without a robust harness,
deploying an LLM to production is a massive risk. By building
robust evaluation and guardrail harnesses, organizations can
confidently iterate on prompts and models without fearing
hallucinations, regressions, or brand damage.
```
### Application 有兩種
 - 1. Standalone Application:例如視窗應用程式,單機使用。```myapp.py```
 - 2. Web Application:部署在Web Server,User Interface 是Browser,online,雲端,cloud

 - ```Python Flask App```
 - ```ChatGPT```、```Gemini``` 網站
### Development(開發) & Deployment (部署) & Maintenence (維護)